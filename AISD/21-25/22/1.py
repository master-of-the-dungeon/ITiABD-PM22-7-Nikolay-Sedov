import numpy as np
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

def min_by_golden_ratio(f, a, b, eps=1e-6):
    phi = (1 + np.sqrt(5)) / 2
    x1 = b - (b - a) / phi
    x2 = a + (b - a) / phi
    while abs(b - a) > eps:
        if f(x1) < f(x2):
            b = x2
            x2 = x1
            x1 = b - (b - a) / phi
        else:
            a = x1
            x1 = x2
            x2 = a + (b - a)



a, b = -1, 3

x = np.linspace(a, b, 1000)
y = f(x)
x_min_digit_search = min_by_digit_search(f, a, b)
print('Минимум функции по методу поразрядного поиска: x =', x_min_digit_search, ', f(x) =', f(x_min_digit_search))
x_min_dichotomy = min_by_dichotomy(f, a, b)
print('Минимум функции по методу дихотомии: x =', x_min_dichotomy, ', f(x) =', f(x_min_dichotomy))
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

