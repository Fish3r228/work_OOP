# Проект интернет-магазина: Категории и Товары

Проект реализует базовую функциональность управления товарами и категориями для интернет-магазина.

### Множественное наследование и миксины

Проект использует множественное наследование для реализации функциональности логирования создания объектов через миксин `PrintInitMixin`:

class PrintInitMixin:
    """Миксин для вывода информации о создании объекта"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Создан объект {self.__class__.__name__} с параметрами: {args}, {kwargs}")

class Product(PrintInitMixin, BaseProduct):
    """Класс продукта с функцией логирования создания"""
    ...


### Класс Product (базовый)
Базовый класс для всех товаров содержит:
- Основные атрибуты товара (name, description, price, quantity)
- Методы:
  - `__str__` - строковое представление товара
  - `__add__` - сложение товаров (по стоимости запасов)

### Класс Smartphone (наследник Product)
Добавляет специфичные для смартфонов атрибуты:
- `efficiency` - производительность (%)
- `model` - модель устройства
- `memory` - объем памяти (GB)
- `color` - цвет устройства

### Класс LawnGrass (наследник Product)
Добавляет специфичные для газонной травы атрибуты:
- `country` - страна-производитель
- `germination_period` - срок прорастания
- `color` - цвет травы

## Функционал проекта

### Основные возможности

1. **Класс Product**
   - Хранение базовой информации о товарах
   - Операции с товарами (сложение по стоимости запасов)
   - Строковое представление товара

2. **Классы-наследники**
   - Специализированные товары с дополнительными атрибутами
   - Полиморфное поведение (переопределенный `__str__`)
   - Контроль типов при операциях

3. **Класс Category**
   - Управление категориями товаров
   - Добавление товаров с проверкой типов
   - Статистика по товарам и категориям



## Требования к коду

- Полное соответствие PEP 8
- Покрытие тестами > 75%
- Полная документация классов и методов
- Проверка типов при добавлении товаров
- Наследование и полиморфизм должны использоваться корректно

## Установка и запуск

1. Клонировать репозиторий:
```bash
git clone https://github.com/ваш-логин/название-репозитория.git
cd название-репозитория