def calc(a):
    ls = a.split(' ')
    alf = {
        'один':1,
        'два':2,
        'три':3,
        'четыре':4,
        'пять':5,
        'шесть':6,
        'семь':7,
        'восемь':8,
        'девять':9,
        'десять':10,
        'одиннадцать':11,
        'двенадцать':12,
        'тринадцать':13,
        'четырнадцать':14,
        'пятнадцать':15,
        'шестнадцать':16,
        'семнадцать':17,
        'восемнадцать':18,
        'девятнадцать':19,
        'двадцать':20,
        'двадцать один':21,
        'тридцать':30,
        'сорок':40,
        'пятьдесят':50,
        'шестьдесят':60,
        'семьдесят':70,
        'восемьдесят':80,
        'девяносто':90,
        'сто':100
        }
    alf_op = {
        'плюс': lambda x, y: x + y,
        'минус': lambda x, y: x - y,
        'делить': lambda x, y: x / y,
        'умножить': lambda x, y: x * y
    }
    i = 0
    try:
        e1 = alf[ls[i]]
    except KeyError:
        raise NotImplementedError
    i += 1

    try:
        func = alf_op[ls[i]]
    except KeyError:
        raise ValueError('ожидался оператор, найдена ересь: "%s"' % ls[i])
    i += 1

    try:
        e2 = alf[ls[i]]
    except KeyError:
        raise NotImplementedError
    i += 1

    if i != len(ls):
        raise ValueError('найдена ересь: "%s"' % ls[i:])

    r = func(e1, e2)
    print(r)
a = str(input())
calc(a)