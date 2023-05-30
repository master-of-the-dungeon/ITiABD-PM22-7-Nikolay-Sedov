# ваш код здесь

ivan = input('Введите зарплату ивана и его траты через пробел:').split()
oleg = input('Введите зарплату олега и его траты через пробел: ').split()
semen = input('Введите зарплату семена и его траты через пробел: ').split()
srok = {'Ivan':0,'Oleg':0,'Semen':0}
tsel = 1000000
shetchik = 0
while tsel!=0:
    tsel-=int(ivan[0])
    shetchik +=1
srok['Ivan'] = shetchik
shetchik = 0
tsel = 1000000
while tsel!=0:
    tsel-=int(oleg[0])
    shetchik +=1
srok['Oleg'] = shetchik
shetchik = 0
tsel = 1000000
while tsel!=0:
    tsel-=int(semen[0])
    shetchik +=1
srok['Semen'] = shetchik
print(srok)