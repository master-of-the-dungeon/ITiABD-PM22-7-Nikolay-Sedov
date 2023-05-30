A = [1, 2, 3, 4, 5]
B = [0] * len(A)
for k in range(len(A)):
    B[k] = sum(A[:k+1]) / (k+1)
print(B)
