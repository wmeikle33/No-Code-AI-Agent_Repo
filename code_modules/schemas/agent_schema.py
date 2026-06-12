from pydantic import BaseModel
from typing import List, Optional, Dict, Any


class AgentConfig(BaseModel):
    name: str
    description: str
    system_prompt: str
    allowed_tools: List[str] = []
    output_schema: Optional[Dict[str, Any]] = None
    human_review_required: bool = False
