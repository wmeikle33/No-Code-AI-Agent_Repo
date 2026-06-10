from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class WorkflowState:
    user_request: str
    selected_agent: Optional[str] = None
    tool_outputs: Dict[str, Any] = field(default_factory=dict)
    final_output: Optional[Dict[str, Any]] = None
    requires_human_review: bool = False
    errors: List[str] = field(default_factory=list)
