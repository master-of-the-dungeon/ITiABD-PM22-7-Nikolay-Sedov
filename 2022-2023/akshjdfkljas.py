import numpy as np
Rook = input('Введите координаты ладьи: ').split()
for i in range(len(Rook)):
    Rook[i] = int(Rook[i])
a = np.zeros([8, 8], dtype=np.int8)
a[Rook[0]], a[:, Rook[1]] = 1, 1

for i in range(8):
    for k, j in enumerate(a[i]):
        if i == Rook[0] and k == Rook[1]:
            print('*', end=' ')
        else:
            if j == 1:
                print('!', end=' ')
            else:
                print('.', end=' ')
    print()