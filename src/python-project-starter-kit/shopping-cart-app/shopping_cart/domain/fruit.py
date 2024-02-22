from dataclasses import dataclass


@dataclass
class Fruit:
    name: str
    price: float = None
