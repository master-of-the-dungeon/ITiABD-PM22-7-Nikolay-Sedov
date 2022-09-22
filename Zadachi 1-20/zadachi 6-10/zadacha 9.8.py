import random
import numpy
counter = 0
m = random.randint(1, 10)
n = random.randint(1, 10)
matrix = [[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        matrix[i][j] = random.randint(1,10)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end = ' ')
    print()


t = list(map(list,zip(*matrix)))

for i in range(len(t)):
    srarif = numpy.mean(t[i])
    for j in range(len(t[i])):
        if t[i][j]>srarif:
            counter+=1
    print('Кол-во элементов в столбце №'+str(i)+': ', counter)
    counter=0



