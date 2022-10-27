import numpy
def str2int(a):             #перевод строки в целые числа
    for i in range(len(a)):
        a[i] = int(a[i])

def sum(a):                 #сумма
    summ = 0
    for i in range(len(a)):
        summ+=a[i]
    return summ

def product(a):         #произведение
    prod = 1
    for i in range(len(a)):
        prod*=a[i]
    return prod

def mean(a):            #среднее арифметическое
    return numpy.mean(a)

a = input().split()
str2int(a)
print("Сумма: ",sum(a))
print("Произведение: ",product(a))
print("Среднее арифметическое: ",mean(a))