
from mcp.server.mcpserver import MCPServer

from tools.analyze_run import analyze_automation_run
from tools.detect_changes import detect_suspicious_changes
from tools.compare_changes import compare_before_after
from tools.review_summary import generate_review_summary
from tools.smart_format_adapter import adapt_format


server = MCPServer("autocomputer-action-auditor")


@server.tool()
def analyze_automation_run_tool(run_id: str) -> str:
    """Analyze an automation run and return its action details."""
    return analyze_automation_run(run_id)


@server.tool()
def detect_suspicious_changes_tool(run_id: str) -> str:
    """Detect unusual changes that may need human review."""
    return detect_suspicious_changes(run_id)


@server.tool()
def compare_before_after_tool(run_id: str) -> str:
    """Compare values before and after automation actions."""
    return compare_before_after(run_id)


@server.tool()
def generate_review_summary_tool(run_id: str) -> str:
    """Generate a summary of an automation run and its review items."""
    return generate_review_summary(run_id)


@server.tool()
def smart_format_adapter_tool(source_data_json: str) -> str:
    """Map unfamiliar spreadsheet column names to standard invoice fields."""
    return adapt_format(source_data_json)


if __name__ == "__main__":
    server.run()
