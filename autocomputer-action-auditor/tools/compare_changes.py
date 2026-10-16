
from services.data_loader import load_automation_run


def compare_before_after(run_id: str) -> str:
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

    try:
        run = load_automation_run(run_id)
    except (FileNotFoundError, ValueError) as error:
        return str(error)

    comparisons = []

    for action in run["actions"]:
        if "before" not in action or "after" not in action:
            continue

        before = action["before"]
        after = action["after"]

        if str(before) == str(after):
            continue

        action_id = action.get("action_id", "N/A")
        document = action.get("document", "N/A")
        field = action.get("field", "N/A")

        result = (
            f"Action ID: {action_id}\n"
            f"Document: {document}\n"
            f"Field: {field}\n"
            f"Before: {before}\n"
            f"After: {after}"
        )

        try:
            old_value = float(before)
            new_value = float(after)
            difference = new_value - old_value

            result += f"\nDifference: {difference:g}"

            if old_value != 0:
                percentage = difference / abs(old_value) * 100
                result += f"\nPercentage change: {percentage:+.2f}%"
            else:
                result += "\nPercentage change: Not available (original value was zero)"

        except (ValueError, TypeError):
            result += "\nChange type: Non-numeric value change"

        comparisons.append(result)

    if not comparisons:
        return f"Run: {run_id}\nNo before-and-after changes were found."

    return (
        f"Run: {run_id}\n"
        f"Changed actions: {len(comparisons)}\n\n"
        "BEFORE-AND-AFTER COMPARISON:\n\n"
        + "\n\n".join(comparisons)
    )
