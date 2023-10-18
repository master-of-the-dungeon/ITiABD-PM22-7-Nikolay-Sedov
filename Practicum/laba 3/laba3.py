import tkinter as tk
from tkinter import ttk

class BlackHoleDiagram(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Black Hole Diagram")
        self.geometry("600x500")

        self.canvas = tk.Canvas(self, bg="white", width=500, height=400)
        self.canvas.pack(pady=20)

        # Черная дыра в центре
        self.canvas.create_oval(200, 150, 300, 250, fill="black")

        # Разные слои вокруг черной дыры
        colors = ["#444", "#777", "#AAA", "#DDD"]
        sizes = [(175, 125, 325, 275), (150, 100, 350, 300), (125, 75, 375, 325), (100, 50, 400, 350)]
        for i, color in enumerate(colors):
            self.canvas.create_oval(sizes[i], fill=color)

        # Горизонтальная линия
        self.canvas.create_line(0, 200, 500, 200)

        # Шкала справа
        for i in range(25, 376, 25):
            self.canvas.create_line(480, i, 500, i, fill="red")
            if i % 50 == 0:  # Большие деления на шкале
                self.canvas.create_line(470, i, 500, i, fill="red")

if __name__ == "__main__":
    app = BlackHoleDiagram()
    app.mainloop()
