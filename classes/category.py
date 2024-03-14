from classes.product import Product


class Category:
    category_name: str
    description_category: str
    category_products: list
    category_count = 0
    product_count = 0

    def __init__(self, category_name, description_category, category_products):
        self.category_name = category_name
        self.description_category = description_category
        self.__category_products = category_products

        Category.category_count += 1
        Category.product_count += len(self.__category_products)

    def __repr__(self):
        return (f"Имя категории - {self.category_name}; "
                f"Описание категории - {self.description_category}; Список продуктов - {self.__category_products}\n")

    def add_product(self, product_name):
        """
        принимает на вход объект товара и добавлять его в список.
        :param product_name:
        :return:
        """
        if isinstance(product_name, Product):
            self.__category_products.append(product_name)
            Category.product_count += 1
        else:
            print("Продукт должен быть объектом класса Product")

    @property
    def category_products(self):
        result = []
        for product in self.__category_products:
            result.append(f'{product.product_name}, {product.price} руб. Остаток: {product.quantity_in_stock} шт.')
        return result

    @category_products.setter
    def category_products(self, item):
        self.__category_products.append(item)
