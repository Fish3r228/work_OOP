from abc import ABC, abstractmethod
from typing import Union


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов"""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other) -> Union[float, TypeError]:
        pass


class PrintInitMixin:
    """Миксин для вывода информации о создании объекта"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_name = self.__class__.__name__
        params = ", ".join([repr(arg) for arg in args] + [f"{k}={repr(v)}" for k, v in kwargs.items()])
        print(f"{class_name}({params})")


class Product(PrintInitMixin, BaseProduct):
    """Базовый класс продукта, реализующий абстрактные методы"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(name, description, price, quantity)

    def __str__(self):
        return f"{self.name}, {int(self.price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты Product")
        if type(self) != type(other):
            raise TypeError(f"Нельзя складывать {type(self).__name__} и {type(other).__name__}")
        return (self.price * self.quantity) + (other.price * other.quantity)

    def __repr__(self):
        return (f"{self.__class__.__name__}(name={repr(self.name)}, "
                f"description={repr(self.description)}, "
                f"price={repr(self.price)}, "
                f"quantity={repr(self.quantity)})")


class Smartphone(Product):
    """Класс смартфона, наследующий от Product"""

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

    def __repr__(self):
        base_repr = super().__repr__()[:-1]  # Убираем закрывающую скобку
        return (f"{base_repr}, "
                f"efficiency={repr(self.efficiency)}, "
                f"model={repr(self.model)}, "
                f"memory={repr(self.memory)}, "
                f"color={repr(self.color)})")


class LawnGrass(Product):
    """Класс газонной травы, наследующий от Product"""

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

    def __repr__(self):
        base_repr = super().__repr__()[:-1]  # Убираем закрывающую скобку
        return (f"{base_repr}, "
                f"country={repr(self.country)}, "
                f"germination_period={repr(self.germination_period)}, "
                f"color={repr(self.color)})")