from dataclasses import dataclass
from typing import List


@dataclass
class Workflow:
    name: str
    steps: List[str]
