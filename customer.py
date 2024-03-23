from shopping_cart import ShoppingCart

class Customer:

    def __init__(self, name):
        self.customer_name = name
        self.cart = ShoppingCart()

    def add_item_to_cart(self, product):
        self.cart.add_product(product)

    def view_cart(self):
        for product in self.cart.items:
            print(product.name)




