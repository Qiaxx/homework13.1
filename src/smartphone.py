from src.product import Product
from src.repr_mixin import ReprMixin


class Smartphone(Product, ReprMixin):
    def __init__(self, name, description, price: float, count: int, color, performance, model, memory_capacity):
        super().__init__(name, description, price, count, color)
        self.performance = performance
        self.model = model
        self.capacity = memory_capacity


