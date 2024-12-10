"""
Main module for the application.

This module initializes the main application window, sets up the canvas,
adds sliders for various parameters, and binds events for canvas zooming.
"""

import tkinter as tk
from numpy import radians
from gui import (initialise_gui,
                 populate_sliders,
                 bind_canvas_zoom_events)
from sandbox import draw_squares, draw_fractal_tree
from datastructures import TreeNodeBase


# Main application window
window_width = 1300
window_height = 700
window = initialise_gui(window_width, window_height)

# place Canvas in the window
canvas_padding_x = 0
canvas_width = window_width - 2 * canvas_padding_x
canvas_height = 535
canvas = tk.Canvas(
    window, bg="white",
    width=canvas_width,
    height=canvas_height
)
canvas.grid(
    row=0, column=0, columnspan=2,
    pady=(0, 0),
    padx=(canvas_padding_x, canvas_padding_x))

# Frame for the sliders
sliders_frame = tk.Frame(window)
sliders_frame.grid(row=1, column=0, columnspan=3, pady=10)

# Create sliders
populate_sliders(sliders_frame, 4)

draw_fractal_tree(
    canvas,
    TreeNodeBase(
        canvas_width/2, canvas_height, 150, radians(-90), 3, 0.7, radians(25), max_depth=7
    )
)
bind_canvas_zoom_events(canvas)

# Run the Tkinter event loop
window.mainloop()