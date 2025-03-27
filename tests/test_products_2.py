import logging
import unittest


class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут для цены
        self.quantity = quantity
        self.logger = logging.getLogger(__name__)

    @classmethod
    def new_product(cls, product_data):
        """Класс-метод для создания продукта из словаря"""
        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )

    @property
    def price(self):
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, value):
        """Сеттер для цены с проверкой"""
        if value <= 0:
            self.logger.warning("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value


class TestProduct(unittest.TestCase):
    def setUp(self):
        """Подготовка тестовых данных"""
        self.product_data = {
            "name": "Test Product",
            "description": "Test Description",
            "price": 1000.0,
            "quantity": 10
        }
        self.product = Product.new_product(self.product_data)
        self.logger = logging.getLogger(__name__)

    def test_product_creation(self):
        """Тест создания продукта"""
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.description, "Test Description")
        self.assertEqual(self.product.price, 1000.0)
        self.assertEqual(self.product.quantity, 10)

    def test_price_setter_valid(self):
        """Тест установки корректной цены"""
        self.product.price = 1500.0
        self.assertEqual(self.product.price, 1500.0)

    def test_price_setter_invalid(self):
        """Тест установки некорректной цены"""
        with self.assertLogs(logger=__name__, level='WARNING') as cm:
            self.product.price = -100
        self.assertIn("Цена не должна быть нулевая или отрицательная", cm.output[0])
        self.assertEqual(self.product.price, 1000.0)  # Цена не должна измениться

        with self.assertLogs(logger=__name__, level='WARNING') as cm:
            self.product.price = 0
        self.assertIn("Цена не должна быть нулевая или отрицательная", cm.output[0])
        self.assertEqual(self.product.price, 1000.0)  # Цена не должна измениться

    def test_new_product_classmethod(self):
        """Тест класс-метода new_product"""
        new_data = {
            "name": "New Product",
            "description": "New Description",
            "price": 2000.0,
            "quantity": 5
        }
        new_product = Product.new_product(new_data)
        self.assertIsInstance(new_product, Product)
        self.assertEqual(new_product.name, "New Product")


if __name__ == "__main__":
    unittest.main()