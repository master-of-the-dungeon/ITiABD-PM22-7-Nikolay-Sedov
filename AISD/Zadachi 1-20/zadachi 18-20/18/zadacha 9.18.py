file = open('/Users/nikolaysedoff/PycharmProjects/ITiABD-PM22-7-Nikolay-Sedov/AISD/Zadachi 1-20/zadachi 18-20/18/text.txt', 'r')
s = file.readline()
a = ''
while s:
    n = (50 - len(s)) // 2 + len(s) % 2
    print(' ' * n, s, sep='')
    s = file.readline()

