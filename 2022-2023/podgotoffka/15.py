a = 'Eeny, meeny, miney, moe; Catch a tiger by his toe.'
b = []
for i in range(len(a)):
    b.append(a.split(','))
print(b)