from src.utils import Category, Product


def test_category_init(categories):
    """тесты для инициализации категорий"""
    assert categories.name == "Электроника"
    assert categories.description == "Мобильная"
    assert len(categories.products) == 2
    assert categories.product_count == 2
    assert categories.count_categories == 1


def test_product_init(products_1):
    """тесты для инициализации продуктов_1"""
    assert products_1.name == "Планшет"
    assert products_1.description == "Игровой"
    assert products_1.price == 20.00
    assert products_1.quantity == 2


def test_product_init_2(products_2):
    """тесты для инициализации продуктов_2"""
    assert products_2.name == "Смартфон"
    assert products_2.description == "Игровой"
    assert products_2.price == 90.00
    assert products_2.quantity == 15


def test_new_product():
    """тесты для метода new_product"""
    data = {
        "name": "Телефон",
        "description": "Смартфон",
        "price": 50000,
        "quantity": 10,
    }
    product = Product.new_product(data)

    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.price == 50000
    assert product.quantity == 10


def test_price_setter():
    """тесты для сеттера price"""
    product = Product("Ноутбук", "Игровой", 100000, 10)

    product.price = 800
    assert product.price == 800

    product.price = -100
    assert product.price == 800


def test_count_categories():
    """тест счетчик категорий"""
    Category.count_categories = 0
    init_count = Category.count_categories
    cat1 = Category("Электроника", "Описание", [])
    assert Category.count_categories == init_count + 1
    cat2 = Category("Одежда", "Описание", [])
    assert Category.count_categories == init_count + 2
    assert Category.count_categories == 2

def test_str_product(products_1, products_2):
    """тест вывод Название продукта, руб. Остаток: шт"""
    assert str(products_1) == "Планшет, 20.0 руб. Остаток: 2 шт."
    assert str(products_2) == "Смартфон, 90.0 руб. Остаток: 15 шт."

def test_str_category(categories):
    """информация по категории"""
    assert str(categories) == "Электроника, количество продуктов: 17 шт."

def test_add_products(products_1, products_2):
    assert (products_1.price * products_1.quantity) + (products_2.price * products_2.quantity) == 1390
