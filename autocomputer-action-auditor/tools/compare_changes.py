
from services.data_loader import load_automation_run


def compare_before_after(run_id: str) -> str:
    """Compare before-and-after values in an automation run."""

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
