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
            'count': int(input('Введите количество товара в наличии: '))
        }

        return new_product_data

    def return_dict(product_object):
        """
        Функция преобразовывает экземпляр класса в словарь, где ключи - это поля класса, а значения - значения ключей
        :param product_object: экземпляр класса
        :return: словарь, где ключи - это поля класса, а значения - значения ключей
        """
        product_dict = vars(product_object)
        return product_dict

    category1 = Category("Category1", "Category Description", [])
    new_product = create_product_dictionary()
    new_product2 = create_product_dictionary()
    product1 = Product.create_product(new_product)
    product1_dict = return_dict(product1)
    product2 = Product.create_product(new_product2)
    product2_dict = return_dict(product2)

    category1.add_product(product1_dict)
    category1.add_product(product2_dict)

    print('\n'.join(category1.products))
    print(category1)


if __name__ == "__main__":
    main()
