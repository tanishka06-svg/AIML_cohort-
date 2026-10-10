
from services.data_loader import load_automation_run


def detect_suspicious_changes(run_id: str) -> str:
    """Identify unusual numeric changes that need human review."""

    try:
        run = load_automation_run(run_id)
    except (FileNotFoundError, ValueError) as error:
        return str(error)

    suspicious_changes = []

    for action in run["actions"]:
        if action.get("type") not in {
            "update_invoice",
            "update_vendor",
        }:
            continue

        before = action.get("before")
        after = action.get("after")

        if before is None or after is None:
            continue

        try:
            before_value = float(before)
            after_value = float(after)
        except (ValueError, TypeError):
            continue

        # Ignore unchanged values and zero starting values.
        if before_value == after_value or before_value == 0:
            continue

        # Flag changes where the new value is at least 5 times
        # the original value, or falls to 20% or less.
        ratio = abs(after_value / before_value)

        if ratio >= 5 or ratio <= 0.2:
            suspicious_changes.append(
                {
                    "action_id": action.get("action_id", "N/A"),
                    "document": action.get("document", "N/A"),
                    "field": action.get("field", "N/A"),
                    "before": before,
                    "after": after,
                    "ratio": ratio,
                }
            )

    if not suspicious_changes:
        return (
            f"Run: {run_id}\n"
            "No unusually large numeric changes were detected."
        )

    report = [
        f"Run: {run_id}",
        f"Changes requiring review: {len(suspicious_changes)}",
        "\nSUSPICIOUS CHANGES:",
    ]

    for change in suspicious_changes:
        report.append(
            f"\nAction ID: {change['action_id']}\n"
            f"Document: {change['document']}\n"
            f"Field: {change['field']}\n"
            f"Before: {change['before']}\n"
            f"After: {change['after']}\n"
            f"Change ratio: {change['ratio']:.2f}x\n"
            "Reason: Large numeric change; human review recommended."
        )

    return "\n".join(report)
