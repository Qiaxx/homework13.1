from abc import ABC, abstractmethod


class Abstract(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def create_product(self, product_dictionary):
        pass
