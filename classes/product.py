class Product:
    product_name: str
    product_description: str
    price: float
    quantity_in_stock: int

    def __init__(self, product_name, product_description, price, quantity_in_stock):
        self.product_name = product_name
        self.product_description = product_description
        self.__price = price
        self.quantity_in_stock = quantity_in_stock

    def __repr__(self):
        return (f"Имя продукта - {self.product_name} Описание продукта - {self.product_description} "
                f"Стоимость продукта - {self.__price} Количество - {self.quantity_in_stock}")

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

    @classmethod
    def create_new_product_object(cls, **kwargs):
        """
        создали новый экземпляр класса Product
        """
        product_name = kwargs['product_name']
        product_description = kwargs['product_description']
        price = kwargs['price']
        quantity_in_stock = kwargs['quantity_in_stock']
        return cls(product_name, product_description, price, quantity_in_stock)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("цена введена некорректная")
        else:
            self.__price = new_price
            print("цена корректная")
