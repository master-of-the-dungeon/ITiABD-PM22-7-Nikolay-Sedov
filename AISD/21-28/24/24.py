import math

class Triangle:
    def __init__(self, a, angle_b, angle_c):
        self.a = a
        self.angle_b = angle_b
        self.angle_c = angle_c

    @property
    def type(self):
        if self.angle_b == self.angle_c == 60:
            return "Равносторонний"
        elif self.angle_b == self.angle_c or self.angle_b + self.angle_c == 90 or self.angle_b == 90 or self.angle_c == 90:
            return "Равнобедренный или Прямоугольный"
        else:
            return "Обычный (не равносторонний, не равнобедренный и не прямоугольный"

    def compute_sides(self):
        b = self.a * math.sin(math.radians(self.angle_b)) / math.sin(math.radians(180 - self.angle_b - self.angle_c))
        c = self.a * math.sin(math.radians(self.angle_c)) / math.sin(math.radians(180 - self.angle_b - self.angle_c))
        return b, c

    def compute_angle_a(self):
        angle_a = 180 - self.angle_b - self.angle_c
        return angle_a
# Создаем экземпляр треугольника
# t = Triangle(5, 30, 60)
t = Triangle(3, 90, 53.13)

# Вычисляем другие две стороны
b, c = t.compute_sides()
print(f"Другие стороны треугольника: b={b:.2f}, c={c:.2f}")

# Вычисляем третий угол треугольника
angle_a = t.compute_angle_a()
print(f"Третий угол треугольника: {angle_a:.2f} градусов")

# Определяем тип треугольника
print(f"Тип треугольника: {t.type}")
