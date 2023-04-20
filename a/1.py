class BaseClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_quality(self):
        return self.a + self.b

    def get_info(self):
        print(f"Object: a={self.a}, b={self.b}, quality={self.calculate_quality()}")


class ChildClass(BaseClass):
    def __init__(self, a, b, p):
        super().__init__(a, b)
        self.p = p

    def calculate_quality(self):
        return self.a + self.b + self.p

    def get_info(self):
        print(f"Object: a={self.a}, b={self.b}, p={self.p}, quality={self.calculate_quality()}")


# создаем объекты классов
base_obj = BaseClass(2, 3)
child_obj = ChildClass(2, 3, 4)

# выводим информацию об объектах
base_obj.get_info()
child_obj.get_info()
