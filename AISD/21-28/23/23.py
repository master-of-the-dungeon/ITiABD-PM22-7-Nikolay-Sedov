import math
class Cone:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def calculate_volume(self):
        return (1 / 3) * math.pi * (self.radius ** 2) * self.height

    def calculate_area(self):
        slant_height = (self.radius ** 2 + self.height ** 2) ** 0.5
        base_area = math.pi * (self.radius ** 2)
        lateral_area = math.pi * self.radius * slant_height
        return base_area + lateral_area


# Создание нескольких экземпляров класса Конус
cone1 = Cone(5, 10)
cone2 = Cone(3, 7)

# Вычисление объема и площади каждого конуса
volume1 = cone1.calculate_volume()
area1 = cone1.calculate_area()
volume2 = cone2.calculate_volume()
area2 = cone2.calculate_area()

# Вывод результатов вычислений
print(f"Объем первого конуса: {volume1}")
print(f"Площадь первого конуса: {area1}")
print(f"Объем второго конуса: {volume2}")
print(f"Площадь второго конуса: {area2}")
