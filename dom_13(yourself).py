import json


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

    @property
    def get_name_product(self):
        name_product = []
        for product in self.__products:
            name_product.append(product.name)
        return name_product

    @property
    def get_count_product(self):
        count_product = []
        for product in self.__products:
            count_product.append(product.count)
        return count_product


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


def create_product_dictionary():
    """
    Функция создания нового товара
    :return: словарь с названием, описанием, ценой и кол-вом товара
    """

    new_product_data = {
        'name': input('Введите название товара: '),
        'description': input('Введите описание товара: '),
        'price': float(input('Введите цену на товар за единицу: ')),
        'count': int(input('Введите количество товара в наличии: '))
    }

    return new_product_data


# def load_data_from_json(data_json):
#     """
#     Загружает файл json, вытаскивает из него название, описание категорий, а так же товары, их название, описание,
#     цену и количество
#     :return: список categories со всеми категориями и товарами в этой категории
#     """
#
#     with open(data_json, 'r', encoding='UTF-8') as file:
#         json_format = json.load(file)
#     categories = []
#     for category_data in json_format:
#         category_name = category_data['name']
#         category_description = category_data['description']
#         products_data = category_data['products']
#         products = []
#         for product_data in products_data:
#             product_name = product_data['name']
#             product_description = product_data['description']
#             product_price = product_data['price']
#             product_count = product_data['quantity']
#             product = Product(product_name, product_description, product_price, product_count)
#             products.append(product)
#         category = Category(category_name, category_description, products_data)
#         categories.append(category)
#     return categories


# if __name__ == '__main__':
#     categories = load_data_from_json('products.json')
#     for category in categories:
#         print(f'Категория: {category.name}, Описание: {category.description}')
#         for product in category.get_products():
#             print(f'Товар: {product.name}, Описание: {product.description}, Цена: {product.price}, '
#                   f'Количество: {product.count}')
#         print()

# код для проверки
category1 = Category("Category1", "Category Description", [])
product1 = Product("Product1", "Description1", 10.0, 5)
product2 = Product("Product2", "Description2", 15.0, 8)

category1.add_product(product1)
category1.add_product(product2)

print('\n'.join(category1.products))

new_product = create_product_dictionary()
product3 = Product.create_product(new_product)

category1.add_product(product3)

print('\n'.join(category1.products))

# category2 = Category("Category2", "Category Description", [])
# new_product = create_product_dictionary()
# new_product2= create_product_dictionary()
#
# product3 = Product.create_product(new_product)
# product4 = Product.create_product(new_product2)
#
# category2.add_product(product3)
# category2.add_product(product4)
#
# print('\n'.join(category2.products))
#
# product3.price = int(input('Введите новую цену: '))
#
# print('\n'.join(category2.products))