y1 = []
y2 = []
for i in range(-100,100):
    if i<=2:
        y2.append(3*(i**2)-2*i-1)
    else:
        y1.append(2*(i**3)-2*i+1)
print(y1)
print(y2)
c = list(set(y1) & set(y2))
print(c)
