class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {int(self.price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты Product")
        if type(self) != type(other):
            raise TypeError(f"Нельзя складывать {type(self).__name__} и {type(other).__name__}")
        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        base_str = super().__str__()
        return (f"{base_str}\n"
                f"Производительность: {self.efficiency}%, "
                f"Модель: {self.model}, "
                f"Память: {self.memory}GB, "
                f"Цвет: {self.color}")


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        base_str = super().__str__()
        return (f"{base_str}\n"
                f"Страна: {self.country}, "
                f"Срок прорастания: {self.germination_period}, "
                f"Цвет: {self.color}")


class Category:
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = []
        for product in products:
            self.add_product(product)  # Используем наш защищенный метод при инициализации

    @property
    def products(self):
        return "\n".join(str(product) for product in self.__products)

    def add_product(self, product):
        """Добавляет продукт в категорию с проверкой типа"""
        if not isinstance(product, Product):
            raise TypeError(f"Ожидается Product или его подкласс, получен {type(product).__name__}")

        # Дополнительная проверка через issubclass
        if not issubclass(type(product), Product):
            raise TypeError(f"Класс {type(product).__name__} не является подклассом Product")

        self.__products.append(product)
        Category.product_count += 1

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


if __name__ == '__main__':
    # Создаем тестовые продукты
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                             180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")
    smartphone2 = Smartphone("iPhone 15", "512GB", 210000.0, 8, 98.2, "15", 512, "Gray")
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона",
                       500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава Premium", "Премиум трава",
                       700.0, 15, "Германия", "5 дней", "Изумрудный")

    # Тест сложения одинаковых типов
    try:
        print(f"Сумма смартфонов: {smartphone1 + smartphone2} руб.")  # Должно работать
        print(f"Сумма газонных трав: {grass1 + grass2} руб.")  # Должно работать
    except TypeError as e:
        print(f"Ошибка: {e}")

    # Тест сложения разных типов
    try:
        invalid_sum = smartphone1 + grass1  # Должно вызвать TypeError
        print("Сумма смартфона и травы:", invalid_sum)
    except TypeError as e:
        print(f"Ожидаемая ошибка: {e}")  # Должно сработать

    # Создаем категории
    tech_category = Category("Смартфоны", "Техника", [smartphone1, smartphone2])
    garden_category = Category("Газоны", "Садоводство", [grass1, grass2])

    print("\nКатегории:")
    print(tech_category)
    print(garden_category)

    print("\nПродукты в категории 'Смартфоны':")
    print(tech_category.products)

if __name__ == '__main__':
    # Создаем тестовые продукты
    smartphone = Smartphone("iPhone", "Cool", 1000, 5, 90, "13", 128, "Black")
    grass = LawnGrass("Grass", "Green", 50, 10, "Russia", "7 days", "Green")

    # Создаем категорию
    tech_category = Category("Tech", "Gadgets", [smartphone])

    # Пытаемся добавить правильные продукты
    tech_category.add_product(smartphone)  # OK
    garden_category = Category("Garden", "Plants", [grass])  # OK

    # Пытаемся добавить неправильные объекты
    try:
        tech_category.add_product("Not a product")  # Должно вызвать TypeError
    except TypeError as e:
        print(f"Ожидаемая ошибка: {e}")  # Сработает

    try:
        tech_category.add_product(123)  # Должно вызвать TypeError
    except TypeError as e:
        print(f"Ожидаемая ошибка: {e}")  # Сработает

    # Проверяем содержимое категории
    print("\nПродукты в категории 'Tech':")
    print(tech_category.products)