import json


class Category:
    """
    Класс для представления категорий товаров.
    """
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.total_categories += 1
        Category.total_unique_products += len(set(products))


class Product:
    """
    Класс для представления товаров.
    """
    def __init__(self, name, description, price: float, count: int):
        self.name = name
        self.description = description
        self.price = price
        self.count = count


def load_data_from_json():
    """
    Загружает файл json, вытаскивает из него название, описание категорий, а так же товары, их название, описание,
    цену и количество
    :return: список categories со всеми категориями и товарами в этой категории
    """

    with open('products.json', 'r', encoding='UTF-8') as file:
        json_format = json.load(file)
    categories = []
    for category_data in json_format:
        category_name = category_data['name']
        category_description = category_data['description']
        products_data = category_data['products']
        products = []
        for product_data in products_data:
            product_name = product_data['name']
            product_description = product_data['description']
            product_price = product_data['price']
            product_count = product_data['quantity']
            product = Product(product_name, product_description, product_price, product_count)
            products.append(product)
        category = Category(category_name, category_description, products)
        categories.append(category)
    return categories


if __name__ == '__main__':
    categories = load_data_from_json()
    for category in categories:
        print(f'Категория: {category.name}, Описание: {category.description}')
        for product in category.products:
            print(f'Товар: {product.name}, Описание: {product.description}, Цена: {product.price}, '
                  f'Количество: {product.count}')
        print()
