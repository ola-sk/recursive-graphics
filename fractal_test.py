from tkinter import *
from fractal_plot_funcs import fractal_canopy
from helper_funcs import generate_gradient

import numpy as np
tk = Tk()

# resize window to 500 x 800
tk.geometry("500x700")

canvas = Canvas(bg="white", height=500, width=500)
canvas.grid(row=0, column=0)

# generate a gradient from brown to green

gradient_list = generate_gradient(["#8B4513", "#228B22"], 10)

fractal_canopy(canvas, 250, 500, n_iters=7, init_length=200, n_splits=3, angle_delta=90, off_angle=5, length_ratio=0.5, wave_amp=5, width=20, width_ratio=0.6, color=gradient_list)



tk.mainloop()