def del_num(text):
    rtrn = ''
    for i in text:
        if not i.isdigit():
            rtrn += i
    return rtrn

def a():
    no_digits = []
    file = open('sample 1.txt', 'r')
    nums= '1234567890'
    t = []
    for line in file:
        t.append(line[:-1])
    file.close()
    print(t)
    for i in range(len(t)):
        no_digits.append(del_num(t[i]))
    f = open('sample 1w.txt', 'w')
    for i in range(len(no_digits)):
        f.write(no_digits[i] + '\n')




def b():
    a = ''
    file = open('sample 2-3.txt','r')
    for line in file:
        a+=str((line)[:-1])
    print(a)
    print(len(a))
def c():

    a = []
    file = open('sample 2-3.txt','r')
    for line in file:
        a.append(str((line)[:-1]))
    print(len(a))
a()