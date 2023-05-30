import random
path1 = str(input('Path 1: '))
path2 = str(input('Path 2: '))

k = int(input('k: '))
m = int(input('m: '))
n = int(input('n: '))
l = int(input('l: '))
def matrix_multiply(data1, data2):
    data3 = [[None for __ in range(l)] for __ in range(m)]

    for i in range(m):
        for j in range(l):
            data3[i][j] = sum(data1[i][kk] * data2[kk][j] for kk in range(n))
    return data3

with open(path1, 'w') as f:
    for j in range(k):
        mat = [[0] * n for i in range(m)]

        for i in range(m):
            for j in range(n):
                f.write(str(random.randint(1,9)))
                f.write(' ')
            f.write('\n')
        f.write('\n')

with open(path2, 'w') as f:
    for j in range(k):
        mat = [[0] * l for i in range(n)]

        for i in range(n):
            for j in range(l):
                f.write(str(random.randint(1,9)))
                f.write(' ')
            f.write('\n')
        f.write('\n')

with open(path1) as f1:
    with open(path2) as f2:
        with open('new_data.txt', 'w') as f3:
            new_data2 = [list(map(int, row.split())) for row in f2.readlines()]
            new_data1 = [list(map(int, row.split())) for row in f1.readlines()]

            a = 0
            data2 = [[[] for g in range(l - l)] for b in range(k)]
            data1 = [[[] for g in range(l - l)] for b in range(k)]
            for row in new_data2:
                if not row:
                    a += 1
                    continue
                data2[a].append(row)
            a = 0
            for row in new_data1:
                if not row:
                    a += 1
                    continue
                data1[a].append(row)
            for x in range(len(data1)):
                data3 = matrix_multiply(data1[x],data2[x])
                for i in range(m):
                    for j in range(n):
                        f3.write(str(data1[x][i][j]))
                        f3.write(' ')
                    f3.write('\n')
                f3.write('*')
                f3.write('\n')
                for i in range(n):
                    for j in range(l):
                        f3.write(str(data2[x][i][j]))
                        f3.write(' ')
                    f3.write('\n')
                f3.write('=')
                f3.write('\n')
                for i in range(m):
                    for j in range(l):
                        f3.write(str(data3[i][j]))
                        f3.write(' ')
                    f3.write('\n')
                f3.write('\n')


