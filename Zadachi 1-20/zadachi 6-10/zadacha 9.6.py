import random
y = random.randint(1,999)
a = random.randint(10,999)
t = []

for i in range(a):
    t.append(i)
print(t)
for i in range(len(t)):
    if t[i]%2==0:
        t[i]*=y
    else:
        pass
print(t)
