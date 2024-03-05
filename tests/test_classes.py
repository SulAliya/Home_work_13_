import pytest

from classes.category import Category
from classes.functions import load_product_list
from classes.product import Product
from classes import functions

@pytest.fixture

def name_category():
    all_product = load_product_list()
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
    assert name_category[1].category_count == 4


@pytest.fixture
def product_names():
    all_product = load_product_list()
    prod_list = []
    for product_list in all_product:
        products_name = functions.get_products_name(product_list)
        products_description = functions.get_products_description(product_list)
        price = functions.get_products_price(product_list)
        quantity_in_stock = functions.get_quantity(product_list)
        product = Product(products_name, products_description, price, quantity_in_stock)
        prod_list.append(product)
    return prod_list


def test_init_product(product_names):
    assert product_names[1].product_name == '55" QLED 4K'
    assert product_names[1].product_description == 'Фоновая подсветка'
    assert product_names[1].price == 123000.0
    assert product_names[1].quantity_in_stock == 7


def test_quantity_product(name_category):
    assert name_category[1].product_count == 12