import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_json(path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def test_demo_has_complete_routing_trace():
    demo_dir = ROOT / "demos" / "lead_qualification_demo"

    assert (demo_dir / "sample_input.json").exists()
    assert (demo_dir / "routing_trace.json").exists()
    assert (demo_dir / "tool_schema.json").exists()
    assert (demo_dir / "expected_output.json").exists()

    routing = load_json(demo_dir / "routing_trace.json")

    assert "selected_agent" in routing
    assert "reason" in routing
    assert "next_step" in routing
    assert routing["selected_agent"]
    assert routing["next_step"]


def test_routed_agent_file_exists():
    demo_dir = ROOT / "demos" / "lead_qualification_demo"
    routing = load_json(demo_dir / "routing_trace.json")

    selected_agent = routing["selected_agent"]
    agent_files = list((ROOT / "agents").rglob("*.json"))

    matching_agents = [
        file for file in agent_files
        if selected_agent in file.name or load_json(file).get("name") == selected_agent
    ]

    assert matching_agents, f"No agent file found for routed agent: {selected_agent}"
