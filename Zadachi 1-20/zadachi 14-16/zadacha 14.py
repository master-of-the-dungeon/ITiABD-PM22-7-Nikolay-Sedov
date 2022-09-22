import math
def TypeTrl(A, B, C):
  a = round(math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2 + (B[2] - A[2])**2), 4)
  b = round(math.sqrt((C[0] - B[0])**2 + (C[1] - B[1])**2 + (C[2] - B[2])**2), 4)
  c = round(math.sqrt((A[0] - C[0])**2 + (A[1] - C[1])**2 + (A[2] - C[2])**2), 4)
  if a == b == c:
    print("Равносторонний")
  elif a == b or b == c or a == c:
    print("Равнобедренный")  
  elif (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == a**2 + b**2):
    print("Прямоугольный")
  else:
    print("Обычный")