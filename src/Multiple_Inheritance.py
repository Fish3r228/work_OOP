from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов.

    Определяет обязательные методы, которые должны быть реализованы в дочерних классах.
    """

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация продукта.

        Args:
            name (str): Название продукта."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self) -> str:
        """Возвращает строковое представление продукта."""
        pass

    @abstractmethod
    def __add__(self, other):
        """Определяет логику сложения продуктов."""
        pass


class PrintInitMixin:
    """Миксин, выводящий информацию о создании объекта.

    При создании экземпляра класса выводит его название и переданные аргументы.
    """

    def __init__(self, *args, **kwargs):
        """Инициализация миксина."""
        super().__init__(*args, **kwargs)
        print(f"{self.__class__.__name__}({', '.join(map(repr, args))})")


class Product(PrintInitMixin, BaseProduct):
    """Базовый класс продукта.

    Реализует абстрактные методы BaseProduct и добавляет логику вывода и сложения товаров.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация продукта."""
        super().__init__(name, description, price, quantity)

    def __str__(self):
        """Возвращает строковое представление продукта."""
        return f"{self.name}, {int(self.price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Складывает два продукта одного типа."""
        if not isinstance(other, type(self)):
            raise TypeError(f"Нельзя складывать {type(self).__name__} и {type(other).__name__}")
        return (self.price * self.quantity) + (other.price * other.quantity)

    def __repr__(self):
        """Возвращает строковое представление для отладки."""
        return (f"{self.__class__.__name__}("
                f"name={repr(self.name)}, "
                f"description={repr(self.description)}, "
                f"price={repr(self.price)}, "
                f"quantity={repr(self.quantity)})")


class Smartphone(Product):
    """Класс, представляющий смартфон.

    Наследует функциональность Product и добавляет специфичные для смартфона атрибуты.
    """

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """Инициализация смартфона."""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        """Возвращает строковое представление смартфона."""
        return (f"{super().__str__()}\n"
                f"Производительность: {self.efficiency}%, "
                f"Модель: {self.model}, "
                f"Память: {self.memory}GB, "
                f"Цвет: {self.color}")

    def __repr__(self):
        """Возвращает строковое представление для отладки."""
        return (f"{super().__repr__()[:-1]}, "
                f"efficiency={repr(self.efficiency)}, "
                f"model={repr(self.model)}, "
                f"memory={repr(self.memory)}, "
                f"color={repr(self.color)})")


class LawnGrass(Product):
    """Класс, представляющий газонную траву.

    Наследует функциональность Product и добавляет специфичные атрибуты.
    """

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """Инициализация газонной травы."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        """Возвращает строковое представление газонной травы."""
        return (f"{super().__str__()}\n"
                f"Страна: {self.country}, "
                f"Срок прорастания: {self.germination_period}, "
                f"Цвет: {self.color}")

    def __repr__(self):
        """Возвращает строковое представление для отладки."""
        return (f"{super().__repr__()[:-1]}, "
                f"country={repr(self.country)}, "
                f"germination_period={repr(self.germination_period)}, "
                f"color={repr(self.color)})")