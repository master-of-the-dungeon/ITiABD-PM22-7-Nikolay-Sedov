import tkinter as tk
import random

def create_fruit():
    x = random.randint(50, 550)
    y = random.randint(50, 550)
    fruit_type = random.choice(fruit_images)
    fruit = canvas.create_image(x, y, anchor=tk.CENTER, image=fruit_type)
    fruits.append((fruit, (x, y)))
    canvas.after(3000, delete_fruit, fruit)
    canvas.after(1000, create_fruit)

def delete_fruit(fruit):
    if fruit in fruits:
        canvas.delete(fruit)
        fruits.remove(fruit)
        reduce_score()

def reduce_score():
    global score
    score -= 1
    if score < 0:
        score = 0
    score_label.config(text=f"Score: {score}")

def collect(event):
    global score
    x, y = event.x, event.y
    for fruit, (fx, fy) in list(fruits):
        if fx - 25 < x < fx + 25 and fy - 25 < y < fy + 25:
            canvas.delete(fruit)
            fruits.remove((fruit, (fx, fy)))
            score += 1
            score_label.config(text=f"Score: {score}")
            break

root = tk.Tk()
root.title("Собери фрукты")

canvas = tk.Canvas(root, width=600, height=600, bg='lightgreen')
canvas.pack()

# Убедитесь, что пути к файлам изображений указаны правильно
apple_img = tk.PhotoImage(file="resized_apple.png")
banana_img = tk.PhotoImage(file="resized_banana.png")
orange_img = tk.PhotoImage(file="resized_orange.png")

fruit_images = [apple_img, banana_img, orange_img]
fruits = []
score = 0

score_label = tk.Label(root, text="Score: 0", font=("Arial", 18))
score_label.pack()

canvas.bind("<Button-1>", collect)

create_fruit()

root.mainloop()
