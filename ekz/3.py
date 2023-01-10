# Функция func(2, 4), в качестве аргумента принимает другую функцию (не
# встроенную в Python). В результате работы она выводит следующие данные:
# название переданной функции, наименование всех принимаемых ею параметров и их
# типы (позиционные, ключевые, целые вещественные, строковые). Например, для
# вызова функции с данными параметрами func(subfunс (17, a=9.5)), должно быть
# выдано: имя функции subfunс, первый параметр позиционный целого типа, второй
# параметр ключевой вещественного типа.
import inspect
def func(f):
    print(inspect.currentframe().f_back)


def subfunc(*x, **y):
    # print(y)
    for i in y.keys():
        print(i)
        if type(y[i]) == int:
            print('Параметр ключевой целого типа')
        if type(y[i]) == float:
            print('Параметр ключевой вещественного типа')
        if type(y[i]) == str:
            print('Параметр ключевой строкового типа')
    for j in x:
        print(j)
        if type(j) == int:
            print('Параметр позиционный целого типа')
        if type(j) == float:
            print('Параметр позиционный вещественного типа')
        if type(j) == str:
            print('Параметр позиционный строкового типа')


func(subfunc(17, a=9.5,b ='a',c=3))