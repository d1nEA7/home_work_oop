def test_category_init(categories):
    """тесты для инициализации категорий"""
    assert categories.name == "Электроника"
    assert categories.description == "Мобильная"
    assert len(categories.products) == 2
    assert categories.product_count == 2
    assert categories.category_count == 1


def test_product_init(products):
    """тесты для инициализации продуктов_1"""
    assert products.name == "Планшет"
    assert products.description == "Игровой"
    assert products.price == 20.00
    assert products.quantity == 2


def test_product_init_2(products_2):
    """тесты для инициализации продуктов_2"""
    assert products_2.name == "Смартфон"
    assert products_2.description == "Игровой"
    assert products_2.price == 90.00
    assert products_2.quantity == 15
