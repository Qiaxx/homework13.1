from src.product import Product


def test_category_total_unique_products():
    product1 = Product("Product1", "Description1", 10.0, 5)
    product2 = Product("Product2", "Description2", 15.0, 8)
    assert product1.name == 'Product1'
    assert product2.name == 'Product2'
    assert product1.description == 'Description1'
    assert product2.description == 'Description2'
    assert product1.price == 10.0
    assert product2.price == 15.0
    assert product1.count == 5
    assert product2.count == 8
    assert str(product1) == 'Product1, 10.0 руб. Остаток: 5 шт.'
    assert product1 + product2 == 170
