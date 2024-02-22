from typing import Union
from .scorers.apex import ApexShoppingCartScorer
from .scorers.base import BaseShoppingCartScorer

def get_scorer(scorer_type: str) -> Union[ApexShoppingCartScorer, BaseShoppingCartScorer]:
    if scorer_type == "apex":
        return ApexShoppingCartScorer
    elif scorer_type == "base":
        return BaseShoppingCartScorer
    else:
        raise ValueError(f"No scorer {scorer_type}!")

