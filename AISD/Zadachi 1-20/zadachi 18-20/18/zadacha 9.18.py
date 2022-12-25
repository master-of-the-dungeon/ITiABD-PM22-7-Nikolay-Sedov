f18 = open('18.txt', 'r', encoding="utf8")
s = f18.readline()
a = ''
while s:
    n = (50 - len(s)) // 2 + len(s) % 2
    print(' ' * n, s, sep='')
    s = f18.readline()

