class Product:
    product_name: str
    product_description: str
    price: float
    quantity_in_stock: int
    color = str

    def __init__(self, product_name, product_description, price, quantity_in_stock):
        self.product_name = product_name
        self.product_description = product_description
        self.__price = price
        self.quantity_in_stock = quantity_in_stock

    def __repr__(self):
        return (f"Имя продукта - {self.product_name} Описание продукта - {self.product_description} "
                f"Стоимость продукта - {self.__price} Количество - {self.quantity_in_stock}")

    def __str__(self):
        return f'{self.product_name}, {self.__price} руб. Остаток: {self.quantity_in_stock} шт.\n'

    def __add__(self, other):
        """
        сложение двух продуктов - сложением сумм, умноженных на количество на складе.
        :param other:
        :return:
        """
        if isinstance(other, type(self)):
            return self.__price * self.quantity_in_stock + other.__price * other.quantity_in_stock
        else:
            raise TypeError

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


class SmartPhone(Product):
    productivity = str
    model = str
    internal_memory = float
    color = str

    def __init__(self, productivity, model, internal_memory, color, product_name, product_description, price,
                 quantity_in_stock):
        super().__init__(product_name, product_description, price, quantity_in_stock)
        self.productivity = productivity
        self.model = model
        self.internal_memory = internal_memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, manufacturer_country, germination_period, color, product_name, product_description, price,
                 quantity_in_stock):
        super().__init__(product_name, product_description, price, quantity_in_stock)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
        self.color = color
