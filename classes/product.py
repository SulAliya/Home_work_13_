from Home_work_13.classes import functions

products = functions.load_product_list()
for product_list in products:
    products_name = functions.get_products_name(product_list)
    products_description = functions.get_products_description(product_list)
    product_price = functions.get_products_price(product_list)
    quantity = functions.get_quantity(product_list)

class Product:
    product_name: str
    product_description: str
    price: float
    quantity_in_stock: int

    def __init__(self, product_name, product_description, price, quantity_in_stock):
        self.product_name = products_name
        self.product_description = products_description
        self.price = product_price
        self.quantity_in_stock = quantity


product_1 = Product(products_name, products_description, product_price, quantity)

print(product_1.quantity_in_stock)