from tkinter import *
import time
window = Tk()
window.title("Тест")
window.geometry("1920x1080")
c  = Canvas(window, width=800, height=800,bg = 'black')
rect = c.create_rectangle(200,800,400,600, outline='purple')
rect2 = c.create_rectangle(250,600,350,500, outline='purple')
rect3 = c.create_rectangle(280,500,320,400, outline='purple')
# while True:
#     c.move(rect3, 2, 2)
#     window.update()
#     time.sleep(1)
c.pack()
window.mainloop()