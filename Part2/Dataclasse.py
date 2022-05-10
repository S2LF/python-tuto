from dataclasses import dataclass
from typing import ClassVar

@dataclass
class User:
    first_name: str
    last_name: str = ""

    c: ClassVar[int]

    def __post_init__(self):
        self.full_name = f"{self.first_name} {self.last_name}"

patrick = User('Patrick', 'Hedlund')
print(patrick.first_name)
print(repr(patrick))

print(patrick.__dict__)
print(patrick.full_name)