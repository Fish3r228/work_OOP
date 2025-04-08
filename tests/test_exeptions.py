import pytest
from src.exceptions import Category, Product


class TestProduct:
    """Тесты для класса Product."""

    def test_product_creation_success(self):
        """Тест успешного создания товара."""
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        assert product.name == "Телефон"
        assert product.description == "Смартфон"
        assert product.price == 50000.0
        assert product.quantity == 10

    def test_product_creation_zero_quantity(self):
        """Тест создания товара с нулевым количеством."""
        with pytest.raises(ValueError) as excinfo:
            Product("Бракованный", "Товар", 1000.0, 0)
        assert "Товар с нулевым количеством не может быть добавлен" in str(excinfo.value)

    def test_product_creation_negative_price(self):
        """Тест создания товара с отрицательной ценой."""
        product = Product("Товар", "С ценой ниже нуля", -100.0, 5)
        assert product.price == -100.0  # Проверяем, что отрицательная цена допустима


class TestCategory:
    """Тесты для класса Category."""

    @pytest.fixture
    def sample_products(self):
        """Фикстура с тестовыми товарами."""
        return [
            Product("Ноутбук", "Игровой", 150000.0, 3),
            Product("Смартфон", "Флагман", 120000.0, 5)
        ]

    def test_category_creation(self, sample_products):
        """Тест создания категории с товарами."""
        category = Category("Техника", "Электроника", sample_products)
        assert category.name == "Техника"
        assert category.description == "Электроника"
        assert len(category.products) == 2

    def test_average_price_with_products(self, sample_products):
        """Тест расчета средней цены для категории с товарами."""
        category = Category("Техника", "Электроника", sample_products)
        assert category.average_price() == pytest.approx(135000.0)

    def test_average_price_empty_category(self):
        """Тест расчета средней цены для пустой категории."""
        category = Category("Пустая", "Нет товаров", [])
        assert category.average_price() == 0

    def test_average_price_single_product(self):
        """Тест расчета средней цены для категории с одним товаром."""
        product = Product("Планшет", "10 дюймов", 80000.0, 2)
        category = Category("Гаджеты", "Планшеты", [product])
        assert category.average_price() == 80000.0


class TestIntegration:
    """Интеграционные тесты для совместной работы классов."""

    def test_product_in_category(self):
        """Тест корректности работы товаров внутри категории."""
        product = Product("Наушники", "Беспроводные", 15000.0, 7)
        category = Category("Аксессуары", "Для техники", [product])

        assert category.products[0].name == "Наушники"
        assert category.products[0].price == 15000.0
        assert category.average_price() == 15000.0


if __name__ == "__main__":
    pytest.main(["-v", "--tb=line"])