class Category:
    """
    Класс для представления категорий товаров.
    """
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description, products):
        """
        Метод инициализации класса
        :param name: название категории
        :param description: описание категории
        :param products: товары, которые входят в эту категорию
        """
        self.name = name
        self.description = description
        self.__products = []
        Category.total_categories += 1

    def add_product(self, product):
        self.__products.append(product)
        Category.total_unique_products += 1

    @property
    def products(self):
        info_list = []
        for product in self.__products:
            info_list.append(f'{product.name}, {product._price} руб. Остаток: {product.count}')
        return info_list
