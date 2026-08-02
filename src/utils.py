class Product:
    name = str
    description = str
    price = float
    quantity = int
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    name = str
    description = str
    product = list
    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.product = product