from src.utils import prod_1, prod_2


def test_category_init(categories):
    assert categories.name == "Электроника"
    assert categories.description == "Мобильная"
    assert len(categories.product) == 2