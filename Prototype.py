# Интерфейс для клонирования объектов
class Cloneable:
    def clone(self):
        pass

# Класс продукта, реализующий интерфейс Cloneable
class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
    
    def __str__(self):
        return f"Продукт: {self.name}, Описание: {self.description}, Цена: {self.price}"

    def clone(self):
        return Product(self.name, self.description, self.price)

# Прототип продукта
class ProductPrototype:
    def __init__(self, product):
        self.product = product

    def create_clone(self):
        return self.product.clone()


# Пример использования
if __name__ == "__main__":
    # Создаем прототип продукта
    original_product = Product("iPhone 13", "Latest iPhone", 999.99)
    product_prototype = ProductPrototype(original_product)

    # Создаем клон прототипа
    clone1 = product_prototype.create_clone()

    # Изменяем свойства клона
    clone1.name = "iPhone 14"
    clone1.price = 1099.99
    
    clone2 = product_prototype.create_clone()
    clone2.name = "iPhone 15"
    clone2.price = 1199.99

    # Выводим клоны
    print(clone2)
    print(clone1)
    print(original_product)