from classes.product import Product


class Category:
    category_name: str
    description_category: str
    __category_products: list
    category_count = 0
    product_count = 0
    cat_list = []

    def __init__(self, category_name, description_category, category_products):
        self.category_name = category_name
        self.description_category = description_category
        self.__category_products = category_products
        Category.category_count += 1
        Category.product_count += len(self.__category_products)
        self.list_goods = []

    def __repr__(self):
        return (f"Имя категории - {self.category_name}; "
                f"Описание категории - {self.description_category}; Список продуктов - {self.__category_products}\n")

    def add_product(self, *args):
        """
        принимает на вход объект товара и добавлять его в список.
        :param product_name:
        :return:
        """
        return self.__category_products.extend(*args)

    @property
    def goods(self):
        category_product_list = ''
        for product in self.list_goods:
            category_product_list += f'{product.product_name}, {product.price} руб. Остаток: {product.quantity_in_stock} шт.\n'
        return category_product_list

    @goods.setter
    def goods(self, item):
        self.list_goods.append(item)
