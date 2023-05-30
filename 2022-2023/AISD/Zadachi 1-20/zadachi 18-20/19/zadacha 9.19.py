import math
file = open('text.txt','r')
a = []
modmax = -9999999999
for line in file:
    a.append(float(line))
print(a)
for i in range(0,len(a),2):
    # print(a[i])
    if math.fabs(a[i])>modmax:
        modmax = math.fabs(a[i])
print('МАКС   ',modmax)

