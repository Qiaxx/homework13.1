from dom_13 import Category, Product


def test_category_total_count():
    assert Category.total_categories == 0
    category1 = Category("Category1", "Category Description", [])
    category2 = Category("Category2", "Category Description", [])
    assert Category.total_categories == 2


def test_category_total_unique_products():
    assert Category.total_unique_products == 0
    product1 = Product("Product1", "Description1", 10.0, 5)
    product2 = Product("Product2", "Description2", 15.0, 8)
    products = [product1, product2]
    category = Category("Category1", "Category Description", products)
    assert Category.total_unique_products == 2
