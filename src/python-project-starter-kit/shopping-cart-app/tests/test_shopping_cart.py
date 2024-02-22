import unittest

from shopping_cart.shopping_cart import initialize_shopping_cart, add_fruit_to_cart, remove_fruit_from_cart
from shopping_cart.fruit import Fruit
ShoppingCart
class TestShoppingCart(unittest.TestCase):

    def test_initialize_shopping_cart(self):
        cart = initialize_shopping_cart()
        self.assertEqual(len(cart.items), 0)

    def test_add_fruit_to_cart(self):
        cart = initialize_shopping_cart()
        apple = Fruit(name="Apple", price=1.2)
        add_fruit_to_cart(cart, apple)
        self.assertEqual(len(cart.items), 1)
        self.assertEqual(cart.items[0].name, "Apple")
        self.assertEqual(cart.items[0].price, 1.2)

    def test_remove_fruit_from_cart(self):
        cart = initialize_shopping_cart()
        apple = Fruit(name="Apple", price=1.2)
        add_fruit_to_cart(cart, apple)
        self.assertEqual(len(cart.items), 1)

        removed_fruit = remove_fruit_from_cart(cart, "Apple")
        self.assertEqual(removed_fruit.name, "Apple")
        self.assertEqual(len(cart.items), 0)

        # Test the null case
        removed_fruit = remove_fruit_from_cart(cart, "Apple")
        self.assertIsNone(removed_fruit)
        self.assertEqual(len(cart.items), 0)

if __name__ == "__main__":
    unittest.main()



