a = {2:4, 3:2, 12:6, 5:4, 1:3}
b = list({x+y:y for x,y in zip(a.keys(),a.values()) if (x+y)%2!=0})
print(b)