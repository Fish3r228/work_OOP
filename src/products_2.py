class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут для цены
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data):
        """Класс-метод для создания продукта из словаря"""
        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )

    @property
    def price(self):
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, value):
        """Сеттер для цены с проверкой"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value


class Category:
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products  # Приватный атрибут

    @property
    def products(self):
        """Геттер для вывода списка товаров"""
        products_list = []
        for product in self.__products:
            products_list.append(
                f"{product.name}, {int(product.price)} руб. Остаток: {product.quantity} шт."
            )
        return "\n".join(products_list)

    def add_product(self, product):
        """Метод для добавления товара в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
        else:
            raise ValueError("Можно добавлять только объекты класса Product")

    @property
    def product_count(self):
        return len(self.__products)


if __name__ == "__main__":
    # Тестирование функционала
    test_product = Product("Test", "Test desc", 100, 10)

    print(f"Исходная цена: {test_product.price}")
    test_product.price = 150  # Корректное изменение
    print(f"Новая цена: {test_product.price}")

    test_product.price = -50  # Некорректное значение
    print(f"Цена после попытки установить отрицательное значение: {test_product.price}")

    test_product.price = 0  # Некорректное значение
    print(f"Цена после попытки установить нуль: {test_product.price}")