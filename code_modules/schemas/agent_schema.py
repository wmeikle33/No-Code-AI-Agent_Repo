from pydantic import BaseModel
from typing import List


class AgentSchema(BaseModel):
    name: str
    role: str
    model: str
    tools: List[str]
