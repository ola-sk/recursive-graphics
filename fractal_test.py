from tkinter import *
from fractal_plot_funcs import fractal_canopy
from helper_funcs import generate_gradient
import numpy as np

tk = Tk()

# resize window to 500 x 700
tk.geometry("500x700")

# create a canvas
canvas = Canvas(bg="white", height=500, width=500)
canvas.grid(row=0, column=0)

# generate a gradient from brown to green
gradient_list = generate_gradient("#8B4513", "#228B22", 10)

# draw a fractal canopy
fractal_canopy(canvas, 250, 500, n_iters=7, init_length=200, n_splits=4, angle_delta=180, off_angle=0, length_ratio=0.3, wave_amp=5, width=20, width_ratio=0.6, color=gradient_list)

tk.mainloop()