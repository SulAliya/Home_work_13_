class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, category_name, description_category, category_products):
        self.category_name = category_name
        self.description_category = description_category
        self.category_products = category_products
        Category.category_count += 1
        Category.product_count += len(self.category_products)


# for product_list in products:
#     category_name = functions.get_name_category(product_list)
#     description_category = functions.get_category_description(product_list)
#     category_products = functions.get_category_products(product_list)
#     category = Category(category_name, description_category, category_products)
#     print(Category.product_count)


