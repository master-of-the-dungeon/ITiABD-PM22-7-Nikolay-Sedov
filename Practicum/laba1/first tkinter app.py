import tkinter as tk
import math


class MovingDotApp:
    def __init__(self):
        self.angle = 0
        self.speed = 1
        self.direction = 1  # 1 for clockwise, -1 for counter-clockwise

        # Создание основного окна
        self.root = tk.Tk()
        self.root.title("Moving Dot on Circle")
        self.root.geometry("600x700")  # увеличиваем высоту, чтобы поместить кнопки

        # Создание области для рисования
        self.canvas = tk.Canvas(self.root, width=600, height=600, bg="white")
        self.canvas.pack()

        # Радиус окружности
        self.radius = 200

        # Рисование окружности в центре
        self.canvas.create_oval(300 - self.radius, 300 - self.radius, 300 + self.radius, 300 + self.radius)

        # Начальные координаты точки на окружности
        self.x = 300 + self.radius
        self.y = 300

        # Создание и начальное отображение точки
        self.dot = self.canvas.create_oval(self.x - 5, self.y - 5, self.x + 5, self.y + 5, fill="red", outline="blue")

        # Кнопки для изменения скорости
        self.speed_up_btn = tk.Button(self.root, text="Увеличить скорость", command=self.speed_up)
        self.speed_up_btn.pack(side=tk.LEFT, padx=20)

        self.speed_down_btn = tk.Button(self.root, text="Уменьшить скорость", command=self.speed_down)
        self.speed_down_btn.pack(side=tk.RIGHT, padx=20)

        # Кнопки для изменения направления
        self.clockwise_btn = tk.Button(self.root, text="По часовой", command=self.set_clockwise)
        self.clockwise_btn.pack(side=tk.LEFT, padx=20)

        self.counter_clockwise_btn = tk.Button(self.root, text="Против часовой", command=self.set_counter_clockwise)
        self.counter_clockwise_btn.pack(side=tk.RIGHT, padx=20)

        self.root.after(50, self.update_dot_position)
        self.root.mainloop()

    def update_dot_position(self):
        # Вычисляем новые координаты точки на окружности
        self.x = 300 + self.radius * math.cos(math.radians(self.angle))
        self.y = 300 + self.radius * math.sin(math.radians(self.angle))

        # Обновляем координаты точки на холсте
        self.canvas.coords(self.dot, self.x - 5, self.y - 5, self.x + 5, self.y + 5)

        self.angle += self.speed * self.direction
        if self.angle >= 360:
            self.angle -= 360
        elif self.angle < 0:
            self.angle += 360

        self.root.after(50, self.update_dot_position)

    def speed_up(self):
        self.speed += 10

    def speed_down(self):
        if self.speed > 10:
            self.speed -= 10

    def set_clockwise(self):
        self.direction = 1

    def set_counter_clockwise(self):
        self.direction = -1


if __name__ == "__main__":
    app = MovingDotApp()
