a = 'Хатуев Амаль Сафарбиевич'
a = a.split()
print(a)
namesurnamelastname = {}
for i in range(len(a)):
    namesurnamelastname[i] = a[i]
print(namesurnamelastname)