import random
r = random.randint(1,999)
t  = []
f = []
for i in range(r):
    t.append(i)
for i in range(len(t)):
    if t[i]<15:
        f.append(t[i])
f.sort()
print(f)