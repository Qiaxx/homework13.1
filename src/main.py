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

    category1 = Category("Category1", "Category Description", [])
    new_product = create_product_dictionary()
    product1 = Product.create_product(new_product)

    category1.add_product(product1)

    print('\n'.join(category1.products))


if __name__ == "__main__":
    main()
