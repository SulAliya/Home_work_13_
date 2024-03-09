from classes.category import Category


class Product:
    product_name: str
    product_description: str
    price: float
    quantity_in_stock: int
    prod_list = []

    def __init__(self, product_name, product_description, price, quantity_in_stock):
        self.product_name = product_name
        self.product_description = product_description
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def __repr__(self):
        return (f"Имя продукта - {self.product_name} Описание продукта - {self.product_description} "
                f"Стоимость продукта - {self.price} Количество - {self.quantity_in_stock}")

    @classmethod
    def create_product_object(cls, products_list):
        """
        Создаем экземпляры класса Product
        :param products_list
        :return: product_object
        """
        product_name = cls.get_product_name(products_list)
        product_description = cls.get_product_description(products_list)
        price = cls.get_products_price(products_list)
        quantity_in_stock = cls.get_quantity(products_list)
        return cls(product_name, product_description, price, quantity_in_stock)

    @classmethod
    def add_product_object(cls, product_object):
        """
        Создаем список всех категорий
        :param product_object:
        :return: cat_list
        """
        cls.prod_list.append(product_object)
        cls.add_in_category(cls.prod_list)


    @classmethod
    def get_product_list(cls):
        return cls.prod_list

    @classmethod
    def add_in_category(cls, prod):
        return Category.set_product(prod)


    @classmethod
    def create_new_product_object(cls, product_name, product_description, price, quantity_in_stock):
        """
        создали новый экземпляр класса Product
        :param product_name:
        :param product_description:
        :param price:
        :param quantity_in_stock:
        :return: new_product_object
        """
        return cls(product_name, product_description, price, quantity_in_stock)

    @property
    def product_price_func(self):
        return self.price

    @product_price_func.setter
    def product_price_func(self, price):
        if price <= 0:
            print("цена введена некорректная")
        else:
            self.price = price
            print("цена корректная")

    @staticmethod
    def get_product_name(products_list):
        """
        получаем наименование продукта для класса Products.
        :param products_list:
        :return:product_name
        """
        product_name = products_list['name']
        return product_name

    @staticmethod
    def get_product_description(products_list):
        """
        получаем описание продукта.
        :param products_list:
        :return:products_description
        """
        products_description = products_list['description']
        return products_description

    @staticmethod
    def get_products_price(products_list):
        """
        получаем цену продукта.
        :param products_list:
        :return:product_price
        """
        price = products_list['price']
        return price

    @staticmethod
    def get_quantity(products_list):
        """
        получаем количество на складе.
        :param products_list:
        :return:product_quantity
        """
        quantity_in_stock = products_list['quantity']
        return quantity_in_stock
