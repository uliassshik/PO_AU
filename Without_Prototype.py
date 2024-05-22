class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"Продукт: {self.name}, Описание: {self.description}, Цена: {self.price}"


if __name__ == "__main__":
    # Создаем исходный продукт
    original_product = Product("iPhone 13", "Latest iPhone", 999.99)

    # Создаем клоны исходного продукта вручную
    clone1 = Product("iPhone 14", "Latest iPhone with new features", 1099.99)
    clone2 = Product("iPhone 15", "Latest iPhone with even more features", 1199.99)

    # Выводим клоны
    print(clone1)
    print(clone2)