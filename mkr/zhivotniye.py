class Animal:
    def __init__(self, name):
        self.__name = name
        print("Родилось животное")

    def eat(self):
        print("Кус-кус")

    def get_Name(self):
        return self.__name

    def set_Name(self, name):
        self.__name = name

    def make_Noise(self):
        print(self.__name, "говорит Гррр")


class Wolf(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("Появился волк")

    def make_Noise(self):
        print(self.get_Name(), "говорит У-у-у")


# Создаем объект класса Animal
my_animal = Animal("Мурзик")

# Вызываем методы объекта
my_animal.eat()
my_animal.set_Name("Васька")
my_animal.make_Noise()

# Создаем объект класса Wolf
my_wolf = Wolf("Серый")

# Вызываем методы объекта Wolf
my_wolf.eat()
my_wolf.make_Noise()
