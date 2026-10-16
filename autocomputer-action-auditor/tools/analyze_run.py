
from services.data_loader import load_automation_run


def analyze_automation_run(run_id: str) -> str:
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
    try:
        run = load_automation_run(run_id)
    except (FileNotFoundError, ValueError) as error:
        return str(error)

    # Get all actions from the automation run
    actions = run["actions"]

    # Count successful and failed actions
    successful = sum(
        1
        for action in actions
        if action.get("status") == "success"
    )

    failed = len(actions) - successful

    # Prepare details for every action
    action_details = []

    for action in actions:
        detail = (
            f"Action ID: {action.get('action_id', 'N/A')}\n"
            f"Type: {action.get('type', 'N/A')}\n"
            f"Document: {action.get('document', 'N/A')}\n"
            f"Status: {action.get('status', 'N/A')}"
        )

        # Include before-and-after values when available
        if "field" in action:
            detail += (
                f"\nField: {action.get('field', 'N/A')}"
                f"\nBefore: {action.get('before', 'N/A')}"
                f"\nAfter: {action.get('after', 'N/A')}"
            )

        action_details.append(detail)

    # Return the complete report
    report = (
        f"Run: {run.get('run_id', 'N/A')}\n"
        f"Task: {run.get('task', 'N/A')}\n"
        f"Status: {run.get('status', 'N/A')}\n"
        f"Total actions: {len(actions)}\n"
        f"Successful actions: {successful}\n"
        f"Failed actions: {failed}\n\n"
        f"ACTION DETAILS:\n"
        + "\n\n".join(action_details)
    )

    return report
