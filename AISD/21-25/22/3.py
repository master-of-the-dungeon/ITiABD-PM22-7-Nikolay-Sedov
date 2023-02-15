# import math
# import matplotlib.pyplot as plt
#
# # Функция для вычисления значения функции
# def f(x):
#     return x**2 - 2*x - math.cos(x)
#
# # Метод средней точки
# def midpoint_method(a, b, eps):
#     while abs(b - a) > eps:
#         c = (a + b) / 2
#         x1 = (a + c) / 2
#         x2 = (c + b) / 2
#         if f(x1) >= f(x2):
#             a = x1
#         else:
#             b = x2
#     return (a + b) / 2
#
# # Метод хорд
# def chord_method(a, b, eps):
#     while abs(b - a) > eps:
#         c = (a*f(b) - b*f(a)) / (f(b) - f(a))
#         if f(a) * f(c) < 0:
#             b = c
#         else:
#             a = c
#     return (a + b) / 2
#
# # Метод Ньютона
# def newton_method(a, b, eps):
#     x = (a + b) / 2
#     while True:
#         df = 2*x - 2 + math.sin(x)
#         ddf = 2 - math.cos(x)
#         x_new = x - df/ddf
#         if abs(x_new - x) < eps:
#             return x_new
#         x = x_new
#
# # Задаем отрезок и точность
# a, b = -0.5, 1
# eps = 1e-6
#
# # Находим минимум с помощью каждого метода
# midpoint_min = midpoint_method(a, b, eps)
# chord_min = chord_method(a, b, eps)
# newton_min = newton_method(a, b, eps)
#
# # Выводим результаты
# print(f"Минимум с помощью метода средней точки: {midpoint_min}")
# print(f"Минимум с помощью метода хорд: {chord_min}")
# print(f"Минимум с помощью метода Ньютона: {newton_min}")
#
# # Строим график функции
# x = [i/100 for i in range(-50, 101)]
# y = [f(xi) for xi in x]
# plt.plot(x, y)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("График функции f(x) = x^2 - 2x - cos(x)")
# plt.show()
# import math
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Функция для вычисления значения функции
# def f(x):
#     return x**2 - 2*x - np.cos(x)
#
# # Функция для вычисления производных
# def df(x):
#     return 2*x - 2 + np.sin(x)
#
# def ddf(x):
#     return 2 - np.cos(x)
#
# # Метод средней точки
# def midpoint_method(a, b, eps):
#     while abs(b - a) > eps:
#         c = (a + b) / 2
#         x1 = (a + c) / 2
#         x2 = (c + b) / 2
#         if f(x1) >= f(x2):
#             a = x1
#         else:
#             b = x2
#     return (a + b) / 2
#
# # Метод хорд
# def chord_method(a, b, eps):
#     while abs(b - a) > eps:
#         c = (a*f(b) - b*f(a)) / (f(b) - f(a))
#         if f(a) * f(c) < 0:
#             b = c
#         else:
#             a = c
#     return (a + b) / 2
#
# # Метод Ньютона
# def newton_method(a, b, eps):
#     x = (a + b) / 2
#     while True:
#         x_new = x - df(x)/ddf(x)
#         if abs(x_new - x) < eps:
#             return x_new
#         x = x_new
#
# # Задаем отрезок и точность
# a, b = -0.5, 1
# eps = 1e-6
#
# # Находим минимум с помощью каждого метода
# midpoint_min = midpoint_method(a, b, eps)
# chord_min = chord_method(a, b, eps)
# newton_min = newton_method(a, b, eps)
#
# # Выводим результаты
# print(f"Минимум с помощью метода средней точки: {midpoint_min}")
# print(f"Минимум с помощью метода хорд: {chord_min}")
# print(f"Минимум с помощью метода Ньютона: {newton_min}")
#
# # Строим график функции
# x = np.linspace(a, b, 1000)
# y = f(x)
# plt.plot(x, y)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("График функции f(x) = x^2 - 2x - cos(x)")
# plt.show()
import math
import matplotlib.pyplot as plt

# Функция для вычисления значения функции
def f(x):
    return x**2 - 2*x - math.cos(x)

# Метод средней точки
midpoint_method = lambda a, b, eps: (a + b) / 2 if abs(b - a) < eps else midpoint_method((a + (a + b) / 2) / 2 if f((a + (a + b) / 2) / 2) >= f(((a + b) / 2 + b) / 2) else (a + b) / 2, ((a + b) / 2 + b) / 2 if f((a + (a + b) / 2) / 2) >= f(((a + b) / 2 + b) / 2) else (a + (a + b) / 2) / 2, eps)

# Метод хорд
chord_method = lambda a, b, eps: (a + b) / 2 if abs(b - a) < eps else chord_method(a, (a * f(b) - b * f(a)) / (f(b) - f(a)), eps) if f(a) * f((a * f(b) - b * f(a)) / (f(b) - f(a))) < 0 else chord_method((a * f(b) - b * f(a)) / (f(b) - f(a)), b, eps)

# Метод Ньютона
newton_method = lambda a, b, eps: newton_method(x_new, b, eps) if abs(x_new - x) >= eps else x_new if abs(x_new - x) < eps else newton_method(x_new, b, eps)
                 x = (a + b) / 2
                 x_new = x - (2*x - 2 + math.sin(x))/(2 - math.cos(x))
                 return newton_method(x_new, b, eps) if x_new > b else x_new

# Задаем отрезок и точность
a, b = -0.5, 1
eps = 1e-6

# Находим минимум с помощью каждого метода
midpoint_min = midpoint_method(a, b, eps)
chord_min = chord_method(a, b, eps)
newton_min = newton_method(a, b, eps)

# Выводим результаты
print(f"Минимум с помощью метода средней точки: {midpoint_min}")
print(f"Минимум с помощью метода хорд: {chord_min}")
print(f"Минимум с помощью метода Ньютона: {newton_min}")

# Строим график функции
x = [i/100 for i in range(-50, 101)]
y = [f(xi)
