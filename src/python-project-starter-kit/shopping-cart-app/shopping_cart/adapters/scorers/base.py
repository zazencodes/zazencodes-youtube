
from ...domain.shopping_cart import ShoppingCart

class BaseShoppingCartScorer:
    def __init__(self):
        pass

    def score_shopping_cart(self, cart: ShoppingCart) -> int:
        score = sum([item.price or 0 for item in cart.items])
        return int(score)



