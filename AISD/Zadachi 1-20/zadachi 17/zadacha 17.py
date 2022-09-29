file = open('sample 1.txt', 'r')
nums= '1234567890'
t = []
for line in file:
    t.append(line[:-1])
file.close()
print(t)
for line in range(len(t)):
    for i in range(len(t[line])):
        if t[line] in nums:
            line = line.replace(line[i],'',1)
print(t)



