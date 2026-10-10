
import json
from pathlib import Path
from typing import Any


# Get the project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Location of mock automation-run data
RUNS_DIRECTORY = PROJECT_ROOT / "mock_data" / "automation_runs"


def load_automation_run(run_id: str) -> dict[str, Any]:
    """
    Load an automation run from its JSON file.

    Args:
        run_id: The ID of the automation run, e.g. RUN-001.

    Returns:
        The automation run data as a dictionary.

    Raises:
        FileNotFoundError: If the requested run does not exist.
        ValueError: If the JSON file contains invalid data.
    """
    if not run_id.startswith("RUN-"):
        raise ValueError("Invalid run ID format. Expected RUN-001.")

    file_path = RUNS_DIRECTORY / f"{run_id.lower().replace('-', '_')}.json"

    if not file_path.is_file():
        raise FileNotFoundError(
            f"Automation run '{run_id}' was not found."
        )

    try:
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Automation run '{run_id}' contains invalid JSON."
        ) from exc

    if data.get("run_id") != run_id:
        raise ValueError("The run ID in the file does not match the requested ID.")

    if not isinstance(data.get("actions"), list):
        raise ValueError("Invalid automation-run data: actions must be a list.")

    return data
