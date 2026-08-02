import pytest

from src.utils import Product, Category


@pytest.fixture
def products():
    return Product(
        name="Планшет",
        description="Игровой",
        price=20.00,
        quantity=2,
    )


@pytest.fixture
def products_2():
    return Product(
        name="Смартфон",
        description="Игровой",
        price=90.00,
        quantity=15,
    )


@pytest.fixture
def categories(products, products_2):
    prod_1 = products
    prod_2 = products_2
    return Category(
        name="Электроника",
        description="Мобильная",
        # product = [prod_1, prod_2],
        product=[prod_1, prod_2],
    )


"""Задание 3
Напишите тесты для классов, которые проверяют:

корректность инициализации объектов класса Category
,
корректность инициализации объектов класса Product
,
подсчет количества продуктов,
подсчет количества категорий.


#pytest #assert #fixtures"""
