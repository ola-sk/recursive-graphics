"""
Module for creating sliders in the GUI.

Contains functions for creating sliders given their parameters, including some custom ones.
in the GUI, which can be used to control the parameters of the fractal tree displayed on the canvas.
It also defines the event handlers as well as the generator for the grid layout of the sliders.

A populate_sliders function is provided to add sliders for different parameters to the sliders frame.
"""
import tkinter as tk


def create_slider(
        parent: tk.Widget, label: str, from_: int | float, to: int | float, row: int, column: int
) -> tk.Scale:
    """
    Create a slider and add it to the parent widget.

    Parameters:
        parent (tk.Widget): The parent widget to which the slider will be added.
        label (str): The label for the slider.
        from_ (int or float): The starting value of the slider.
        to (int or float): The ending value of the slider.
        row (int): The row position in the grid layout.
        column (int): The column position in the grid layout.

    Returns:
        tk.Scale: The created slider widget.
    """
    slider = tk.Scale(parent, label=label, from_=from_, to=to, orient=tk.HORIZONTAL, length=120)
    slider.grid(row=row, column=column, padx=25, pady=3)
    return slider


def column_sequence_generator(num_columns: int):
    """
    Generator function that yields a repeating sequence of numbers from 1 to 4.
    """
    row = 0
    while True:
        for column in range(0, num_columns):
            yield row, column
        row += 1


def populate_sliders(sliders_frame: tk.Frame, num_columns: int = 2) -> None:
    """
    Add sliders for different parameters to the sliders frame.

    Parameters:
        sliders_frame (tk.Frame): The frame to which the sliders will be added.
        num_columns (int): The number of columns in the grid layout of the sliders frame.
    """
    for i in range(num_columns):
        sliders_frame.columnconfigure(i, weight=1)

    column_sequence = column_sequence_generator(num_columns)

    sliders = [
        ("Angle Offset", -45, 45),
        ("Angle Size", 0, 180),
        ("Number of Branches", 2, 8),
        ("Length Ratio", 0, 1),
        ("Initial Length", 0.5, 0.75),
        ("Width Ratio", 0.5, 0.75),
        ("Root Color", 0, 360),
        ("Leaf Color", 0, 360)
    ]

    for slider in sliders:
        placement = next(column_sequence)
        create_slider(sliders_frame, *slider, *placement)
