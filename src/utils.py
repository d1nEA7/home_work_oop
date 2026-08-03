class Product:
    """Класс товары"""

    name: str  # Название товара (строка)
    description: str  # Описание (строка)
    price: float  # Цена (число с копейками, float)
    quantity: int  # Количество в наличии (целое число, штуки)

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс категории"""

    name: str  # Название категории (строка)
    description: str  # Описание (строка)
    products: list  # товары (список)

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)
        print(Category.product_count)


if __name__ == "__main__":
    # Создаём товары
    prod_1 = Product("Ноутбук", "Игровой", 100000, 10)
    prod_2 = Product("Мышь", "Игровая", 4000, 30)

    # Создаём категорию
    cat_1 = Category("Электроника", "Все для ПК", [prod_1, prod_2])
