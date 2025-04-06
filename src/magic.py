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
            raise TypeError("Можно складывать только объекты класса Product")
        return (self.price * self.quantity) + (other.price * other.quantity)


class Category:
    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products

    @property
    def products(self):
        products_str = [str(product) for product in self.__products]
        return "\n".join(products_str)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


if __name__ == '__main__':
    # Создаем тестовые продукты
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Проверяем строковое представление продуктов
    print("Информация о продуктах:")
    print(product1)
    print(product2)
    print(product3)

    # Создаем категорию
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    # Проверяем строковое представление категории
    print("\nИнформация о категории:")
    print(category1)

    # Проверяем список продуктов в категории
    print("\nСписок продуктов в категории:")
    print(category1.products)

    # Проверяем сложение продуктов
    print("\nСуммарная стоимость товаров на складе:")
    print(f"Samsung + iPhone: {product1 + product2} руб.")
    print(f"Samsung + Xiaomi: {product1 + product3} руб.")
    print(f"iPhone + Xiaomi: {product2 + product3} руб.")