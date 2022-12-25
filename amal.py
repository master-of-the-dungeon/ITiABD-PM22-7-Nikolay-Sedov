import random
a = {}
c = []
d = []
alf = 'abcdefghilklmnopqrstuvwkyz'
for i in range(random.randint(1,19)):
    a[alf[i]] = i
print('Начальный словарь: ',a)
k = int(input('Введите символ для разделения: '))

if k<len(a):
    s =list(map(lambda x:{x[0]:x[1]},a.items() ))
print(s)


