from src.product import Product


class Grass(Product):
    def __init__(self, name, description, price: float, count: int, color, country, germination_period):
        super().__init__(name, description, price, count, color)
        self.country = country
        self.period = germination_period
