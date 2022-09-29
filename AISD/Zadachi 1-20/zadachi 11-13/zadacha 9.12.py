import collections
def a():
    a = tuple('1234567891012345672356798765433425')
    print(a)
    povt = collections.Counter(a)
    print(povt)
def b():
    b = [1,2,3,4,5,'ff','sdfsddgsf',(1,2,3,1,2,4,5,6),1213,[1,2,3],6544654,'dfgdsgd',"gjfljghsdl"]
    for i in range(len(b)):
        print(b[i])
        if b[i] is tuple:
            print("Я нашел кортеж!")
            print(b[i])
b()