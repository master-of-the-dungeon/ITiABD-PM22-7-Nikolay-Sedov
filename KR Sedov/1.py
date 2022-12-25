a = [8,2]
b = {'abc':4,'def':9}
g = []
c = {}
counter = 0
for keys,values in b.items():
    g.append(dict(zip(keys,str(values))))
print(g)
if len(a) == len(g):
    for i in range(len(a)):
        c[a[i]] = g[i]
    print(c)
elif len(a)!=len(g):
    print('Объединение невозможно')

