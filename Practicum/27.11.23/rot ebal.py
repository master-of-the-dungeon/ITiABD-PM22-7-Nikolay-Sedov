import tkinter
import random
import time

score = 0
speed = 5
fruit = []  # список для выбора появляющихся фруктов

window = tkinter.Tk()
window.title('Собери фрукты')
h = 800
c = tkinter.Canvas(window, width=800, height=h, bg='#9999FF')
c.pack()

# Добавляем изображение корзинки
basket_img = tkinter.PhotoImage(file='basket.png    ')
basket = c.create_image(400, h-50, image=basket_img)  # Создаем корзинку

def func1():
    global speed
    speed += 5

def move_basket(event):
    x, y = c.coords(basket)
    if event.keysym == 'Left':
        c.move(basket, -20, 0)
    elif event.keysym == 'Right':
        c.move(basket, 20, 0)

# Привязываем клавиши к функции перемещения корзинки
window.bind('<Left>', move_basket)
window.bind('<Right>', move_basket)

# создаем кнопку 
but = tkinter.Button(text="Увеличь скорость", command=func1)
c.create_window((6, 217), anchor="nw", window=but)
t = c.create_text(150, 20, font='Arial 20', fill='black', text='ОЧКИ: ' + str(score))

def func():
    global score
    for i in range((h-100)//speed):
        c.move(id_fr, 0, speed)
        fruit_x, fruit_y = c.coords(id_fr)
        basket_x, basket_y = c.coords(basket)
        if abs(fruit_x - basket_x) < 50 and abs(fruit_y - basket_y) < 50:  # Проверка на столкновение с корзинкой
            score += 1
            c.itemconfig(t, text='ОЧКИ: ' + str(score))
            c.delete(id_fr)
            return
        window.update()
        time.sleep(0.02)

def click_fruit(event):
    global score
    position = c.coords(id_fr) 
    if abs(event.x - position[0]) <= 25 and abs(event.y - position[1]) <= 25:
        score += 1
        c.itemconfig(t, text='ОЧКИ: ' + str(score))
        c.delete(id_fr)

fruit_images = ['ananas.png', 'banana.png', 'apple.png', 'orange.png']
fruit = [tkinter.PhotoImage(file=image_file) for image_file in fruit_images]

c.bind_all('<Button-1>', click_fruit)

while True:
    i = random.randint(0, 3)
    x = random.randint(100, 700)
    y = 0
    
    id_fr = c.create_image(x, y, image=fruit[i])
    func()

window.mainloop()
