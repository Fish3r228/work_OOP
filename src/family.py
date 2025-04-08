class Product:
    """Базовый класс для представления товара в магазине."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализирует экземпляр класса Product."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """Возвращает строковое представление товара."""
        return f"{self.name}, {int(self.price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> float:
        """
        Складывает стоимость товаров на складе."""
        if type(self) != type(other):
            raise TypeError(f"Нельзя складывать {type(self).__name__} и {type(other).__name__}")
        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    """Класс для представления смартфонов."""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        """
        Инициализирует экземпляр класса Smartphone."""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self) -> str:
        """Возвращает расширенное строковое представление смартфона."""
        return (f"{super().__str__()}\n"
                f"Производительность: {self.efficiency}%, "
                f"Модель: {self.model}, "
                f"Память: {self.memory}GB, "
                f"Цвет: {self.color}")


class LawnGrass(Product):
    """Класс для представления газонной травы."""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        """
        Инициализирует экземпляр класса LawnGrass."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self) -> str:
        """Возвращает расширенное строковое представление газонной травы."""
        return (f"{super().__str__()}\n"
                f"Страна: {self.country}, "
                f"Срок прорастания: {self.germination_period}, "
                f"Цвет: {self.color}")


class Category:
    """Класс для представления категории товаров."""

    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """
        Инициализирует экземпляр класса Category."""
        self.name = name
        self.description = description
        self.__products = []
        for product in products:
            self.add_product(product)

    @property
    def products(self) -> str:
        """Возвращает строку со списком всех товаров категории."""
        return "\n".join(str(product) for product in self.__products)

    def add_product(self, product: Product):
        """
        Добавляет товар в категорию."""
        if not isinstance(product, Product):
            raise TypeError(f"Ожидается Product, получен {type(product).__name__}")
        self.__products.append(product)
        Category.product_count += 1

    def __str__(self) -> str:
        """Возвращает строковое представление категории."""
        return f"{self.name}, количество продуктов: {sum(p.quantity for p in self.__products)} шт."


if __name__ == '__main__':
    # Создание тестовых данных
    smartphones = [
        Smartphone("Samsung Galaxy S23", "256GB, 200MP камера", 180000.0, 5, 95.5, "S23", 256, "Серый"),
        Smartphone("iPhone 15", "512GB", 210000.0, 8, 98.2, "15", 512, "Gray")
    ]

    grasses = [
        LawnGrass("Газонная трава", "Элитная трава", 500.0, 20, "Россия", "7 дней", "Зеленый"),
        LawnGrass("Газон Premium", "Премиум трава", 700.0, 15, "Германия", "5 дней", "Изумрудный")
    ]

    # Демонстрация работы
    tech_category = Category("Смартфоны", "Техника", smartphones)
    garden_category = Category("Газоны", "Садоводство", grasses)

    print("Категории:")
    print(tech_category)
    print(garden_category)

    print("\nТовары в категории 'Смартфоны':")
    print(tech_category.products)

    # Тестирование сложения
    try:
        print(f"\nСумма смартфонов: {smartphones[0] + smartphones[1]} руб.")
        print(f"Сумма газонов: {grasses[0] + grasses[1]} руб.")
    except TypeError as e:
        print(f"Ошибка: {e}")