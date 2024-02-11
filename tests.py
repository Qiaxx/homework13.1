from dom_13 import Category, Product, load_data_from_json


def test_category_total_count():
    assert Category.total_categories == 0
    # category1 = Category("Category1", "Category Description", [])
    # category2 = Category("Category2", "Category Description", [])
    # assert Category.total_categories == 2
    # assert category1.name == 'Category1'
    # assert category2.name == 'Category2'
    # assert category1.description == 'Category Description'
    # assert category2.description == 'Category Description'
    # assert category1.products == []
    # assert category2.products == []


def test_category_total_unique_products():
    assert Category.total_unique_products == 0
    # product1 = Product("Product1", "Description1", 10.0, 5)
    # product2 = Product("Product2", "Description2", 15.0, 8)
    # products = [product1, product2]
    # category = Category("Category1", "Category Description", products)
    # assert Category.total_unique_products == 2
    # assert product1.name == 'Product1'
    # assert product2.name == 'Product2'
    # assert product1.description == 'Description1'
    # assert product2.description == 'Description2'
    # assert product1.price == 10.0
    # assert product2.price == 15.0
    # assert product1.count == 5
    # assert product2.count == 8