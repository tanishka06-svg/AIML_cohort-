
import asyncio
import os
import re
from contextlib import AsyncExitStack

from openai import AsyncOpenAI
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


LLM_BASE_URL = "http://127.0.0.1:8080/v1"
MODEL_NAME = "model.gguf"

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

MCP_SERVER = StdioServerParameters(
    command="uv",
    args=["run", "python", "server.py"],
    cwd=PROJECT_ROOT,
)


def select_tool(question: str, available_tools: set[str]):
    """Choose an MCP tool using simple, predictable routing."""

    text = question.lower()

    match = re.search(r"\bRUN-\d+\b", question, re.IGNORECASE)

    if not match:
        return None, None

    run_id = match.group(0).upper()

    if any(word in text for word in [
        "review", "review summary", "overall summary",
        "final report", "summarize the run",
    ]):
        tool_name = "generate_review_summary_tool"

    elif any(word in text for word in [
        "suspicious", "unusual change", "flagged change",
        "detect changes",
    ]):
        tool_name = "detect_suspicious_changes_tool"

    elif any(word in text for word in [
        "compare", "before and after", "before-after",
        "percentage change",
    ]):
        tool_name = "compare_before_after_tool"

    elif any(word in text for word in [
        "analyze", "analyse", "action details",
        "list actions", "run details",
    ]):
        tool_name = "analyze_automation_run_tool"

    else:
        return None, None

    if tool_name not in available_tools:
        return None, None

    return tool_name, {"run_id": run_id}


async def main():
    client = AsyncOpenAI(
        base_url=LLM_BASE_URL,
        api_key="local",
    )

    async with AsyncExitStack() as stack:
        read_stream, write_stream = await stack.enter_async_context(
            stdio_client(MCP_SERVER)
        )

        session = await stack.enter_async_context(
            ClientSession(read_stream, write_stream)
        )

        await session.initialize()

        tools_result = await session.list_tools()
        available_tools = {tool.name for tool in tools_result.tools}

        print("\nConnected to AutoComputer Action Auditor!")
        print("\nAvailable MCP tools:")

        for tool in tools_result.tools:
            print(f"- {tool.name}: {tool.description}")

        print("\nExamples:")
        print("- Review automation run RUN-001")
        print("- Detect suspicious changes in RUN-001")
        print("- Compare before and after values in RUN-001")
        print("- Analyze action details for RUN-001")
        print("Type 'exit' to quit.")

        while True:
            question = input("\nYou: ").strip()

            if question.lower() == "exit":
                break

            if not question:
                continue

            tool_name, arguments = select_tool(
                question, available_tools
            )

            print(f"DEBUG: Received question: {question!r}")
            print(f"DEBUG: Selected tool: {tool_name!r}")
            print(f"DEBUG: Arguments: {arguments!r}")

            if not tool_name:
                print(
                    "\nI couldn't identify the requested operation. "
                    "Include a run ID such as RUN-001 and specify "
                    "whether you want a review, suspicious-change "
                    "check, comparison, or action analysis."
                )
                continue

            print(f"\nCalling MCP tool: {tool_name}")

            try:
                result = await session.call_tool(
                    tool_name,
                    arguments=arguments,
                )

                tool_output = "\n".join(
                    item.text
                    for item in (result.content or [])
                    if hasattr(item, "text")
                )

                if getattr(result, "isError", False):
                    print(
                        f"\nMCP tool reported an error:\n{tool_output}"
                    )
                    continue

                if not tool_output:
                    tool_output = "The MCP tool returned no text."

                print(f"\nActual MCP result:\n{tool_output}")

                final_response = await client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "Explain the supplied automation audit "
                                "result in simple, clear language. Use "
                                "only facts and numbers in the result. "
                                "Do not invent findings. A flagged change "
                                "requires human review; it is not proof "
                                "of an error."
                            ),
                        },
                        {
                            "role": "user",
                            "content": (
                                f"Original request: {question}\n\n"
                                f"Actual MCP tool result:\n{tool_output}"
                            ),
                        },
                    ],
                    temperature=0,
                    max_tokens=400,
                )

                message = final_response.choices[0].message
                explanation = (message.content or "").strip()

                print("\nBonsai explanation:")

                if explanation:
                    print(explanation)
                else:
                    print("The local model returned no explanation.")
                    print(
                        "\nShowing the actual MCP result instead:\n"
                    )
                    print(tool_output)

            except Exception as error:
                print(f"\nRequest failed: {error}")


if __name__ == "__main__":
    asyncio.run(main())
