
from services.data_loader import load_automation_run
from tools.detect_changes import detect_suspicious_changes


def generate_review_summary(run_id: str) -> str:
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
    try:
        run = load_automation_run(run_id)
    except (FileNotFoundError, ValueError) as error:
        return str(error)

    actions = run["actions"]

    successful = sum(
        1 for action in actions
        if action.get("status") == "success"
    )

    failed = len(actions) - successful

    # Reuse Tool 2 to detect unusual numeric changes.
    suspicious_report = detect_suspicious_changes(run_id)

    suspicious_count = 0
    suspicious_details = []

    for line in suspicious_report.splitlines():
        if line.startswith("Changes requiring review:"):
            try:
                suspicious_count = int(line.split(":", 1)[1].strip())
            except ValueError:
                suspicious_count = 0

    if suspicious_count > 0:
        lines = suspicious_report.splitlines()

        for index, line in enumerate(lines):
            if line.startswith("Action ID:"):
                details = []

                for detail_line in lines[index:index + 7]:
                    if detail_line.startswith("Reason:"):
                        details.append(detail_line)
                        break
                    details.append(detail_line)

                suspicious_details.append("\n".join(details))

    if suspicious_count > 0:
        findings = "\n\n".join(suspicious_details)
    else:
        findings = "No unusually large numeric changes were detected."

    return (
        f"AUTOMATION REVIEW SUMMARY\n"
        f"Run ID: {run.get('run_id', run_id)}\n"
        f"Task: {run.get('task', 'N/A')}\n"
        f"Run status: {run.get('status', 'N/A')}\n\n"
        f"Total actions: {len(actions)}\n"
        f"Successful actions: {successful}\n"
        f"Failed actions: {failed}\n"
        f"Changes requiring review: {suspicious_count}\n\n"
        f"REVIEW FINDINGS:\n{findings}\n\n"
        "RECOMMENDATION:\n"
        "Review the flagged changes before accepting the results. "
        "A flagged change is not necessarily an error. "
        "A human should make the final decision."
    )
