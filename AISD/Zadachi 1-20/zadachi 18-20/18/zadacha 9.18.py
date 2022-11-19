file = open('/Users/nikolaysedoff/PycharmProjects/ITiABD-PM22-7-Nikolay-Sedov/AISD/Zadachi 1-20/zadachi 18-20/18/text.txt', 'r')
f = open('/Users/nikolaysedoff/PycharmProjects/ITiABD-PM22-7-Nikolay-Sedov/AISD/Zadachi 1-20/zadachi 18-20/18/textw.txt', 'w')
s = file.readline()
a = ''
while s:
    n = (50 - len(s)) // 2 + len(s) % 2
    print(' ' * n, s, sep='')
    f.write(' ' * n, s)
    s = file.readline()

