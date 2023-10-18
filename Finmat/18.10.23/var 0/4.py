def bond_B_price(r_B, F_B, y, T):
    C = r_B * F_B
    price = sum([C / (1+y)**t for t in range(1, T+1)]) + F_B / (1+y)**T
    return price

# Исходные данные
P_A = 708.4252
F_A = 1000
r_B = 0.12
F_B = 1000
y = 0.09
T = 5
debt = 200000

# Вычисляем цену облигации B
P_B = bond_B_price(r_B, F_B, y, T)

# Создаем систему уравнений:
# x - количество облигаций A
# y - количество облигаций B

# 200000 = x * P_A + y * P_B

# Пусть мы купим максимальное количество облигаций A
x_max = int(debt / P_A)
remaining_debt = debt - x_max * P_A

y_required = int(remaining_debt / P_B)

print(f"Количество 4-летних облигаций типа A: {x_max}")
print(f"Количество 7-летних облигаций типа B: {y_required}")
