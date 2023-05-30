g = {(2,4):'a', (1,11,1):'b', (12,3):'c'}
b = {min(x):y for x,y in zip(g.keys(),g.values())}
print(b)
