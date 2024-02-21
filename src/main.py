from product import Product
from category import Category


def main():
    def create_product_dictionary() -> dict:
        """
        Функция создания нового товара
        :return: словарь с названием, описанием, ценой и кол-вом товара
        """

        new_product_data = {
            'name': input('Введите название товара: '),
            'description': input('Введите описание товара: '),
            'price': float(input('Введите цену на товар за единицу: ')),
            'count': int(input('Введите количество товара в наличии: ')),
            'color': input('Введите цвет товара')
        }

        return new_product_data

    category1 = Category("Category1", "Category Description", [])
    new_product = create_product_dictionary()
    new_product2 = create_product_dictionary()
    product1 = Product.create_product(new_product)
    product2 = Product.create_product(new_product2)


    category1.add_product(product1)
    category1.add_product(product2)
    

    print('\n'.join(category1.products))
    print(category1)


if __name__ == "__main__":
     main()

from src.product import Product
from src.category import Category

# def main():
#     prod_one_data = {
#         "name": "Samsung Galaxy C23 Ultra",
#         "description": "256GB, Серый цвет, 200MP камера",
#         "price": 180000.0,
#         "count": 5
#     }
#     prod_two_data = {
#             "name": "Iphone 15",
#             "description": "512GB, Gray space",
#             "price": 210000.0,
#             "count": 8
#     }
#     # на основе словарей создаем экземпляры
#     product_one_instance = Product.create_product(prod_one_data)
#     product_two_instance = Product.create_product(prod_two_data)
#     # проверим, что это именно экземпляры класса Product
#     print(type(product_one_instance))
#     # проверим что у продукта верно отрабатывает str
#     print(product_one_instance)
#     # соберем продукты в список и создадим категорию
#     all_products = [product_one_instance, product_two_instance]
#     category = Category('Смартфоны', 'Категория для смартфонов', all_products)
#     # проверим что у категории верно отрабатывает str
#     print(category)
#     # проверим, что продукты верно складываются.
#     print(product_one_instance + product_two_instance)
#     # ну и посмотрим на геттер products, он работает с экземпляроами, а не со словарями
#     print(category.products)
#
# if __name__ == "__main__":
#     main()