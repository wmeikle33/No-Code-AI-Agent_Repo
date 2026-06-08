import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

JSON_DIRS = [
    "agents",
    "tools",
    "workflows",
    "demos",
]

REQUIRED_AGENT_FIELDS = ["name", "description"]
REQUIRED_TOOL_FIELDS = ["name", "description"]
REQUIRED_WORKFLOW_FIELDS = ["name"]


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def test_all_json_files_are_valid():
    json_files = []
    for folder in JSON_DIRS:
        path = ROOT / folder
        if path.exists():
            json_files.extend(path.rglob("*.json"))

    assert json_files, "No JSON files found to test."

    for file in json_files:
        try:
            load_json(file)
        except json.JSONDecodeError as e:
            raise AssertionError(f"Invalid JSON in {file}: {e}")


def test_agent_files_have_required_fields():
    agents_dir = ROOT / "agents"
    if not agents_dir.exists():
        return

    for file in agents_dir.rglob("*.json"):
        data = load_json(file)
        for field in REQUIRED_AGENT_FIELDS:
            assert field in data, f"{file} missing required field: {field}"


def test_tool_files_have_required_fields():
    tools_dir = ROOT / "tools"
    if not tools_dir.exists():
        return

    for file in tools_dir.rglob("*.json"):
        data = load_json(file)
        for field in REQUIRED_TOOL_FIELDS:
            assert field in data, f"{file} missing required field: {field}"


def test_workflow_files_have_required_fields():
    workflows_dir = ROOT / "workflows"
    if not workflows_dir.exists():
        return

    for file in workflows_dir.rglob("*.json"):
        data = load_json(file)
        for field in REQUIRED_WORKFLOW_FIELDS:
            assert field in data, f"{file} missing required field: {field}"
