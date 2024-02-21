from src.product import Product

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
        self.__products = set(products)
        Category.total_categories += 1

    def add_product(self, product):
        """
        Метод добавления новых товаров
        :param product: товар
        """
        if isinstance(product, Product):
            self.__products.add(product)
            Category.total_unique_products += 1

    @property
    def products(self):
        """
        Метод вывода информации о товаре в категории
        :return: список из вывода информации о товаре
        """
        info_list = []
        for product in self.__products:
            info_list.append(f'{product.name}, {product._price} руб. Остаток: {product.count}')
        return info_list

    def __str__(self):
        """
        Метод вывода информации о категории
        :return: информация о категории
        """
        return f'{self.name}, количество продуктов: {len(self)} шт.'

    def __len__(self):
        """
        Метод вычисления общего количества товара в категории
        :return: переменную с общим количеством товара категории
        """
        count_all_products = 0
        for product in self.__products:
            count_all_products += product.count
        return count_all_products