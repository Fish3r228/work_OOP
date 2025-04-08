class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация продукта с проверкой типов"""
        if not isinstance(name, str):
            raise TypeError("Название продукта должно быть строкой")
        if not isinstance(description, str):
            raise TypeError("Описание продукта должно быть строкой")
        if not isinstance(price, (int, float)):
            raise TypeError("Цена должна быть числом")
        if not isinstance(quantity, int):
            raise TypeError("Количество должно быть целым числом")
        if price <= 0:
            raise ValueError("Цена должна быть положительной")
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")

        self.name = name
        self.description = description
        self.price = float(price)
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.description}, {self.price} руб., Остаток: {self.quantity} шт."


class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products: list):
        """Инициализация категории с проверкой типов"""
        if not isinstance(name, str):
            raise TypeError("Название категории должно быть строкой")
        if not isinstance(description, str):
            raise TypeError("Описание категории должно быть строкой")
        if not isinstance(products, list):
            raise TypeError("Продукты должны быть переданы в виде списка")

        for product in products:
            if not isinstance(product, Product):
                raise TypeError("Все элементы списка продуктов должны быть экземплярами Product")

        self.name = name
        self.description = description
        self.__products = products  # Приватный атрибут

        Category.total_categories += 1
        Category.total_products += len(products)

    @property
    def products(self):
        """Геттер для списка продуктов"""
        return self.__products

    def __str__(self):
        products_str = '\n'.join(str(product) for product in self.__products)
        return f"{self.name}, количество продуктов: {len(self.__products)} шт.\n{products_str}"


if __name__ == "__main__":
    # Создаем тестовые товары
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("iPhone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создаем первую категорию
    smartphones = Category(
        "Смартфоны",
        "Средство коммуникации и получения дополнительных функций",
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