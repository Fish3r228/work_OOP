class Product:
    """Класс, представляющий товар в магазине."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализирует новый экземпляр класса Product."""
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс, представляющий категорию товаров в магазине."""

    def __init__(self, name: str, description: str, products: list):
        """Инициализирует новый экземпляр класса Category."""
        self.name = name
        self.description = description
        self.products = products

    def average_price(self) -> float:
        """Вычисляет среднюю цену товаров в категории."""
        try:
            total = sum(product.price for product in self.products)
            return total / len(self.products)
        except ZeroDivisionError:
            return 0
        except Exception as exc:
            print(f"Произошла ошибка при расчете средней цены: {exc}")
            return 0


if __name__ == '__main__':
    """Основной блок выполнения программы.

    Демонстрирует:
    1. Создание товаров
    2. Создание категорий
    3. Расчет средней цены товаров в категории
    4. Обработку ошибок при создании товаров
    """
    try:
        # Создаем тестовые товары
        product1 = Product("Ноутбук", "Игровой", 150000.0, 3)
        product2 = Product("Смартфон", "Флагман", 120000.0, 5)

        # Создаем категорию с товарами
        tech_category = Category("Техника", "Электроника", [product1, product2])
        print(f"Средняя цена в категории '{tech_category.name}': {tech_category.average_price()}")

        # Создаем пустую категорию
        empty_category = Category("Пустая", "Нет товаров", [])
        print(f"Средняя цена в пустой категории: {empty_category.average_price()}")

    except ValueError as err:
        print(f"Ошибка создания товара: {err}")