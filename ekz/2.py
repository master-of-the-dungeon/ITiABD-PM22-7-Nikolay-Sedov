#Для произвольного значения x найти сумму первых пяти элементов убывающего
#ряда: я не смог его тут записать
#Сравнить результат с точным значением синуса.
import math
x = float(input("Введите число: "))
s = 0
for i in range(1,6):
  s += ((-1)**(i+1)*x**(2*i-1))/math.factorial(2*i-1)
print("Значние выражения: ",s, "  Значение синуса: ",math.sin(x))