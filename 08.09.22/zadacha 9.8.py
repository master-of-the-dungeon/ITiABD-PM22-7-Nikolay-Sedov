import random
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
