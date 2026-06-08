from dataclasses import dataclass

@dataclass
class Lead:
    id: str
    name: str
    description: str
    role: str
    active: bool = False
