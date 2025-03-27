class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Класс товара с полной инициализацией параметров
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    total_categories = 0  # Общее количество категорий
    total_products = 0  # Общее количество всех товаров во всех категориях

    def __init__(self, name: str, description: str, products: list[Product]):
        """
        Класс категории с автоматическим подсчетом статистики
        """
        self.name = name
        self.description = description
        self.products = products

        # Обновляем атрибуты класса
        Category.total_categories += 1
        Category.total_products += len(products)


if __name__ == "__main__":
    # Создаем тестовые товары
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("iPhone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создаем первую категорию
    smartphones = Category(
        "Смартфоны",
        "Средствa коммуникации и получения дополнительных функций",
        [product1, product2, product3]
    )

    # Создаем второй товар и категорию
    tv = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    tvs = Category(
        "Телевизоры",
        "Современные телевизоры для просмотра контента",
        [tv]
    )

    # Проверяем атрибуты класса
    print(f"Всего категорий: {Category.total_categories}")  # Ожидается 2
    print(f"Всего товаров: {Category.total_products}")  # Ожидается 4 (3 смартфона + 1 телевизор)

    # Проверяем атрибуты экземпляров
    print(f"Товаров в категории '{smartphones.name}': {len(smartphones.products)}")
    print(f"Товаров в категории '{tvs.name}': {len(tvs.products)}")