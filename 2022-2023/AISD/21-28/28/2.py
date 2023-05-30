A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
M = len(A)
for i in range(M):
    for j in range(i + 1, M):
        A[i][j], A[j][i] = A[j][i], A[i][j]
for i in range(M):
    A[i] = A[i][::-1]
print(A)
