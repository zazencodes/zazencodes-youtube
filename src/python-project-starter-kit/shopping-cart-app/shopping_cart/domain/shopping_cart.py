from dataclasses import dataclass
from typing import List, Optional

from .fruit import Fruit

@dataclass
class ShoppingCart:
    items: List[Fruit]
    score: int = None
