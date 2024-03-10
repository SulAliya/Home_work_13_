
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

    def __repr__(self):
        return (f"Имя продукта - {self.product_name} Описание продукта - {self.product_description} "
                f"Стоимость продукта - {self.price} Количество - {self.quantity_in_stock}")

    @staticmethod
    def my_decorator(func):
        def inner(**kwargs):
            result = func(**kwargs)
            result2 = {
                "Имя продукта": result.product_name,
                "Описание продукта": result.product_description,
                'Стоимость продукта': result.price,
                'Количество': result.quantity_in_stock
            }
            # print(f"Создали новый экземпляр товара = {result2}")
            return result2
        return inner

    @staticmethod
    @my_decorator
    def create_new_product_object(**kwargs):
        """
        создали новый экземпляр класса Product
        """
        new_product_object = Product(**kwargs)
        return new_product_object

    @property
    def product_price_func(self):
        return self.price

    @product_price_func.setter
    def product_price_func(self, new_price):
        if new_price <= 0:
            print("цена введена некорректная")
        else:
            self.price = new_price
            print("цена корректная")
