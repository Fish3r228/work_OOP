import pytest
from src.inheritance import Product, Smartphone, LawnGrass, Category


class TestProductAddition:
    """Тесты для проверки сложения продуктов"""

    def test_add_smartphones(self):
        """Сложение смартфонов должно работать"""
        s1 = Smartphone("S1", "", 1000, 2, 90, "M1", 64, "Black")
        s2 = Smartphone("S2", "", 2000, 3, 95, "M2", 128, "White")
        assert s1 + s2 == 1000 * 2 + 2000 * 3

    def test_add_lawn_grass(self):
        """Сложение газонных трав должно работать"""
        g1 = LawnGrass("G1", "", 500, 4, "RU", "7d", "Green")
        g2 = LawnGrass("G2", "", 700, 5, "US", "5d", "Dark Green")
        assert g1 + g2 == 500 * 4 + 700 * 5

    def test_add_different_types(self):
        """Сложение разных типов должно вызывать ошибку"""
        s = Smartphone("S", "", 1000, 1, 90, "M", 64, "Black")
        g = LawnGrass("G", "", 500, 1, "RU", "7d", "Green")
        with pytest.raises(TypeError):
            s + g

    def test_add_non_product(self):
        """Сложение с не-продуктом должно вызывать ошибку"""
        s = Smartphone("S", "", 1000, 1, 90, "M", 64, "Black")
        with pytest.raises(TypeError):
            s + "not a product"


class TestCategoryAddProduct:
    """Тесты для проверки добавления продуктов в категорию"""

    @pytest.fixture
    def sample_products(self):
        """Фикстура с тестовыми продуктами"""
        return [
            Smartphone("S1", "", 1000, 2, 90, "M1", 64, "Black"),
            LawnGrass("G1", "", 500, 4, "RU", "7d", "Green")
        ]

    def test_add_smartphone(self):
        """Добавление смартфона должно работать"""
        cat = Category("Tech", "Gadgets", [])
        s = Smartphone("S", "", 1000, 1, 90, "M", 64, "Black")
        cat.add_product(s)
        assert "S, 1000 руб." in cat.products

    def test_add_lawn_grass(self):
        """Добавление газонной травы должно работать"""
        cat = Category("Garden", "Plants", [])
        g = LawnGrass("G", "", 500, 1, "RU", "7d", "Green")
        cat.add_product(g)
        assert "G, 500 руб." in cat.products

    def test_add_non_product(self):
        """Попытка добавить не-продукт должна вызывать ошибку"""
        cat = Category("Test", "Test", [])
        with pytest.raises(TypeError):
            cat.add_product("not a product")
        with pytest.raises(TypeError):
            cat.add_product(123)

    def test_add_invalid_type(self):
        """Попытка добавить объект не из иерархии Product должна вызывать ошибку"""
        cat = Category("Test", "Test", [])

        class FakeProduct:
            pass

        fake = FakeProduct()
        with pytest.raises(TypeError):
            cat.add_product(fake)

    def test_product_count_increases(self):
        """Счетчик продуктов должен увеличиваться при добавлении"""
        initial_count = Category.product_count
        cat = Category("Test", "Test", [])
        s = Smartphone("S", "", 1000, 1, 90, "M", 64, "Black")
        cat.add_product(s)
        assert Category.product_count == initial_count + 1


class TestPreviousFunctionality:
    """Тесты для проверки сохранения предыдущей функциональности"""

    def test_product_str(self):
        """Проверка строкового представления продукта"""
        p = Product("Test", "Desc", 100, 5)
        assert "Test, 100 руб. Остаток: 5 шт." in str(p)

    def test_category_str(self):
        """Проверка строкового представления категории"""
        p = Product("Test", "Desc", 100, 5)
        cat = Category("TestCat", "Desc", [p])
        assert "TestCat, количество продуктов: 5 шт." in str(cat)

    def test_products_property(self):
        """Проверка свойства products"""
        p1 = Product("P1", "Desc", 100, 5)
        p2 = Product("P2", "Desc", 200, 3)
        cat = Category("Test", "Test", [p1, p2])
        assert "P1, 100 руб." in cat.products
        assert "P2, 200 руб." in cat.products