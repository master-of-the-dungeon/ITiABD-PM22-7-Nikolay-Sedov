import numpy as np
import matplotlib.pyplot as plt

# Определение функции
def f(x):
    return x**3 + 4*x**2 - 4*x + 1

# Определение отрезка
a, b = -1 ,2

# Начальное приближение
x1, x2, x3 = a, (a+b)/2, b
y1, y2, y3 = f(x1), f(x2), f(x3)

# Определение функции, которая будет использоваться для поиска минимума
def parabolic_interpolation(x1, x2, x3, y1, y2, y3):
    a0 = y1
    a1 = (y2 - y1) / (x2 - x1)
    a2 = ((y3 - y1) / (x3 - x1) - a1) / (x3 - x2)
    x_min = 0.5 * (x1 + x2 - a1 / a2)
    return x_min

# Поиск минимума с заданной точностью
tolerance = 0.001
while abs(x3 - x1) > tolerance:
    x_min = parabolic_interpolation(x1, x2, x3, y1, y2, y3)
    y_min = f(x_min)
    if x_min > x2:
        if y_min > y2:
            x3, y3 = x_min, y_min
        else:
            x1, y1 = x2, y2
            x2, y2 = x_min, y_min
    else:
        if y_min > y2:
            x1, y1 = x_min, y_min
        else:
            x3, y3 = x2, y2
            x2, y2 = x_min, y_min

# Вывод результата
print(f"Минимум функции: x = {x2:.3f}, y = {y2:.3f}")

# Построение графика функции
x = np.linspace(a, b, 1000)
y = f(x)
plt.plot(x, y)
plt.plot(x2, y2, 'ro')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции')
plt.show()
