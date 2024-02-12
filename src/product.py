class Product:
    """
    Класс для представления товаров.
    """

    products_list = []  # Список существующих товаров

    def __init__(self, name, description, price: float, count: int):
        """
        Метод инициализации класса
        :param name: название товара
        :param description: описание товара
        :param price: цена на товар
        :param count: кол-во товара
        """
        self.name = name
        self.description = description
        self._price = price
        self.count = count
        Product.products_list.append(self)

    @classmethod
    def create_product(cls, product_dictionary):
        name = product_dictionary['name']
        description = product_dictionary['description']
        price = product_dictionary['price']
        count = product_dictionary['count']

        for product in cls.products_list:
            if name == product.name:
                product.count += count
                return product

        return cls(name, description, price, count)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: int):
        if value <= 0:
            print('Цена введена неккоректно')
        else:
            if value < self._price or value > self._price:
                answer = input('Вы уверены, что хотите изменить цену? (y/n) ')
                if answer == 'n':
                    print('Действие отменено')
                else:
                    self._price = value