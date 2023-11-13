import tkinter as tk
from math import sin, cos, atan2, sqrt

# Инициализация главного окна приложения
root = tk.Tk()
root.title("Black Hole Animation")

# Параметры для анимации
width, height = 450, 450
center = (width // 2, height // 2)
photon_count = 50
photon_radius = 2  # Радиус фотонов
photon_speed = 3  # Скорость фотонов
gravity_constant = 0.1  # Константа гравитации, начальное значение

# Инициализация холста
canvas = tk.Canvas(root, width=width, height=height, bg="white")
canvas.pack()

# Рисуем черную дыру
black_hole_radius = 40
black_hole_id = canvas.create_oval(
    center[0] - black_hole_radius, center[1] - black_hole_radius,
    center[0] + black_hole_radius, center[1] + black_hole_radius,
    fill="black"
)

# Создаем фотоны
photons = []
for i in range(photon_count):
    x, y = 0, (i + 0.5) * height / photon_count
    photon = canvas.create_oval(
        x - photon_radius, y - photon_radius,
        x + photon_radius, y + photon_radius,
        fill="red"
    )
    photons.append([photon, x, y])

# Функция обновления позиции фотонов
def update_photons():
    for photon_data in photons:
        photon_id, x, y = photon_data
        dx = center[0] - x
        dy = center[1] - y
        distance = sqrt(dx**2 + dy**2)
        angle = atan2(dy, dx)
        force = gravity_constant / distance**2 if distance else 0
        x += (photon_speed + force) * cos(angle)
        y += (photon_speed + force) * sin(angle)
        canvas.coords(photon_id, x - photon_radius, y - photon_radius,
                      x + photon_radius, y + photon_radius)
        photon_data[1], photon_data[2] = x, y
        if x > width or y > height or x < 0 or y < 0:
            photon_data[1], photon_data[2] = 0, (photons.index(photon_data) + 0.5) * height / photon_count

    root.after(50, update_photons)

# Слайдер для изменения силы притяжения черной дыры
def change_gravity(value):
    global gravity_constant
    gravity_constant = float(value)

gravity_slider = tk.Scale(root, from_=0, to=0.5, resolution=0.01, length=400, orient='horizontal', label='Gravity Constant',
                          command=change_gravity)
gravity_slider.pack()
gravity_slider.set(gravity_constant)

update_photons()  # Запускаем анимацию

root.mainloop()  # Запускаем цикл обработки событий Tkinter
 