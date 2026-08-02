# from src.utils import prod_1, prod_2, Product


def test_category_init(categories):
    assert categories.name == "Электроника"
    assert categories.description == "Мобильная"
    assert len(categories.product) == 2
    assert categories.count_products == 2
    assert categories.count_categories == 1









