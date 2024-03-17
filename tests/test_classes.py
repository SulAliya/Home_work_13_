import pytest
from classes.category import Category
from classes.product import Product


@pytest.fixture
def name_category():
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
                    [
                        {
                            "name": "Samsung Galaxy C23 Ultra",
                            "description": "256GB, Серый цвет, 200MP камера",
                            "price": 180000.0,
                            "quantity": 5
                        },
                        {
                            "name": "Iphone 15",
                            "description": "512GB, Gray space",
                            "price": 210000.0,
                            "quantity": 8
                        },
                        {
                            "name": "Xiaomi Redmi Note 11",
                            "description": "1024GB, Синий",
                            "price": 31000.0,
                            "quantity": 14
                        }
                    ]
                    )


def test_init_category(name_category):
    """
    тест на корректность инициализации объектов класса Category.
    """
    assert name_category.category_name == 'Смартфоны'
    assert name_category.description_category == (
        'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни')
    assert name_category.category_products == [
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5
        },
        {
            "name": "Iphone 15",
            "description": "512GB, Gray space",
            "price": 210000.0,
            "quantity": 8
        },
        {
            "name": "Xiaomi Redmi Note 11",
            "description": "1024GB, Синий",
            "price": 31000.0,
            "quantity": 14
        }
    ]


def test_quantity_category(name_category):
    """
    тест на подсчёт количества категорий.
    :param name_category:
    :return:
    """
    assert name_category.category_count == 1


def test_quantity_product(name_category):
    assert name_category.product_count == 3


@pytest.fixture
def product_names():
    return Product('55" QLED 4K', 'Фоновая подсветка', 123000.0, 7)


def test_init_product(product_names):
    """
    тест на корректность инициализации объектов класса Product.
    :param product_names:
    :return:
    """
    assert product_names.product_name == '55" QLED 4K'
    assert product_names.product_description == 'Фоновая подсветка'
    assert product_names.price == 123000.0
    assert product_names.quantity_in_stock == 7
