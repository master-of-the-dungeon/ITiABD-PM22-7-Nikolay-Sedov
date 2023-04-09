class MyClass:
    def __init__(self, lst):
        self.lst = lst

    def __add__(self, other):
        new_lst = self.lst + other.lst
        return MyClass(new_lst)

    def __str__(self):
        return str(self.lst)


# создаем несколько объектов класса
obj1 = MyClass([1, 2, 3])
obj2 = MyClass([4, 5, 6])

# складываем объекты
obj3 = obj1 + obj2

# выводим результат
print(obj3)  # [1, 2, 3, 4, 5, 6]
