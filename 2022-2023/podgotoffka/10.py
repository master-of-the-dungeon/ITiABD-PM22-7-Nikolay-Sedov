a = [2,4,1,3]
b = ['a','b','c','d']
res = {a[i]:b[i]*a[i] for i in range(len(a))}
print(res)