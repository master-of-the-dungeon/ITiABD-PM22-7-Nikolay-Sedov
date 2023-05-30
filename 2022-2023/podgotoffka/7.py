a = {(2,4):'a', (1,11,1):'b', (2,3):'c'}
b = {max(x):y for x,y in zip(a.keys(),a.values())}
print(b)
