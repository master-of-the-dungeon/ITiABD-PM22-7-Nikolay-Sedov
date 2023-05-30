c = {'a':1, 'b':3, 'c':4, 'd':3}
c = {x : y for x,y in zip(c.values(),c.keys()) if list(c.values()).count(x)==1}
print(c)