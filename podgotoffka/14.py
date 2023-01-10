a = [(1,3,4), (2,1), (6,), (2,2,2,1)]
b = [a[i][:-1] for i in range(len(a)) if len(a[i])%2 == 0]
print(b)