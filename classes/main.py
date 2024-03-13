from classes.category import Category
from classes.product import Product

category_1 = Category('Смартфоны', 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни',['Samsung Galaxy C23 Ultra', 'Iphone 15', 'Xiaomi Redmi Note 11'])
category_2 = Category('Телевизоры', 'Современный телевизор, который позволяет наслаждаться '
                                    'просмотром, станет вашим другом и помощником', '55\" QLED 4K')


product_1 = Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера',
                    180000.0, 5)
product_2 = Product('Iphone 15', '512GB, Gray space', 210000.0, 8)
product_3 = Product('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14)
product_4 = Product('55\" QLED 4K', 'Фоновая подсветка', 123000.0, 7)

product_5 = Product.create_new_product_object(product_name='Nokia', product_description='16 мб, Синий', price=6000.0, quantity_in_stock=3)
product_6 = Product.create_new_product_object(product_name='LG', product_description='Смарт ТВ', price=22000.0, quantity_in_stock=4)
print(f'Новый продукт {product_5}\n') # проверяем новый объект.
print(f'Новый продукт {product_6}\n')

product_1.price = -120 # проверяем корректность введенной цены.

category_1.add_product = product_1
category_1.add_product = product_2
category_1.add_product = product_3
category_2.add_product = product_4
category_2.add_product = product_5

print(f' Длина первой категории до добавления {len(category_1.category_products)}')
print(category_1.category_products)
print(f' Длина второй категории до добавления {len(category_2.category_products)}')
Category.add_product(category_1, product_5)
# Category.add_product(category_2, product_6)
print(f' Длина первой категории после добавления {len(category_1.category_products)}')
print(category_1.category_products)
print(category_2.category_products)
print(category_2.category_products)
