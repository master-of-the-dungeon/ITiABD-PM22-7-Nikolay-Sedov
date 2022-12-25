import random
import sympy as sp
import numpy as np
import random as ran
t = open('1.txt','w')
k = int(input())
a = []
for i in range(k):
    M = str(sp.Matrix(3,3,[
        random.randint(2,10), random.randint(2,10), random.randint(2,10),
        random.randint(2,10), random.randint(2,10), random.randint(2,10),
        random.randint(2,10), random.randint(2,10), random.randint(2,10)
    ]))
    print(M)
    a.append(M)
    t.write(M)
    t.write('\n')

t.close()
# a = open('1.txt','r')
b = open('2.txt','w')
c = open('3.txt','w')
e = []
for line in a:
    e.append(eval(line))
print(e)
# for i in range(len(a)):
#     pass
# print(a)
    # if a[i] == sp.Transpose(a[i]):
    #     print("Хуй")
    # y.append(e[i])
    # print(y)
    # f = sp.Matrix(list(e[i]))
    # print(f)
    # if f == sp.Transpose(f):
    #     print(e[i])




