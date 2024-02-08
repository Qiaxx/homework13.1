class Category:

    numbers_of_category = 0
    numbers_of_product = 0

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.product = product


class Product:

    def __init__(self, name, description, price: float, count: int):
        self.name = name
        self.description = description
        self.price = price
        self.count = count
