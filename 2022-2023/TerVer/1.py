import numpy as np
import matplotlib.pyplot as plt

# Значения и вероятности
values = np.array([-2, -1, 0, 1, 2])
probabilities = np.array([0.1, 0.2, 0.2, 0.4, 0.1])

# Построение полигона распределения
plt.figure(figsize=(8, 5))
plt.stem(values, probabilities, basefmt=" ", use_line_collection=True)
plt.xlabel("Значения случайной величины")
plt.ylabel("Вероятности")
plt.title("Полигон распределения")
plt.xticks(values)
plt.grid()
plt.show()

# Функция распределения
def distribution_function(x):
    if x < -2:
        return 0
    elif -2 <= x < -1:
        return 0.1
    elif -1 <= x < 0:
        return 0.3
    elif 0 <= x < 1:
        return 0.5
    elif 1 <= x < 2:
        return 0.9
    else:
        return 1

# Построение графика функции распределения
x_values = np.linspace(-3, 3, 1000)
y_values = [distribution_function(x) for x in x_values]

plt.figure(figsize=(8, 5))
plt.step(x_values, y_values, where="post")
plt.xlabel("Значения случайной величины")
plt.ylabel("F(x)")
plt.title("Функция распределения")
plt.xticks(values)
plt.yticks(np.arange(0, 1.1, 0.1))
plt.grid()
plt.show()
