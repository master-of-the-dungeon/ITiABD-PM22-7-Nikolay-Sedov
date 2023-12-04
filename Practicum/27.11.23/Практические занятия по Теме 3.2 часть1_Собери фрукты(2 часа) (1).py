''' Задание 1. Написать игру "Собери фрукты", обладающую следующим функционалом:
- Создать плоскость рисования размером 800х800, выбрать фон плоскости рисования
- Разместить на поле ОЧКИ и кнопку "Увеличить скорость" падения фруктов
- Осуществить движение 4х фруктов(яблоко, банан, апельсин, ананас) сверху вниз, имитируя падение
- При достижении фруктом низа экрана, движение фрукта должно заканчиваться
- Разработать функцию "Клик левой кнопкой мыши", которая при клике на фрукт увеличивает очки и делает
фрукт исчезнувшим
- Для  отображения изменений по сумме очков использовать метод itemconfigure()
- Разработать функцию по увеличению скорости падения фруктов.'''

import tkinter
import random
import time


score=0
speed=5
fruit=[] #список для выбора появляющихся фруктов
fruit_mass=[]#список из 4х появившихся фруктов

window=tkinter.Tk()
window.title('Собери фрукты')
h=800
c=tkinter.Canvas(window,width=800, height=h,bg='#9999FF')
c.pack()

def func1():
    global speed
    speed=speed+5
    

#создаем кнопку 
but = tkinter.Button(text="Увеличь скорость", command=func1)
# Привязываем созданные виджеты (but) к канвасу окна.
c.create_window((6, 217), anchor="nw", window=but)
t=c.create_text(150,20,font='Arial 20',fill='black',text='ОЧКИ: '+str(score))


def func():
    for i in range((h-100)//speed):# минус 100,т.к. каждый фрукт примерно 100х100 пикселей
                                    #а положение прорисовки фрукта считается по левому верхнему углу
        c.move(id_fr,0,speed)
        window.update()
        time.sleep(0.02)
        
def click_fruit(event):
    global score
    print(event.x,event.y)
    position = c.coords(id_fr) # получение координат объекта
    print(position)
    if abs(event.x-position[0])<=25 and abs(event.y-position[1])<=25:
        score=score+1
        c.itemconfig(t, text='ОЧКИ: '+str(score)) #именяем очки
        c.delete(id_fr)
        
    
while True:
    img1=tkinter.PhotoImage(file='ananas.png')
    fruit.append(img1)
    img2=tkinter.PhotoImage(file='banana.png')
    fruit.append(img2)
    img3=tkinter.PhotoImage(file='apple.png')
    fruit.append(img3)
    img4=tkinter.PhotoImage(file='orange.png')
    fruit.append(img4)
    
    c.bind_all('<Button-1>',click_fruit)#клик левой кнопкой мыши

    i=random.randint(0,3)#какой фрукт выпадет
    x=random.randint(100,700)#появляются сверху
    y=0
    
    id_fr=c.create_image(x,y,image=fruit[i]) 
    func()

    

window.mainloop()





