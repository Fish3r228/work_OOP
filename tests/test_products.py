import unittest
from src.products import Product, Category


class TestCategory(unittest.TestCase):
    def setUp(self):
        """Сбрасываем счетчики перед каждым тестом"""
        Category.total_categories = 0
        Category.total_products = 0
        self.product1 = Product("Товар1", "Описание1", 1000.0, 5)
        self.product2 = Product("Товар2", "Описание2", 2000.0, 10)

    def test_category_counters(self):
        """Тест счетчиков при создании категории"""
        # Создаем и сразу проверяем категорию
        category = Category("Тестовая", "Описание", [self.product1, self.product2])
        self.assertEqual(category.name, "Тестовая")
        self.assertEqual(category.description, "Описание")
        self.assertEqual(Category.total_categories, 1)
        self.assertEqual(Category.total_products, 2)

    def test_empty_category(self):
        """Тест пустой категори"""
        # Создаем и проверяем пустую категорию
        empty_category = Category("Пустая", "Нет товаров", [])
        self.assertEqual(empty_category.name, "Пустая")
        self.assertEqual(empty_category.description, "Нет товаров")
        self.assertEqual(Category.total_categories, 1)
        self.assertEqual(Category.total_products, 0)
        self.assertEqual(len(empty_category.products), 0)

    def test_category_with_single_product(self):
        """Тест категории с одним товаром"""
        # Создаем и проверяем категорию с одним товаром
        single_product = Product("Один", "Единственный", 500.0, 1)
        single_category = Category("Одиночная", "Один товар", [single_product])

        self.assertEqual(single_category.name, "Одиночная")
        self.assertEqual(single_category.description, "Один товар")
        self.assertEqual(Category.total_categories, 1)
        self.assertEqual(Category.total_products, 1)
        self.assertEqual(len(single_category.products), 1)
        self.assertEqual(single_category.products[0].name, "Один")


if __name__ == '__main__':
    unittest.main()