
from typing import List, Optional
from ..domain.shopping_cart import ShoppingCart
from ..domain.fruit import Fruit
from ..adapters import get_scorer



def initialize_shopping_cart() -> ShoppingCart:
    """
    Initialize a new shopping cart object.
    """
    return ShoppingCart(items=[])


def add_fruit_to_cart(cart: ShoppingCart, fruit: Fruit) -> None:
    """
    Add fruit to the shopping cart.
    """
    cart.items.append(fruit)

def remove_fruit_from_cart(cart: ShoppingCart, fruit_name: str) -> Optional[Fruit]:
    """
    Remove fruit by name from the shopping cart.
    """
    for idx, item in enumerate(cart.items):
        if item.name == fruit_name:
            return cart.items.pop(idx)
    return None

def score_shopping_cart(cart: ShoppingCart, scorer_type: str):
    """
    Assign a score to the shopping cart
    based on the contents using an ML model.
    """
    ScorerCls = get_scorer(scorer_type=scorer_type)
    scorer = ScorerCls()
    cart_score = scorer.score_shopping_cart(cart)
    print(f"Assigning score to cart: {cart_score}")
    cart.score = cart_score




