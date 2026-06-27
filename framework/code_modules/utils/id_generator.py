from datetime import datetime
from uuid import uuid4


def generate_uuid() -> str:
    return str(uuid4())


def generate_workflow_id(workflow_name: str) -> str:
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    return f"{workflow_name}_{timestamp}"


def generate_agent_id(agent_name: str) -> str:
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    return f"{agent_name}_{timestamp}"


def generate_run_id() -> str:
    return f"run_{uuid4().hex[:12]}"
