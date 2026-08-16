from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """"""

    @abstractmethod
    def __str__(self):
        pass


class LogMixin:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __repr__(self) -> str:
        return (
            f"Product({self.name}, {self.description}, {self.__price}, {self.quantity})"
        )


class Product(BaseProduct, LogMixin):
    """Класс товары"""

    name: str  # Название товара (строка)
    description: str  # Описание (строка)
    price: float  # Цена (число с копейками, float)
    quantity: int  # Количество в наличии (целое число, штуки)

    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, data: dict) -> Product:
        """метод класса создание нового продукта"""
        name = data.get("name")  # "Samsung Galaxy S23 Ultra"
        description = data.get("description")
        price = data.get("price")
        quantity = data.get("quantity")
        return Product(name, description, price, quantity)

    @property
    def price(self):
        """вызов приватного price"""
        return self.__price

    @price.setter
    def price(self, value):
        """возвращает значение цены если больше 0"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    def __str__(self):
        """строковое отображение: Название продукта, 80 руб. Остаток: 15 шт."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """сложение стоимости товаров"""
        if type(self) is not type(other):
            raise ValueError("Складывать можно только из одинаковых классов продукты.")
        else:
            price_prod_1 = self.price * self.quantity
            price_prod_2 = other.price * other.quantity
            return price_prod_1 + price_prod_2


class Category:
    """Класс категории"""

    name: str  # Название категории (строка)
    description: str  # Описание (строка)
    products: list  # товары (список)

    category_count = 0
    count_products = 0

    def __init__(self, name, description, products: list[Product]):

        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.count_products += len(products)

    @property
    def products(self):
        """возвращает приватные продукты"""
        return self.__products

    @property
    def product_count(self):
        """считает количество продуктов"""
        return len(self.__products)

    def add_product(self, product):
        """добавляет продукты"""
        if not isinstance(product, Product):
            raise ValueError(
                "Кроме смартфонов, травы газонной и других продуктов,"
                " в список нельзя добавлять ничего другого."
            )

        self.__products.append(product)
        Category.count_products += 1

    @property
    def list_products(self):
        """создает список продуктов с описанием"""
        return [str(product) for product in self.__products]

    def __str__(self) -> str:
        """количество продуктов в категории"""
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."


class Smartphone(Product):
    """класс Смартфоны"""

    efficiency: int  # производительность
    model: str  # модель
    memory: int  # объем встроенной памяти
    color: str  # цвет

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """класс Трава газонная"""

    country: str  # страна-производитель
    germination_period: str  # срок прорастания
    color: str  # цвет

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


if __name__ == "__main__":
    # Создаём товары
    prod_1 = Product("Ноутбук", "Игровой", 100000, 10)
    prod_2 = Product("Мышь", "Игровая", 4000, 30)

    # Создаём категорию
    cat_1 = Category("Электроника", "Все для ПК", [prod_1, prod_2])
