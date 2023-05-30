class Wolf:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.__food_dict = {"Мясо": 0.5, "Кости": 0.2, "Рыба": 0.3, "Овощи": 0.1}
        print("Появился волк по кличке", self.name)

    def howl(self):
        print("Ууу")

    def calculate_food_amount(self, days):
        total_food_amount = sum(self.__food_dict.values()) * days
        return total_food_amount


# Создаем объект класса Wolf
my_wolf = Wolf("Серый", 5, 30)

# Устанавливаем значения атрибутов
my_wolf.name = "Белый"
my_wolf.age = 7
my_wolf.weight = 35

# Вызываем метод howl
my_wolf.howl()

# Вычисляем количество необходимого корма на 10 дней
food_amount = my_wolf.calculate_food_amount(10)
print("Количество корма для волка", my_wolf.name, "на 10 дней:", food_amount)
