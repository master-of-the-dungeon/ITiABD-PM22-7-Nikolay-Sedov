# Написать калькулятор для строковых выражений вида '<число> <операция> <число>', где <число> - не отрицательное целое число
# меньшее 100, записанное словами, например "тридцать четыре", <арифмитическая операция> - одна из операций "плюс", "минус",
# "умножить". Результат выполнения операции вернуть в виде текстового представления числа. Пример calc("двадцать пять плюс
# тринадцать") -> "тридцать восемь"
# Оформить калькулятор в виде функции, которая принимает на вход строку и возвращает строку.

# 10) Диагностировать ошибки: неправильную запись числа; неправильную последовательность чисел и операций; (задание 1) деление
# на ноль; (задание 3) неправильную последовательность чисел и операций; (задание 4) некорректный баланс и вложенность скобок;
# (задание 6) некорректную запись числа


d = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9,
     'десять': 10, 'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13, 'четырнадцать': 14, 'пятнадцать': 15,
     'шестнадцать': 16, 'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19, 'двадцать': 20, 'двадцать один': 21,
     'двадцать два': 22, 'двадцать три': 23, 'двадцать четыре': 24, 'двадцать пять': 25, 'двадцать шесть': 26,
     'двадцать семь': 27, 'двадцать восемь': 28, 'двадцать девять': 29, 'тридцать': 30, 'тридцать один': 31,
     'тридцать два': 32, 'тридцать три': 33, 'тридцать четыре': 34, 'тридцать пять': 35, 'тридцать шесть': 36,
     'тридцать семь': 37, 'тридцать восемь': 38, 'тридцать девять': 39, 'сорок': 40, 'сорок один': 41, 'сорок два': 42,
     'сорок три': 43, 'сорок четыре': 44, 'сорок пять': 45, 'сорок шесть': 46, 'сорок семь': 47, 'сорок восемь': 48,
     'сорок девять': 49, 'пятьдесят': 50, 'пятьдесят один': 51, 'пятьдесят два': 52, 'пятьдесят три': 53,
     'пятьдесят четыре': 54, 'пятьдесят пять': 55, 'пятьдесят шесть': 56, 'пятьдесят семь': 57, 'пятьдесят восемь': 58,
     'пятьдесят девять': 59, 'шестьдесят': 60, 'шестьдесят один': 61, 'шестьдесят два': 62, 'шестьдесят три': 63,
     'шестьдесят четыре': 64, 'шестьдесят пять': 65, 'шестьдесят шесть': 66, 'шестьдесят семь': 67,
     'шестьдесят восемь': 68, 'шестьдесят девять': 69, 'семьдесят': 70, 'семьдесят один': 71, 'семьдесят два': 72,
     'семьдесят три': 73, 'семьдесят четыре': 74, 'семьдесят пять': 75, 'семьдесят шесть': 76, 'семьдесят семь': 77,
     'семьдесят восемь': 78, 'семьдесят девять': 79, 'восемьдесят': 80, 'восемьдесят один': 81, 'восемьдесят два': 82,
     'восемьдесят три': 83, 'восемьдесят четыре': 84, 'восемьдесят пять': 85, 'восемьдесят шесть': 86,
     'восемьдесят семь': 87, 'восемьдесят восемь': 88, 'восемьдесят девять': 89, 'девяносто': 90, 'девяносто один': 91,
     'девяносто два': 92, 'девяносто три': 93, 'девяносто четыре': 94, 'девяносто пять': 95, 'девяносто шесть': 96,
     'девяносто семь': 97, 'девяносто восемь': 98, 'девяносто девять': 99, 'сто': 100}
k = input('ВВЕДИТЕ ВЫРАЖЕНИЕ-->> ').lower()

if k.count('плюс') == 0 and k.count('минус') == 0 and k.count('умножить') == 0 and k.count('делить') == 0:
    while k.count('плюс') == 0 and k.count('минус') == 0 and k.count('умножить') == 0 and k.count('делить') == 0:
        k = input('повторите ввод ').lower()

if 'скобка' in k:  # для выражений со скобками
    if k.count('скобка') % 2 != 0:
        while k.count('скобка') % 2 != 0:
            k = input('повторите ввод ').lower()
    if k.count('скобка') % 2 == 0:
        k1 = k[k.find('скобка') + 7: k.rfind('скобка') - 1]  # выражение в скобках

        if 'плюс' in k1:
            while 'плюс' in k1:
                if k1[:k1.find('плюс') - 1] not in d:
                    while k1[:k1.find('плюс') - 1] not in d:
                        k1 = input('повторите ввод выражения в скобках ').lower()
                if k1[k1.find('плюс') + 5:] not in d:
                    while k1[k1.find('плюс') + 5:] not in d:
                        k1 = input('повторите ввод выражения в скобках ').lower()
                for i in d:
                    for j in d:
                        if i == k1[:k1.find('плюс') - 1] and j == k1[k1.find('плюс') + 5:]:
                            for n in d:
                                if d[n] == d[i] + d[j]:
                                    c = d[n]
                                    s = i + ' плюс ' + j + ' равно ' + n
                break
                print(s)

        if 'минус' in k1:
            while 'минус' in k1:
                if k1[:k1.find('минус') - 1] not in d:
                    while k1[:k1.find('минус') - 1] not in d:
                        k1 = input('повторите ввод выражения в скобках ').lower()
                if k1[k1.find('минус') + 6:] not in d:
                    while k1[k1.find('минус') + 6:] not in d:
                        k1 = input('повторите ввод выражения в скобках ').lower()
                for i in d:
                    for j in d:
                        if i == k1[:k1.find('минус') - 1] and j == k1[k1.find('минус') + 6:]:
                            for n in d:
                                if d[n] == d[i] - d[j]:
                                    c = d[n]
                                    s = i + ' минус ' + j + ' равно ' + n
                break
                print(s)

        if 'умножить' in k1:
            while 'умножить' in k1:
                if k1[:k1.find('умножить') - 1] not in d:
                    while k1[:k1.find('умножить') - 1] not in d:
                        k1 = input('повторите ввод выражения в скобках ').lower()
                if k1[k1.find('умножить') + 9:] not in d:
                    while k1[k1.find('умножить') + 9:] not in d:
                        k = input('повторите ввод выражения в скобках ').lower()
                for i in d:
                    for j in d:
                        if i == k1[:k1.find('умножить') - 1] and j == k1[k1.find('умножить') + 9:]:
                            for n in d:
                                if d[n] == d[i] * d[j]:
                                    c = d[n]
                                    s = i + ' умножить на ' + j + ' равно ' + n
                break
                print(s)

        if 'делить' in k1:
            while 'делить' in k1:
                if k1[:k1.find('делить') - 1] not in d:
                    while k1[:k1.find('делить') - 1] not in d:
                        k1 = input('повторите ввод ').lower()
                if k1[k1.find('делить') + 7:] not in d:
                    while k1[k1.find('делить') + 7:] not in d:
                        k1 = input('повторите ввод выражения в скобках ').lower()
                if k1[k1.find('делить') + 7:] == 'ноль':
                    while k1[k1.find('делить') + 7:] == 'ноль':
                        k1 = input('повторите ввод выражения в скобках ').lower()
                for i in d:
                    for j in d:
                        if i == k1[:k1.find('делить') - 1] and j == k1[k1.find('делить') + 7:]:
                            for n in d:
                                if d[n] == d[i] / d[j]:
                                    c = d[n]
                                    s = i + ' делить на ' + j + ' равно ' + n
                break
                print(s)

        if k.find(
                'скобка') == 0:  # для случая когда выражение начинается со скобки (скобка три плюс три скобка минус один)
            k2 = k[k.rfind('скобка') + 7:]  # срез того, что идет после скобок (минус один)
            if 'плюс' in k2:
                def addition(k2):
                    while 'плюс' in k2:
                        if k2[k2.find('плюс') + 5:] not in d:
                            while k2[k2.find('плюс') + 5:] not in d:
                                k2 = input('повторите ввод выражения после скобок ').lower()
                        for i in d:
                            if i == k2[k2.find('плюс') + 5:]:
                                for n in d:
                                    if d[n] == d[i] + c:
                                        s = k + ' равно ' + n
                        return (s)
                        break


                print(addition(k2))

            if 'минус' in k2:
                def subtraction(k2):
                    while 'минус' in k2:
                        if k2[k2.find('минус') + 6:] not in d:
                            while k2[k2.find('минус') + 6:] not in d:
                                k2 = input('повторите ввод выражения после скобок ').lower()
                        for i in d:
                            if i == k2[k2.find('минус') + 6:]:
                                for n in d:
                                    if d[n] == c - d[i]:
                                        s = k + ' равно ' + n
                        return (s)
                        break
            # print(subtraction(k2))

            if 'умножить' in k2:
                def multiplication(k2):
                    while 'умножить' in k2:
                        if k2[k2.find('умножить') + 9:] not in d:
                            while k2[k2.find('умножить') + 9:] not in d:
                                k2 = input('повторите ввод выражения после скобок ').lower()
                        for i in d:
                            if i == k2[k2.find('умножить') + 9:]:
                                for n in d:
                                    if d[n] == d[i] * c:
                                        s = k + ' равно ' + n
                        return (s)
                        break


                print(multiplication(k2))

            if 'делить' in k2:
                def division(k2):
                    while 'делить' in k2:
                        if k2[k2.find('делить') + 7:] not in d:
                            while k2[k2.find('делить') + 7:] not in d:
                                k1 = input('повторите ввод выражения после скобок ').lower()
                        if k2[k2.find('делить') + 7:] == 'ноль':
                            while k2[k2.find('делить') + 7:] == 'ноль':
                                k2 = input('повторите ввод выражения после скобок ').lower()
                        for i in d:
                            if i == k2[k2.find('делить') + 7:]:
                                for n in d:
                                    if d[n] == c // d[i]:
                                        s = k + ' равно ' + n
                        return (s)
                        break


                print(division(k2))

        if k.find('скобка') != 0:  # когда начинается не со скобки (три плюс скобка три плюс три скобка)
            k2 = k[: k.find('скобка') - 1]
            if 'плюс' in k2:
                k2[: k2.find('плюс') - 1]


                def addition(k2):
                    while 'плюс' in k2:
                        if k2[: k2.find('плюс') - 1] not in d:
                            while k2[: k2.find('плюс') - 1] not in d:
                                k2 = input('повторите ввод выражения до скобок ').lower()
                        for i in d:
                            if i == k2[: k2.find('плюс') - 1]:
                                for n in d:
                                    if d[n] == d[i] + c:
                                        s = k + ' равно ' + n
                        return (s)
                        break


                print(addition(k2))

            if 'минус' in k2:
                k2[: k2.find('минус') - 1]


                def subtraction(k2):
                    while 'минус' in k2:
                        if k2[: k2.find('минус') - 1] not in d:
                            while k2[: k2.find('минус') - 1] not in d:
                                k2 = input('повторите ввод выражения до скобок ').lower()
                        for i in d:
                            if i == k2[: k2.find('минус') - 1]:
                                for n in d:
                                    if d[n] == d[i] - c:
                                        s = k + ' равно ' + n
                        return (s)
                        break


                print(subtraction(k2))

            if 'умножить' in k2:
                k2[: k2.find('умножить') - 1]


                def multiplication(k2):
                    while 'умножить' in k2:
                        if k2[: k2.find('умножить') - 1] not in d:
                            while k2[: k2.find('умножить') - 1] not in d:
                                k2 = input('повторите ввод выражения до скобок ').lower()
                        for i in d:
                            if i == k2[: k2.find('умножить') - 1]:
                                for n in d:
                                    if d[n] == d[i] * c:
                                        s = k + ' равно ' + n
                        return (s)
                        break


                print(multiplication(k2))

            if 'делить' in k2:
                def division(k2):
                    while 'делить' in k2:
                        if k2[: k2.find('делить') - 1] not in d:
                            while k2[: k2.find('делить') - 1] not in d:
                                k1 = input('повторите ввод выражения до скобок ').lower()
                        if k2[: k2.find('делить') - 1] == 'ноль':
                            while k2[: k2.find('делить') - 1] == 'ноль':
                                k2 = input('повторите ввод выражения до скобок ').lower()
                        for i in d:
                            if i == k2[: k2.find('делить') - 1]:
                                for n in d:
                                    if d[n] == d[i] // c:
                                        s = k + ' равно ' + n
                        return (s)
                        break


                print(division(k2))

if 'скобка' not in k:
    if 'плюс' in k:
        def addition(k):
            while 'плюс' in k:
                if k[:k.find('плюс') - 1] not in d:
                    while k[:k.find('плюс') - 1] not in d:
                        k = input('повторите ввод ').lower()
                if k[k.find('плюс') + 5:] not in d:
                    while k[k.find('плюс') + 5:] not in d:
                        k = input('повторите ввод ').lower()
                for i in d:
                    for j in d:
                        if i == k[:k.find('плюс') - 1] and j == k[k.find('плюс') + 5:]:
                            for n in d:
                                if d[n] == d[i] + d[j]:
                                    s = i + ' плюс ' + j + ' равно ' + n
                return (s)
                break


        print(addition(k))

    if 'минус' in k:
        def subtraction(k):
            while 'минус' in k:
                if k[:k.find('минус') - 1] not in d:
                    while k[:k.find('минус') - 1] not in d:
                        k = input('повторите ввод ').lower()
                if k[k.find('минус') + 6:] not in d:
                    while k[k.find('минус') + 6:] not in d:
                        k = input('повторите ввод ').lower()
                for i in d:
                    for j in d:
                        if i == k[:k.find('минус') - 1] and j == k[k.find('минус') + 6:]:
                            for n in d:
                                if d[n] == d[i] - d[j]:
                                    s = i + ' минус' + j + ' равно ' + n
                return (s)
                break


        print(subtraction(k))

    if 'умножить' in k:
        def multiplication(k):
            while 'умножить' in k:
                if k[:k.find('умножить') - 1] not in d:
                    while k[:k.find('умножить') - 1] not in d:
                        k = input('повторите ввод ').lower()
                if k[k.find('умножить') + 9:] not in d:
                    while k[k.find('умножить') + 9:] not in d:
                        k = input('повторте ввод ').lower()
                for i in d:
                    for j in d:
                        if i == k[:k.find('умножить') - 1] and j == k[k.find('умножить') + 9:]:
                            for n in d:
                                if d[n] == d[i] * d[j]:
                                    s = i + ' умножить на ' + j + ' равно ' + n
                return (s)
                break


        print(multiplication(k))

    if 'делить' in k:
        def division(k):
            while 'делить' in k:
                if k[:k.find('делить') - 1] not in d:
                    while k[:k.find('делить') - 1] not in d:
                        k = input('повторите ввод ').lower()
                if k[k.find('делить') + 7:] not in d:
                    while k[k.find('делить') + 7:] not in d:
                        k = input('повторите ввод ').lower()
                if k[k.find('делить') + 7:] == 'ноль':
                    while k[k.find('делить') + 7:] == 'ноль':
                        k = input('повторите ввод ').lower()
                for i in d:
                    for j in d:
                        if i == k[:k.find('делить') - 1] and j == k[k.find('делить') + 7:]:
                            for n in d:
                                if d[n] == d[i] / d[j]:
                                    s = i + ' делить на ' + j + ' равно ' + n
                return (s)
                break


        print(division(k))