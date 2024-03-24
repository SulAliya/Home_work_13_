from classes.category import Category
# from classes.category import CategoryIter
from classes.product import Product, SmartPhone, LawnGrass

#продукты
product_1 = Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера',
                    180000.0, 5)
product_2 = Product('Iphone 15', '512GB, Gray space', 210000.0, 8)
product_3 = Product('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14)
product_4 = Product('55\" QLED 4K', 'Фоновая подсветка', 123000.0, 7)
product_5 = Product.create_new_product_object(product_name='Nokia', product_description='16 мб, Синий', price=6000.0,
                                              quantity_in_stock=0)
product_6 = Product.create_new_product_object(product_name='LG', product_description='Смарт ТВ', price=22000.0,
                                              quantity_in_stock=4)
#категория
category_1 = Category('Смартфоны',
                      'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для '
                      'удобства жизни',
                      [product_1, product_2, product_3])
category_2 = Category('Телевизоры', 'Современный телевизор, который позволяет наслаждаться '
                                    'просмотром, станет вашим другом и помощником', [product_4])

print(f'Новый продукт {product_5}\n')  # проверяем новый объект.
print(f'Новый продукт {product_6}\n')
# product_1.price = -120  # проверяем корректность введенной цены.
# print(f'Длина первой категории до добавления {category_1.get_product_count()}')
# print(f'Длина второй категории до добавления {category_2.get_product_count()}\n')
# print(f'{category_1.category_products}')
# print(f'{category_2.category_products}\n')
Category.add_product(category_1, product_5)  # добавляем продукт в категорию 1
Category.add_product(category_2, product_6)  # добавляем продукт в категорию 2
print(f'Длина первой категории после добавления {category_1.get_product_count()}')
print(f'Длина второй категории после добавления {category_2.get_product_count()}\n')
print(category_1.category_products)
print(category_2.category_products)
print(category_1, category_2)
print(product_1, product_2)
# sum_price = product_5 + product_1
# print(sum_price)  # результат выполнения сложения двух продуктов, т.е сложение сумм, умноженных на количество на складе
# Tv = CategoryIter(category_2.category_name, category_2.category_products)  #
# for item in Tv:
#     print(item, end='')
# print(Product.__mro__)
# print(SmartPhone.__mro__)
# print(LawnGrass.__mro__)