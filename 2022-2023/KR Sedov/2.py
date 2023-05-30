import random
file = open('b.txt','w')
a = random.randint(10,50)
b = []
for i in range(a):
    file.write(str(i))
    file.write('\n')
file.close()
file2 = open('b.txt','r')
for line in file2:
    b.append(int(line))
print('Начальный список: ',b)
c = []
g = []
f = []
halflen = 0
if len(b)%2==0:
    for i in range(0,len(b)//2):
        c.append(b[i])
    b.reverse()
    for i in range(0,len(b)//2):
        g.append(b[i])
    for j in range(len(c)):
        f.append(c[j])
        f.append(g[j])
if len(b)%2!=0:
    for i in range(0,(len(b)//2)):
        c.append(b[i])
    b.reverse()
    for i in range(0,len(b)//2+1):
        g.append(b[i])
    for j in range(len(c)):
        f.append(c[j])
        f.append(g[j])
    f.append(g[j+1])
print('Финальный список: ',f)