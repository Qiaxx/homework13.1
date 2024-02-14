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
    category1.add_product({
            'name': 'Ya govno',
            'description': 'dadada',
            'price': 17.8,
            'count': 10
        })
    assert str(category1) == 'Category1, количество продуктов: 10 шт.'