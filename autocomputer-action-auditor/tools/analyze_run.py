
from services.data_loader import load_automation_run


def analyze_automation_run(run_id: str) -> str:
    """Summarize an automation run and display its action details."""

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
