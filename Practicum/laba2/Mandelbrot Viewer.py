import tkinter as tk
from PIL import Image, ImageTk, ImageDraw


def compute_mandelbrot(width, height, x_center, y_center, x_width, y_width, max_iterations):
    x_step = x_width / width
    y_step = y_width / height
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    for x in range(width):
        for y in range(height):
            zx, zy = x * x_step + x_center - x_width / 2, y * y_step + y_center - y_width / 2
            c = zx + zy * 1j
            z = c
            for i in range(max_iterations):
                if abs(z) > 2.0:
                    break
                z = z * z + c

            # Convert iteration number to color
            r, g, b = i % 8 * 32, i % 16 * 16, i % 32 * 8
            draw.point((x, y), fill=(r, g, b))

    return image


class MandelbrotViewer:
    def __init__(self, master):
        self.canvas = tk.Canvas(master, width=600, height=600, bg="white")
        self.canvas.pack(pady=20, padx=20)

        self.canvas.bind("<Button-1>", self.zoom)

        self.x_center = 0
        self.y_center = 0
        self.width = 4
        self.height = 4

        self.redraw()

    def zoom(self, event):
        self.width /= 2
        self.height /= 2
        self.x_center = (event.x / 600) * self.width + self.x_center - self.width / 2
        self.y_center = (event.y / 600) * self.height + self.y_center - self.height / 2
        self.redraw()

    def redraw(self):
        image = compute_mandelbrot(600, 600, self.x_center, self.y_center, self.width, self.height, 1000)
        self.tk_image = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)


root = tk.Tk()
root.title("Mandelbrot Viewer")
app = MandelbrotViewer(root)
root.mainloop()
