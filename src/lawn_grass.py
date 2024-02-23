from src.product import Product
from src.repr_mixin import ReprMixin


class Grass(Product, ReprMixin):
    def __init__(self, name, description, price: float, count: int, color, country, germination_period):
        super().__init__(name, description, price, count, color)
        self.country = country
        self.period = germination_period
