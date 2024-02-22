# from shopping_cart.shopping_cart import initialize_shopping_cart, add_fruit_to_cart, remove_fruit_from_cart
# from shopping_cart.fruit import Fruit
from shopping_cart import initialize_shopping_cart, add_fruit_to_cart, remove_fruit_from_cart, score_shopping_cart
from shopping_cart import Fruit
from typing import List

SCORER_TYPE = "apex"

def create_happy_cart(fave_fruits: str):
    fruit_names : List[str] = _parse_fruits_arg(fave_fruits)
    
    cart = initialize_shopping_cart()
    for fruit_name in fruit_names:
        fruit = Fruit(name=fruit_name, price=99)
        add_fruit_to_cart(cart, fruit)

    print("Happy cart created!")
    print(score_shopping_cart(cart, SCORER_TYPE))

    print("Cart scored:")
    print(cart)


def _parse_fruits_arg(fave_fruits: str) -> List[str]:
    return [fruit.strip() for fruit in fave_fruits.split(",") if fruit.strip()]


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--fave-fruits", required=True, help="All your favorite fruits!")
    args = parser.parse_args()
    create_happy_cart(args.fave_fruits)




