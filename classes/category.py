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

    def __repr__(self):
        return (f"Имя категории - {self.category_name}; "
                f"Описание категории - {self.description_category}; Список продуктов - {self.__category_products}\n")

    @classmethod
    def create_category_object(cls, category_list):
        """
        Создаем экземпляры класса Category
        :param category_list
        :return: category_object
        """
        category_name = cls.get_category_name(category_list)
        description_category = cls.get_description_category(category_list)
        category_products = cls.get_category(category_list)
        return cls(category_name, description_category, category_products)

    @classmethod
    def add_category_object(cls, category_object):
        """
        Создаем список всех категорий
        :param category_object:
        :return: cat_list
        """
        cls.cat_list.append(category_object)

    @classmethod
    def get_category_list(cls):
        return cls.cat_list

    def add_product_object(self, product_obj):
        """
        метод для добавления товаров в категорию (в список). Метод должен добавлять в список экземпляр класса Product,
        соответственно список будет состоять из экземлпяров класса Product.
        :param product_obj:принимоет объект класса продукт
        :return:
        """
        self.__category_products.append(product_obj)
        print(self.__category_products)
        return self.__category_products

    @property
    def get_category_products(self):
        category_products = ''
        for product in self.__category_products:
            category_products += f'{product.product_name}, {product.price} руб. Остаток:{product.quantity_in_stock} шт.'
        return category_products

    @staticmethod
    def get_category_name(category_list):
        """
        получаем наименование категории
        :return:category_name
        """
        category_name = category_list['name']
        return category_name

    @staticmethod
    def get_description_category(category_list):
        """
        получаем описание категории
        :return:category_description
        """
        description_category = category_list['description']
        return description_category

    @staticmethod
    def get_category(category_list):
        """
        Получаем список товаров в категории
        :return:category_products
        """
        category_products = category_list['products']
        return category_products
