import pytest

from Home_work_13.classes.category import Category
from Home_work_13.classes.functions import load_product_list
from Home_work_13.classes.product import Product
from Home_work_13.classes import functions

@pytest.fixture

def name_category():
    # return Category('category_name',
    #                 'description_category',
    #                 'category_products')
    all_product=load_product_list()
    category_list = []
    for product_list in all_product:
        category_name = functions.get_name_category(product_list)
        description_category = functions.get_category_description(product_list)
        category_products = functions.get_category_products(product_list)
        category = Category(category_name, description_category, category_products)
        category_list.append(category)
    return category_list


def test_init_category(name_category):
    assert name_category[1].category_name == "Телевизоры"
    assert name_category[1].description_category == (
        'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником')
    assert name_category[1].category_products == [{'name': '55" QLED 4K', 'description': 'Фоновая подсветка', 'price': 123000.0, 'quantity': 7}]


def test_quantity(name_category):
    assert name_category[1].category_count == 2


@pytest.fixture
def product_names():
    return Product('product_name', 'product_description', 'price', 'quantity_in_stock')


def test_init_product(product_names):
    assert product_names.product_name == '55" QLED 4K'
    assert product_names.product_description == 'Фоновая подсветка'
    assert product_names.price == 123000.0
    assert product_names.quantity_in_stock == 7


def test_quantity_product(name_category):
    assert name_category.product_count == 4