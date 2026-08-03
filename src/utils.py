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

    count_categories = 0
    count_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.count_categories += 1
        Category.count_products += len(products)
        print(Category.count_products)

    @property
    def products(self):
        return self.__products

    @property
    def product_count(self):
        return len(self.__products)

    def add_product(self, product ):
        self.__products.append(product)
        Category.count_products += 1


    @property
    def list_products(self):
        result = []
        for product in self.__products:
            result.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")

        return result







if __name__ == "__main__":
    # Создаём товары
    prod_1 = Product("Ноутбук", "Игровой", 100000, 10)
    prod_2 = Product("Мышь", "Игровая", 4000, 30)

    # Создаём категорию
    cat_1 = Category("Электроника", "Все для ПК", [prod_1, prod_2])
