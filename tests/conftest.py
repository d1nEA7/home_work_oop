import pytest

from src.utils import Category, LawnGrass, Product, Smartphone


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


@pytest.fixture
def smartphone_1():
    """фикстура для класса смартфон"""
    return Smartphone(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=100000.0,
        quantity=10,
        efficiency=95.5,
        model="S23 Ultra",
        memory=256,
        color="Серый",
    )


@pytest.fixture
def smartphone_2():
    """фикстура для класса смартфон 2"""
    return Smartphone(
        name="poco X5 5G",
        description="256GB, Черный цвет, 48MP камера",
        price=25000.0,
        quantity=1,
        efficiency=90.5,
        model="X5 5G",
        memory=256,
        color="Черный",
    )


@pytest.fixture
def lawn_grass_1():
    """фикстура для класса lawn_grass"""
    return LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=600.0,
        quantity=2,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый",
    )
