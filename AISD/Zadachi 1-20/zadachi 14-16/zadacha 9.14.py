import math
def raschet(a,b,c):
  def xxy(x, y):
    if int(x[0]) > int(y[0]):
      ab = int(x[0]) - int(y[0])
      return ab
    elif int(x[0]) < int(y[0]):
      ab = int(x[0]) - int(y[0])
      return ab
    else:
      return 0


  def yxy(x, y):
    if int(x[1]) > int(y[1]):
      ab = int(x[1]) - int(y[1])
      return ab
    elif int(x[1]) < int(y[1]):
      ab = int(x[1]) - int(y[1])
      return ab
    else:
      return 0

  def pif(x, y):
    return math.sqrt((xxy(x, y) ** 2) + (yxy(x, y) ** 2))

  a1 = pif(a, b)
  b1 = pif(b, c)
  c1 = pif(a, c)
  return a1,b1,c1

a = input('Введите координаты первой точки через пробел: ').split()
b = input('Введите координаты второй точки через пробел: ').split()
c = input('Введите координаты третьей точки через пробел: ').split()

print(raschet(a,b,c))


if raschet(a,b,c)[0] == raschet(a,b,c)[1] == raschet(a,b,c)[2]:
  print("Равносторонний")
elif raschet(a,b,c)[0] == raschet(a,b,c)[1] or raschet(a,b,c)[1] == raschet(a,b,c)[2] or raschet(a,b,c)[0] == raschet(a,b,c)[2]:
  print("Равнобедренный")
elif (raschet(a,b,c)[0]**2 == raschet(a,b,c)[1]**2 + raschet(a,b,c)[2]**2) or (raschet(a,b,c)[1]**2 == raschet(a,b,c)[0]**2 + raschet(a,b,c)[2]**2) or (raschet(a,b,c)[2]**2 == raschet(a,b,c)[0]**2 + raschet(a,b,c)[1]**2):
  print("Прямоугольный")
else:
  print("Обычный")