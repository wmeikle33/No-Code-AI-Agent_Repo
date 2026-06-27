from dataclasses import dataclass

@dataclass
class Employee:
    id: str
    name: str
    description: str
    role: str
    active: bool = True
