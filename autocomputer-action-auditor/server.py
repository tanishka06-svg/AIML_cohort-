
from mcp.server.mcpserver import MCPServer

from tools.analyze_run import analyze_automation_run
from tools.detect_changes import detect_suspicious_changes
from tools.compare_changes import compare_before_after
from tools.review_summary import generate_review_summary
from tools.smart_format_adapter import adapt_format


server = MCPServer("autocomputer-action-auditor")


@server.tool()
def analyze_automation_run_tool(run_id: str) -> str:
    """
Analyze an automation run and provide an overview of its recorded actions.

Use this tool when the user wants to:
- Inspect a specific automation run using its run ID.
- See the actions performed during the run.
- Check action details and execution statuses.
- Understand what happened during an automation task.

Input:
    run_id: The ID of the automation run to analyze, such as "RUN-001".

Returns:
    A summary of the run and its recorded action details.

Do not use this tool solely to detect suspicious numerical changes;
use detect_suspicious_changes for that purpose. Use
generate_review_summary when the user wants a concise review report.
"""
    return analyze_automation_run(run_id)


@server.tool()
def detect_suspicious_changes_tool(run_id: str) -> str:
    """
Detect unusually large or small numerical changes in an automation run.

Use this tool when the user asks to:
- Find suspicious or unusual numerical changes.
- Identify values that may need human review.
- Flag potentially risky changes in recorded automation data.
- Investigate whether a numerical update looks unusual.

Input:
    run_id: The ID of the automation run to inspect, such as "RUN-001".

Returns:
    Details of changes that meet the tool's predefined suspicious-change
    rules, along with reasons for flagging them.

The tool uses predefined numerical thresholds. A flagged change is
a warning for human review, not proof of an error or fraud.

Do not use this tool for a complete list of all differences;
use compare_before_after for that purpose.
"""
    return detect_suspicious_changes(run_id)


@server.tool()
def compare_before_after_tool(run_id: str) -> str:
    """
Compare recorded before-and-after values in an automation run.

Use this tool when the user wants to:
- Compare values before and after an action.
- Find what changed in the recorded data.
- Calculate numerical differences or percentage changes.
- Understand how a value was modified during automation.

Input:
    run_id: The ID of the automation run to compare, such as "RUN-001".

Returns:
    Details of recorded changes, including before-and-after values
    and numerical differences or percentages where applicable.

This tool compares values already recorded in the run data. It does
not independently retrieve historical values from a live application.

Use detect_suspicious_changes to identify changes that cross the
predefined suspicious-change thresholds. Use this tool when the main
goal is to understand the differences themselves.
"""
    return compare_before_after(run_id)


@server.tool()
def generate_review_summary_tool(run_id: str) -> str:
    """
Generate a concise review summary for an automation run.

Use this tool when the user wants to:
- Get an overall summary of an automation run.
- See the total number of actions, successful actions, and failed actions.
- See how many changes require human review.
- Obtain a report combining run statistics and review findings.

Input:
    run_id: The ID of the automation run to summarize, such as "RUN-001".

Returns:
    A formatted review summary containing run information, action
    statistics, and detected changes that may require human attention.

This tool combines information from the run data and suspicious-change
detection. It does not independently verify whether a flagged change
is actually incorrect.

Use analyze_automation_run for detailed action-by-action information,
or detect_suspicious_changes for focused suspicious-change detection.
"""
    return generate_review_summary(run_id)


@server.tool()
def smart_format_adapter_tool(source_data_json: str) -> str:
   def adapt_format(source_data_json: str) -> str:
    """
    Standardize invoice data by mapping supported column names to
    predefined standard fields.

    Use this tool when the user wants to:
    - Convert invoice column names into standard field names.
    - Map supplier or vendor columns to vendor_name.
    - Map amount-related columns to invoice_amount.
    - Map invoice or bill number columns to invoice_number.
    - Identify unknown columns or ambiguous field matches.

    Input:
        source_data_json: A valid JSON string containing:
            - "columns": A list of column names.
            - "rows": A list of objects containing the corresponding values.

    Returns:
        A JSON string containing:
            - column_mapping: Original names mapped to standard fields.
            - adapted_rows: Data using the standard field names.
            - unmapped_columns: Columns not used in the mapping.
            - needs_review: Fields with multiple possible matches.
            - message: A reminder to review the mapping.

    The tool uses predefined aliases, not machine learning or RAG.
    It does not verify invoice authenticity or financial correctness.

    Use this tool for column-name standardization, not for comparing
    before-and-after values or detecting suspicious changes.
    """
    return adapt_format(source_data_json)


if __name__ == "__main__":
    server.run()
