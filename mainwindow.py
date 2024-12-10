"""
Main module for the application.

This module initializes the main application window, sets up the canvas,
adds sliders for various parameters, and binds events for canvas zooming.
"""

import tkinter as tk

from numpy import radians

from datastructures import TreeNodeBase
from gui import (initialize_gui,
                 populate_sliders,
                 draw_fractal_tree,
                 bind_canvas_zoom_events)
from state import sliders_init_data

# Main application window
window_width = 1300
window_height = 700
window = initialize_gui(window_width, window_height)

# place Canvas in the window
canvas_padding_x = 0
canvas_width = window_width - (2 * canvas_padding_x)
canvas_height = 0.85 * window_height
canvas = tk.Canvas(
    window, bg="white",
    width=canvas_width,
    height=canvas_height
)
canvas.grid(
    row=0, column=0, columnspan=2,
    pady=(0, 0),
    padx=(canvas_padding_x, canvas_padding_x)
)

# Frame for the sliders
sliders_frame = tk.Frame(window)
sliders_frame.grid(row=1, column=0, columnspan=3, pady=10)

# Initialize and place sliders for changing the parameters of the fractal tree
sliders = populate_sliders(sliders_frame, canvas, sliders_init_data, 5)

# Initialize the tree. The Tree is stored as a static property in the TreeNodeBase class. An internal method of the
# class takes care of saving this generated tree as state. You can access it using
# TreeNodeBase.get_current_tree_root(); update it using TreeNodeBase.set_current_tree_root(new_tree) or
# TreeNodeBase.update_tree(old_tree, **kwargs) where kwargs are keyword parameters that the new tree should have
# changed (the rest of tree parameters would come from the `old_tree`).
# noinspection PyUnresolvedReferences
initial_values = {slider.modifies_parameter: slider.get() for slider in sliders}

TreeNodeBase(
    start_x=canvas_width / 2,
    start_y=canvas_height,
    length=initial_values.get("length", 150),
    angle=radians(initial_values.get("angle", -90)),
    num_children=int(initial_values.get("num_children", 3)),
    length_scale=initial_values.get("length_scale", 0.7),
    delta_angle=radians(initial_values.get("delta_angle", 25)),
    max_depth=int(initial_values.get("max_depth", 7))
)
draw_fractal_tree(canvas, TreeNodeBase.get_current_tree_root())

bind_canvas_zoom_events(canvas)

# Run the Tkinter event loop
window.mainloop()