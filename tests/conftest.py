import pytest

from src.utils import Category, Product


@pytest.fixture
def products_1():
    """фикстура продукт 1"""
    return Product(
        name="Планшет",
        description="Игровой",
        price=20.00,
        quantity=2,
    )


@pytest.fixture
def products_2():
    """фикстура продукт 2"""
    return Product(
        name="Смартфон",
        description="Игровой",
        price=90.00,
        quantity=15,
    )


@pytest.fixture
def categories(products_1, products_2):
    """фикстура категории"""
    prod_1 = products_1
    prod_2 = products_2
    return Category(
        name="Электроника",
        description="Мобильная",
        products=[prod_1, prod_2],
    )
