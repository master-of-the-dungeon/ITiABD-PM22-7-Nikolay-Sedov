a = [['E', 'e', 'n', 'y'], ['m', 'e', 'e', 'n', 'y'], ['m', 'i', 'n', 'e', 'y'], ['m', 'o', 'e']]
c = ''
for i in range(len(a)):
    for j in range(len(a[i])):
        c+=(''.join(a[i]))
        break
    c+=','
c = c[:-1]
print(c)