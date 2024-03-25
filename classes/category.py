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

    def __len__(self):
        len_products = 0
        for i in self.__category_products:
            len_products += i.quantity_in_stock
        return len_products

    def __str__(self):
        return f'{self.category_name},  количество продуктов: {self.__len__()} шт.\n'

    def add_product(self, product_name):
        """
        принимает на вход объект товара и добавлять его в список.
        :param product_name:
        :return:
        """
        if isinstance(product_name, Product):
            self.__category_products.append(product_name)
            Category.product_count += 1
            if product_name.quantity_in_stock == 0:
                raise ValueError('Товар с нулевым количеством не может быть добавлен')
        else:
            print("Продукт должен быть объектом класса Product")

    def average_price(self):
        """
        метод, который подсчитывает средний ценник всех товаров.
        :return:
        """
        try:
            result = 0
            for product in self.__category_products:
                result += product.price * product.quantity_in_stock
            return f'Средний чек {result / len(self)}'
        except ZeroDivisionError:
            print('0')

    def get_product_count(self):
        return len(self.__category_products)

    @property
    def category_products(self):
        result = ''
        for product in self.__category_products:
            result += f'{product.product_name}, {product.price} руб. Остаток: {product.quantity_in_stock} шт.\n'
        return result


# class CategoryIter:
#     """
#     принимает на вход категорию и дает возможность использовать цикл for для прохода по всем товарам данной категории
#     """
#
#     def __init__(self, category_name, category_products):
#         self.category_name = category_name
#         self.__category_products = category_products
#         self.index = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.index += 1
#         if self.index >= len(self.__category_products):
#             raise StopIteration
#         else:
#             return self.__category_products[self.index]
