class Product:
    product_name: str
    product_description: str
    price: float
    quantity_in_stock: int

    def __init__(self, product_name, product_description, price, quantity_in_stock):
        self.product_name = product_name
        self.product_description = product_description
        self.price = price
        self.quantity_in_stock = quantity_in_stock
