from classes.category import Category
from classes.product import Product
from classes.functions import load_product_list

products = load_product_list()
cat_list = []
prod_list = []

for i in range(len(products)):
    category_list = products[i]
    category_object = Category.create_category_object(category_list)
    Category.add_category_object(category_object)
cat_list = Category.get_category_list()
print(f"Список категорий: {cat_list}")
print(f"Количество категорий: {len(cat_list)}\n")


for i in range(len(products)):
    for j in range(len(products[i]['products'])):
        products_list = products[i]['products'][j]
        product_object = Product.create_product_object(products_list)
        Product.add_product_object(product_object)
        print(product_object)
prod_list = Product.get_product_list()
print(f"Список продуктов: {prod_list}")
print(f"Количество продуктов: {len(prod_list)}\n")


new_product_object = Product.create_new_product_object('Iphone 5', "128GB, Gray space", 10000.0, 3)
print("Создали новый продукт:", new_product_object)
Product.add_product_object(new_product_object)
prod_list = Product.get_product_list()
print(f"Список продуктов после добавления: {prod_list}")
print(f"Количество продуктов после добавления: {len(prod_list)}\n")
