import unittest

from src.products import Category, Product


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.valid_product = Product("Телефон", "Смартфон", 50000.0, 10)

    def test_product_initialization(self):
        self.assertEqual(self.valid_product.name, "Телефон")
        self.assertEqual(self.valid_product.description, "Смартфон")
        self.assertEqual(self.valid_product.price, 50000.0)
        self.assertEqual(self.valid_product.quantity, 10)

    def test_product_price_validation(self):
        with self.assertRaises(TypeError):
            Product("Телефон", "Смартфон", "не число", 10)

        with self.assertRaises(ValueError):
            Product("Телефон", "Смартфон", -100.0, 10)

    def test_product_quantity_validation(self):
        with self.assertRaises(TypeError):
            Product("Телефон", "Смартфон", 50000.0, "не число")

        with self.assertRaises(ValueError):
            Product("Телефон", "Смартфон", 50000.0, -5)

    def test_product_name_validation(self):
        with self.assertRaises(TypeError):
            Product(12345, "Смартфон", 50000.0, 10)

    def test_product_description_validation(self):
        with self.assertRaises(TypeError):
            Product("Телефон", 12345, 50000.0, 10)

    def test_product_str_representation(self):
        expected_str = "Телефон, Смартфон, 50000.0 руб., Остаток: 10 шт."
        self.assertEqual(str(self.valid_product), expected_str)


class TestCategory(unittest.TestCase):
    def setUp(self):
        Category.total_categories = 0
        Category.total_products = 0
        self.product1 = Product("Товар1", "Описание1", 1000.0, 5)
        self.product2 = Product("Товар2", "Описание2", 2000.0, 10)

    def test_category_initialization(self):
        category = Category("Тестовая", "Описание", [self.product1])
        self.assertEqual(category.name, "Тестовая")
        self.assertEqual(category.description, "Описание")
        self.assertEqual(len(category.products), 1)
        self.assertEqual(category.products[0].name, "Товар1")

    def test_category_name_validation(self):
        with self.assertRaises(TypeError):
            Category(12345, "Описание", [self.product1])

    def test_category_description_validation(self):
        with self.assertRaises(TypeError):
            Category("Тестовая", 12345, [self.product1])

    def test_category_products_validation(self):
        with self.assertRaises(TypeError):
            Category("Тестовая", "Описание", "не список")

        with self.assertRaises(TypeError):
            Category("Тестовая", "Описание", [12345])

    def test_category_str_representation(self):
        category = Category("Тестовая", "Описание", [self.product1])
        expected_str = (
            "Тестовая, количество продуктов: 1 шт.\n"
            "Товар1, Описание1, 1000.0 руб., Остаток: 5 шт."
        )
        self.assertEqual(str(category), expected_str)

    def test_category_products_protection(self):
        category = Category("Защита", "Тест", [self.product1])
        with self.assertRaises(AttributeError):
            category.products = [self.product2]

        # Проверяем, что список остался неизменным
        self.assertEqual(len(category.products), 1)
        self.assertEqual(category.products[0].name, "Товар1")


if __name__ == "__main__":
    unittest.main()
