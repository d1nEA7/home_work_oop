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


class quantity:
    name = str
    description = str
    product = str
    def __init__(self, name, discription, product):
        self.name = name
        self.discription = discription
        self.product = product