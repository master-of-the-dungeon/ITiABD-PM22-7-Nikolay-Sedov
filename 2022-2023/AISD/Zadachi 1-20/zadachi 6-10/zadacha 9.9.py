alf = 'abcdefghijklmnopqrstuvwqyzабвгдеёжзиклмнопрстуфхцчшщьыъэюя'
str = 'A6gh7IJhыйжопаыыы'
counter = 1
for i in range(len(str)):
    if str[i] in alf:
        counter+=1
print(counter)