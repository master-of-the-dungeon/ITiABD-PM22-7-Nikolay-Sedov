import random
d = {a: a**2 for a in range(7)}
students = {}
def a(d):
    for i in range(len(d)):
        print(d[i])
def b(d):
    sum = 0
    for i in range(len(d)):
        sum+=d[i]
    print(sum)
def c():
    students = {'Лев Троцкий':[193,79], 'Ганнибал Лектер':[175,98],'Вася Пупкин':[297,1300],'Давид Мастейненко':[187,73]}
    print('Выше какого роста: ')
    a = int(input())
    print('Тяжелее какого веса: ')
    b = int(input())
    for name in students.keys() :
        if students[name][0]>=a and students[name][1]>=b:
            print(name)
c()