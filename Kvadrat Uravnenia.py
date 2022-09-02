import math
print("Введите коофиценты:")
print("ax^2+bx+c=0")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
dis = b**2 - 4*(a*c)

if a ==0:
    x = (c/b)*-1
    print(x)

elif dis>0:
    x1 = (-b + math.sqrt(dis))/(2*a)
    x2 = (-b - math.sqrt(dis)) / (2 * a)
    print(print("x1 = %.2f \nx2 = %.2f" % (x1, x2)))
elif dis == 0:
    x = -b/(2*a)
    print("x = %.2f" % x)
elif dis <0:
    print('Корней нет')
