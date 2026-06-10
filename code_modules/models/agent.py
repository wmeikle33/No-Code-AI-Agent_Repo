from dataclasses import dataclass
from typing import List


@dataclass
class Agent:
    name: str
    role: str
    model: str
    tools: List[str]
