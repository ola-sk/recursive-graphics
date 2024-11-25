from tkinter import *
from fractal_plot_funcs import fractal_canopy
import numpy as np
tk = Tk()

# resize window to 500 x 800
tk.geometry("500x700")

canvas = Canvas(bg="white", height=500, width=500)
canvas.grid(row=0, column=0)

# dr

fractal_canopy(canvas, 250, 500, n_iters=5, init_length=100, n_splits=5, angle_delta=30)



tk.mainloop()