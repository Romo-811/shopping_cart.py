from product import Product

class ShoppingCart:
    
    def __init__(self):
        self.items = []

    def add_product(self, product):  
        self.items.append(product) 
        print(f'{product.name} has been added to your cart')
 
    def empty_cart(self):
        self.items = []
        print("The cart is now empty")

    def calculate_total_cost(self):
        total_cost = int(0) 
        for product in self.products:
            total_cost = total_cost + product.price
            
        print(f'Your total cost is ${total_cost}')
