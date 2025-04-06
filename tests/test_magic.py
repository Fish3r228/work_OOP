import pytest
from src.magic import Category, Product


class TestProduct:
    def test_product_creation(self):
        """Тест создания продукта и его атрибутов"""
        product = Product("Телевизор", "4K OLED", 100000, 3)
        assert product.name == "Телевизор"
        assert product.description == "4K OLED"
        assert product.price == 100000
        assert product.quantity == 3

    def test_product_str(self):
        """Тест строкового представления продукта"""
        product = Product("Наушники", "Bluetooth", 5000, 10)
        assert str(product) == "Наушники, 5000 руб. Остаток: 10 шт."

    def test_product_addition(self):
        """Тест сложения двух продуктов"""
        p1 = Product("Товар1", "", 100, 10)
        p2 = Product("Товар2", "", 200, 2)
        assert p1 + p2 == 1400  # 100*10 + 200*2 = 1400

    def test_product_addition_with_wrong_type(self):
        """Тест попытки сложения продукта с неправильным типом"""
        p = Product("Товар", "", 100, 1)
        with pytest.raises(TypeError):
            p + "не продукт"


class TestCategory:
    @pytest.fixture
    def sample_products(self):
        """Фикстура с тестовыми продуктами"""
        return [
            Product("Товар1", "", 100, 5),
            Product("Товар2", "", 200, 3),
            Product("Товар3", "", 300, 2),
        ]

    def test_category_creation(self, sample_products):
        """Тест создания категории"""
        category = Category("Электроника", "Техника", sample_products)
        assert category.name == "Электроника"
        assert category.description == "Техника"
        assert len(category.products.split("\n")) == 3

    def test_category_str(self, sample_products):
        """Тест строкового представления категории"""
        category = Category("Электроника", "", sample_products)
        assert str(category) == "Электроника, количество продуктов: 10 шт."

    def test_category_products_property(self, sample_products):
        """Тест свойства products категории"""
        category = Category("Категория", "", sample_products)
        products_str = category.products
        assert "Товар1, 100 руб. Остаток: 5 шт." in products_str
        assert "Товар2, 200 руб. Остаток: 3 шт." in products_str
        assert "Товар3, 300 руб. Остаток: 2 шт." in products_str


def test_integration():
    """Интеграционный тест работы классов вместе"""
    # Создаем продукты
    p1 = Product("Мышь", "Беспроводная", 2500, 4)
    p2 = Product("Клавиатура", "Механическая", 5000, 2)

    # Проверяем сложение
    assert p1 + p2 == 2500 * 4 + 5000 * 2

    # Создаем категорию
    category = Category("Комплектующие", "Для ПК", [p1, p2])

    # Проверяем категорию
    assert str(category) == "Комплектующие, количество продуктов: 6 шт."
    assert "Мышь, 2500 руб. Остаток: 4 шт." in category.products
    assert "Клавиатура, 5000 руб. Остаток: 2 шт." in category.products
