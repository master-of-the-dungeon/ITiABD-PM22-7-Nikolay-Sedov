import random
a = []
b = []
counter = 0
for i in range(5):
    a.append(random.randint(1, 10))
for i in range(5):
    b.append(random.randint(1, 10))

for i in range (len(a)):
    if a.count(a[i]) == 1 and b.count(a[i])==0:
        counter+=1
for i in range(len(b)):
    if a.count(b[i]) == 0 and b.count(b[i]) == 1:
        counter += 1
print("Списки А и Б: ",a,b)
print("Кол-во уникальных элементов: ",counter)
