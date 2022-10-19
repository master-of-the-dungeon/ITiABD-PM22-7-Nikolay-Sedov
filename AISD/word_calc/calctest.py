digit = {"ноль":0,"один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5, "шесть": 6, "семь": 7, "восемь": 8, "девять": 9, \
         "одиннадцать": 11, "двенадцать": 12, "тринадцать": 13, "четырнадцать": 14, "пятнадцать": 15, "шестнадцать": 16,
         "семнадцать": 17, "восемнадцать": 18, "девятнадцать": 19, \
         "десять": 10, "двадцать": 20, "тридцать": 30, "сорок": 40, "пятьдесят": 50, "шестьдесят": 60, "семьдесят": 70,
         "восемьдесят": 80, "девяносто": 90,"сто":100,
         'плюс': '+', 'минус': '-', 'умножить': '*', 'делить': '/'}


def calc(calc=str(input('Ведите выражение: ')).split(' ')):
    ls = list(calc)

    del1 = ''.join(ls)

    try:
        delete = del1.find('на')
        if delete != 0:
            ls.remove('на')
    except:
        pass

    count = len(ls)

    for i in range(0, count):
        ls[i] = digit.get(ls[i])

    if count == 3:
        if ls[1] == '+':
            answer = ls[0] + ls[2]
        elif ls[1] == '-':
            answer = ls[0] - ls[2]
        elif ls[1] == '*':
            answer = ls[0] * ls[2]
        elif ls[1] == '/':
            answer = ls[0] / ls[2]


    elif count == 5:
        y1 = ls[0] + ls[1]
        y2 = ls[3] + ls[4]
        if ls[2] == '+':
            answer = y1 + y2
        elif ls[2] == '-':
            answer = y1 - y2
        elif ls[2] == '*':
            answer = y1 * y2
        elif ls[2] == '/':
            answer = y1 / y2


    elif count == 4:
        if ls[1] == '+' or ls[1] == '-' or ls[1] == '*':
            y2 = ls[2] + ls[3]
            if ls[1] == '+':
                answer = ls[0] + y2
            elif ls[1] == '-':
                answer = ls[0] - y2
            elif ls[1] == '*':
                answer = ls[0] * y2
            elif ls[2] == '/':
                answer = ls[0] / y2
            elif ls[2] == '**':
                answer = ls[0] ** y2
        elif ls[2] == '+' or ls[2] == '-' or ls[2] == '*':
            y1 = ls[0] + ls[1]
            if ls[1] == '+':
                answer = y1 + ls[3]
            elif ls[1] == '-':
                answer = y1 - ls[3]
            elif ls[1] == '*':
                answer = ls[3] * y1
            elif ls[1] == '/':
                answer = y1 / ls[3]


    return round(answer, 3)


print(calc())