import numpy
a = {(2,4):'a', (1,1,1):'b', (2,3):'c'}
a = {sum(x)/len(x) : y for x,y in zip(a.keys(),a.values())}
print(a)