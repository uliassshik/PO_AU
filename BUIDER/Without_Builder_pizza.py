class Pizza:
    def __init__(self, size, crust, toppings, sauce):
        self.size = size
        self.crust = crust
        self.toppings = toppings
        self.sauce = sauce

    def __str__(self):
        return f"Пицца: {self.size} {self.crust} с начинкой {self.toppings} и соусом {self.sauce}"


if __name__ == "__main__":
    # Создаем пиццу напрямую, указав все параметры
    pizza = Pizza("Большая", "Тонкая", ["Пепперони", "Грибы", "Лук"], "Томатный")

    # Выводим пиццу
    print(pizza)