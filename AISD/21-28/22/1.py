import numpy as np
import math
import matplotlib.pyplot as plt
def f(x):
    return 2 * (x ** 2) - 6 * x - 3
def min_by_digit_search(f, a, b, eps=1e-6):
    l, r = a, b
    while (r - l) > eps:
        m = (l + r) / 2
        if f(m - eps) < f(m + eps):
            r = m
        else:
            l = m
    return (l + r) / 2

def min_by_dichotomy(f, a, b, eps=1e-6):
    l, r = a, b
    while (r - l) > eps:
        m = (l + r) / 2
        if f(m - eps) < f(m + eps):
            r = m
        else:
            l = m
    return (l + r) / 2

# def min_by_golden_ratio(f, a, b, eps=1e-6):
#     phi = (1 + np.sqrt(5)) / 2
#     x1 = b - (b - a) / phi
#     x2 = a + (b - a) / phi
#     while abs(b - a) > eps:
#         if f(x1) < f(x2):
#             b = x2
#             x2 = x1
#             x1 = b - (b - a) / phi
#         else:
#             a = x1
#             x1 = x2
#             x2 = a + (b - a)
# def golden_section(a, b, eps):
#     t = (math.sqrt(5) - 1) / 2
#     x1 = b - t * (b - a)
#     x2 = a + t * (b - a)
#     while abs(b - a) > eps:
#         if f(x1) < f(x2):
#             b = x2
#             x2 = x1
#             x1 = b - t * (b - a)
#         else:
#             a = x1
#             x1 = x2
#             x2 = a + t * (b - a)
#     return (a + b) / 2
def golden_ratio(f, a, b, eps=1e-6):

    golden_ratio = (1 + math.sqrt(5)) / 2  # Золотое сечение
    x1 = b - (b - a) / golden_ratio
    x2 = a + (b - a) / golden_ratio
    f1, f2 = f(x1), f(x2)
    while abs(b - a) > eps:
        if f1 < f2:
            b = x2
            x2, f2 = x1, f1
            x1 = b - (b - a) / golden_ratio
            f1 = f(x1)
        else:
            a = x1
            x1, f1 = x2, f2
            x2 = a + (b - a) / golden_ratio
            f2 = f(x2)
    x_min = (a + b) / 2
    return x_min

a, b = -1, 3

x = np.linspace(a, b, 1000)
y = f(x)
x_min_digit_search = min_by_digit_search(f, a, b)
print('Минимум функции по методу поразрядного поиска: x =', x_min_digit_search, ', f(x) =', f(x_min_digit_search))
x_min_dichotomy = min_by_dichotomy(f, a, b)
print('Минимум функции по методу дихотомии: x =', x_min_dichotomy, ', f(x) =', f(x_min_dichotomy))
x_min_golden_ratio = golden_ratio(f, a, b)
print(f"Минимум функции по методу золотого сечения x = {x_min_golden_ratio}", ', f(x) =', f(x_min_golden_ratio) )
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

