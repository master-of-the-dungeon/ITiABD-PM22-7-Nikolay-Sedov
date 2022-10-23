file = open('text.txt', 'r')
f = open('textw.txt', 'w')
s = file.readline()
a = ''
while s:
    n = (50 - len(s)) // 2 + len(s) % 2
    print(' ' * n, s, sep='')
    # f.write(' ' * n, s)
    s = file.readline()

