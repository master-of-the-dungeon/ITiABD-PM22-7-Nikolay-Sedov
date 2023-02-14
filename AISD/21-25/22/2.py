import numpy as np
from scipy.optimize import minimize_scalar
import matplotlib.pyplot as plt

def f(x):
    return x**3 + 4*x**2 + 1

a, b = -1, 2
res = minimize_scalar(f, bounds=(a, b), method='bounded')
x_min = res.x
y_min = res.fun

print("Минимум функции f(x) на отрезке [{}, {}] равен {:.4f} при x = {:.4f}".format(a, b, y_min, x_min))

x = np.linspace(a, b, 100)
y = f(x)

plt.plot(x, y, label='f(x)')
plt.plot(x_min, y_min, 'ro', label='Минимум')
plt.legend()
plt.show()
