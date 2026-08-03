from src.utils import Category, Product


def test_category_init(categories):
    assert categories.name == "Электроника"
    assert categories.description == "Мобильная"
    assert len(categories.products) == 2
    assert categories.product_count == 2
    assert categories.category_count == 1

def test_product_init(products):
    assert products.name == "Планшет"
    assert products.description == "Игровой"
    assert products.price == 20.00
    assert products.quantity == 2