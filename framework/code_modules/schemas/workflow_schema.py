from pydantic import BaseModel
from typing import List


class WorkflowSchema(BaseModel):
    name: str
    description: str
    steps: List[str]
