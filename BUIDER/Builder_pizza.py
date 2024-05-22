# Строитель
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size

    def set_crust(self, crust):
        self.pizza.crust = crust

    def add_toppings(self, toppings):
        self.pizza.toppings.extend(toppings)

    def set_sauce(self, sauce):
        self.pizza.sauce = sauce

    def get_pizza(self):
        return self.pizza


# Конкретный строитель для пиццы
class PizzaBuilderImpl(PizzaBuilder):
    def __init__(self):
        super().__init__()
        self.pizza.toppings = []


# Класс продукта (пицца)
class Pizza:
    def __init__(self):
        self.size = None
        self.crust = None
        self.toppings = []
        self.sauce = None

    def __str__(self):
        return f"Пицца: {self.size} {self.crust} с начинкой {self.toppings} и соусом {self.sauce}"


# Директор, который управляет процессом создания пиццы
class PizzaDirector:
    def __init__(self, pizza_builder):
        self.pizza_builder = pizza_builder

    def create_pizza(self, size, crust, toppings, sauce):
        self.pizza_builder.set_size(size)
        self.pizza_builder.set_crust(crust)
        self.pizza_builder.add_toppings(toppings)
        self.pizza_builder.set_sauce(sauce)
        return self.pizza_builder.get_pizza()


# Пример использования
if __name__ == "__main__":
    # Создаем строителя и директора для конкретного типа пиццы
    pizza_builder = PizzaBuilderImpl()
    pizza_director = PizzaDirector(pizza_builder)

    # Создаем пиццу, указывая пошагово ее характеристики
    pizza = pizza_director.create_pizza('Большая', "Тонкая", ["Пепперони", "Грибы", "Лук"], "Томатный")

    # Выводим пиццу
    print(pizza)