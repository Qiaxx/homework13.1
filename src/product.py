from src.abstract_product import Abstract
from src.repr_mixin import ReprMixin


class Product(Abstract, ReprMixin):
    """
    Класс для представления товаров.
    """

    products_list = []  # Список существующих товаров

    def __init__(self, name, description, price: float, count: int, color):
        """
        Метод инициализации класса
        :param name: название товара
        :param description: описание товара
        :param price: цена на товар
        :param count: кол-во товара
        """
        self.name = name
        self.description = description
        self.color = color
        self._price = price
        self.count = count
        Product.products_list.append(self)

    @classmethod
    def create_product(cls, product_dictionary):
        """
        Метод форматирования словаря в экземпляр класса Product
        :param product_dictionary: словарь с данными о товаре, где 'name' - название, 'description' - описание,
        'price' - цена, 'count' - количество штук
        :return: экземпляр товара
        """
        name = product_dictionary['name']
        description = product_dictionary['description']
        price = product_dictionary['price']
        count = product_dictionary['count']
        color = product_dictionary['color']

        for product in cls.products_list:
            if name == product.name:
                product.count += count
                return product

        return cls(name, description, price, count, color)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: int):
        if value <= 0:
            print('Цена введена неккоректно')
        else:
            if self._price > value:
                self._price = value
            elif value < self._price:
                answer = input('Вы уверены, что хотите изменить цену? (y/n) ')
                if answer == 'n':
                    print('Действие отменено')
                else:
                    self._price = value

    def __str__(self):
        """
        Метод вывода информации о товаре
        :return: вывод информации о товаре
        """
        return f"{self.name}, {self._price} руб. Остаток: {self.count} шт."

    def __add__(self, other):
        """
        Метод сложения общей стоимости товаров с учетом их количества
        :return: общая сумма всех товаров
        """
        if type(self) == type(other):
            sum_product1 = self.count * self._price
            sum_product2 = other._price * other.count
            return sum_product1 + sum_product2

        raise TypeError('Можно складывать товары только из одинаковых классов продуктов')

