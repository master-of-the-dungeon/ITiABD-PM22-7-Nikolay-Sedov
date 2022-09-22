import random
a = random.randint(1,10)
x = random.randint(1,10)
y = random.randint(1,10)
b = random.randint(1,10)

def odin_kg_kazhdogo_i_voskolko_raz(a,b,x,y):
    shokolad = a/x
    iriski = b/y
    voskolko_raz = shokolad/iriski
    print("Шоколад стоит: ", shokolad," гривен за кило")
    print("Ириски стоят: ", iriski," гривен за кило")
    print("Шоколад дороже в ",voskolko_raz," раз")

odin_kg_kazhdogo_i_voskolko_raz(a,b,x,y)