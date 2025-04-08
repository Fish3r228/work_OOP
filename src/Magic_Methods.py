class Product:
    """Класс, представляющий товар в магазине."""
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
    """Класс, представляющий категорию товаров."""
    def __init__(self, name: str, description: str, products_list: list):
        self.name = name
        self.description = description
        self.__products = products_list  # Changed parameter name to avoid shadowing

    @property
    def products(self):
        return "\n".join(map(str, self.__products))

    def __str__(self):
        return f"{self.name}, количество продуктов: {sum(p.quantity for p in self.__products)} шт."


if __name__ == '__main__':
    # Renamed to sample_products to avoid shadowing
    sample_products = [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    ]

    print("Информация о продуктах:")
    print(*sample_products, sep='\n')

    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        sample_products
    )

    print("\nИнформация о категории:")
    print(category)

    print("\nСписок продуктов в категории:")
    print(category.products)

    print("\nСуммарная стоимость товаров на складе:")
    print(f"Samsung + iPhone: {sample_products[0] + sample_products[1]} руб.")
    print(f"Samsung + Xiaomi: {sample_products[0] + sample_products[2]} руб.")
    print(f"iPhone + Xiaomi: {sample_products[1] + sample_products[2]} руб.")