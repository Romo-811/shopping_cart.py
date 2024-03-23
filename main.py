from customer import Customer
from product import Product

customer_one = Customer("Chad")
product_one = Product("tire", 100, "Auto")
product_two = Product("wheels", 50, "Auto")
product_three = Product("valves", 10, "Auto")
product_four = Product("lug nuts", 5, "Auto")

customer_one.add_item_to_cart(product_one)
customer_one.add_item_to_cart(product_two)
customer_one.add_item_to_cart(product_three)
customer_one.add_item_to_cart(product_four)
customer_one.view_cart


