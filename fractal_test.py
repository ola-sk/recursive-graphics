"""
This script demonstrates how to draw a fractal canopy
using the fractal_canopy function from fractal_funcs.py.
The fractal canopy is drawn on a tkinter canvas.
The color of the canopy is generated using a gradient
from brown to green. The gradient is generated using the
generate_gradient function from helper_funcs.py.
The fractal canopy is drawn with various parameters such as
the number of iterations, initial length, number of splits,
angle delta, and wave amplitude.
"""

from tkinter import Tk, Canvas
from fractal_funcs import fractal_canopy
from helper_funcs import generate_gradient

tk = Tk()

# resize window to 500 x 700
tk.geometry("500x700")

# create a canvas
canvas = Canvas(bg="white", height=500, width=500)
canvas.grid(row=0, column=0)

# generate a gradient from brown to green
gradient_list = generate_gradient("#8B4513", "#228B22", 10)

# draw a fractal canopy
fractal_canopy(canvas, 250, 500,
               n_iters=7, init_length=200,
               n_splits=4, angle_delta=180,
               off_angle=0, length_ratio=0.3,
               wave_amp=5, width=20,
               width_ratio=0.6, color=gradient_list)

tk.mainloop()
