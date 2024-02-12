from src.category import Category


def test_category_total_count():
    assert Category.total_categories == 0
    category1 = Category("Category1", "Category Description", [])
    category2 = Category("Category2", "Category Description", [])
    assert Category.total_categories == 2
    assert category1.name == 'Category1'
    assert category2.name == 'Category2'
    assert category1.description == 'Category Description'
    assert category2.description == 'Category Description'
    assert category1.products == []
    assert category2.products == []
