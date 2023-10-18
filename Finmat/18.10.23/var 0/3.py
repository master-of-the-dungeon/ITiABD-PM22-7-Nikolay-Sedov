def future_value_annuity(PMT, r, n):
    # Функция для вычисления будущей стоимости аннуитета с квартальной капитализацией
    FV = 0
    for i in range(n):
        FV += PMT * (1 + r)**(i//3)
    return FV

def present_value(FV, r, n):
    # Функция для вычисления начальной суммы инвестирования
    return FV / (1 + r)**n

# Исходные данные
r_yearly = 0.12
r_quarterly = r_yearly / 4
years_till_retirement = 60 - 37
quarters_till_retirement = years_till_retirement * 4
n = 15 * 12

# Вычисляем будущую стоимость аннуитета на момент начала пенсии
FV = future_value_annuity(10000, r_quarterly, n)

# Теперь вычисляем, сколько нужно вложить сегодня
PV = present_value(FV, r_quarterly, quarters_till_retirement)

print(f"Необходимая сумма для вложения сегодня: {PV:.2f} руб.")
