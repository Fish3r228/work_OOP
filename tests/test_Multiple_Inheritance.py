import io
import sys
import unittest
from src.Multiple_Inheritance import Product, Smartphone, LawnGrass

class TestProductClasses(unittest.TestCase):
    def setUp(self):
        # Перехватываем stdout для проверки вывода PrintInitMixin
        self.held_output = io.StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        # Восстанавливаем stdout
        sys.stdout = sys.__stdout__

    def test_print_init_mixin_with_product(self):
        """Тестирование вывода информации при создании Product"""
        self.held_output.truncate(0)
        self.held_output.seek(0)

        _ = Product("Телефон", "Смартфон", 10000.0, 5)  # Используем _ для неиспользуемой переменной

        output = self.held_output.getvalue().strip()
        expected_output = "Product('Телефон', 'Смартфон', 10000.0, 5)"
        self.assertEqual(output, expected_output)

    def test_product_creation_and_str(self):
        """Тестирование создания Product и метода __str__"""
        product = Product("Ноутбук", "Игровой", 75000.0, 3)
        self.assertEqual(product.name, "Ноутбук")
        self.assertEqual(product.description, "Игровой")
        self.assertEqual(product.price, 75000.0)
        self.assertEqual(product.quantity, 3)
        self.assertEqual(str(product), "Ноутбук, 75000 руб. Остаток: 3 шт.")

    def test_smartphone_creation_and_str(self):
        """Тестирование создания Smartphone и метода __str__"""
        smartphone = Smartphone("iPhone", "Профессиональный", 100000.0, 5,
                                90.0, "15 Pro", 256, "Blue")
        self.assertEqual(smartphone.name, "iPhone")
        self.assertEqual(smartphone.efficiency, 90.0)
        self.assertEqual(smartphone.memory, 256)
        expected_str = ("iPhone, 100000 руб. Остаток: 5 шт.\n"
                        "Производительность: 90.0%, Модель: 15 Pro, Память: 256GB, Цвет: Blue")
        self.assertEqual(str(smartphone), expected_str)

    def test_lawn_grass_creation_and_str(self):
        """Тестирование создания LawnGrass и метода __str__"""
        grass = LawnGrass("Газон", "Премиум", 1200.0, 50,
                          "Германия", "21 день", "Изумрудный")
        self.assertEqual(grass.name, "Газон")
        self.assertEqual(grass.country, "Германия")
        self.assertEqual(grass.germination_period, "21 день")
        expected_str = ("Газон, 1200 руб. Остаток: 50 шт.\n"
                        "Страна: Германия, Срок прорастания: 21 день, Цвет: Изумрудный")
        self.assertEqual(str(grass), expected_str)

    def test_product_addition(self):
        """Тестирование сложения продуктов"""
        p1 = Product("Товар1", "Описание1", 1000.0, 2)
        p2 = Product("Товар2", "Описание2", 2000.0, 3)
        self.assertEqual(p1 + p2, 1000.0 * 2 + 2000.0 * 3)

    def test_product_repr(self):
        """Тестирование метода __repr__ для Product"""
        product = Product("Телевизор", "4K", 50000.0, 7)
        expected_repr = ("Product(name='Телевизор', description='4K', "
                         "price=50000.0, quantity=7)")
        self.assertEqual(repr(product), expected_repr)

    def test_smartphone_repr(self):
        """Тестирование метода __repr__ для Smartphone"""
        smartphone = Smartphone("Модель", "Описание", 30000.0, 4,
                                80.0, "Y", 64, "Red")
        expected_repr = ("Smartphone(name='Модель', description='Описание', "
                         "price=30000.0, quantity=4, efficiency=80.0, "
                         "model='Y', memory=64, color='Red')")
        self.assertEqual(repr(smartphone), expected_repr)


if __name__ == '__main__':
    unittest.main()