from random import *
import math
n = randint(1,9999)
x = float(input())
c = 0
while n!=0:
    c+=math.sin(n)
    n-=1
print(c)
