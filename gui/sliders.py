"""
Module for creating sliders in the GUI.

Contains functions for creating sliders given their parameters, including some custom ones.
in the GUI, which can be used to control the parameters of the fractal tree displayed on the canvas.
It also defines the event handlers as well as the generator for the grid layout of the sliders.

A populate_sliders function is provided to add sliders for different parameters to the sliders frame.
It uses an application state defining the sliders' parameters and their ranges.
It binds each slider to an event and assigns the event handler that updates the canvas with the new tree.

"""
import tkinter as tk
from collections.abc import Collection

from datastructures import TreeNodeBase
from gui import draw_fractal_tree, update_canvas


def create_slider(
        parent: tk.Widget, parameter_name: str, label: str, from_: int | float, to: int | float,
        initial_value: int | float, resolution: int | float, row: int, column: int
) -> tk.Scale:
    """
    Create a slider and add it to the parent widget at row 'row' and column 'column'.

    Parameters:
        parent (tk.Widget): The parent widget to which the slider will be added.
        parameter_name (str): The name of the parameter that the slider will control.
            It can be accessed when creating new tree with the updated parameter (from the slider).
        label (str): The label for the slider.
        from_ (int or float): The starting value of the slider.
        to (int or float): The ending value of the slider.
        initial_value (int or float): The initial value of the slider.
        resolution (int or float): The increment step for the slider.
        row (int): The row position in the grid layout.
        column (int): The column position in the grid layout.

    Returns:
        slider (tk.Scale): The created slider widget.
    """
    slider = tk.Scale(parent, label=label, from_=from_, to=to, resolution=resolution, orient=tk.HORIZONTAL, length=120)
    slider.modifies_parameter = parameter_name
    if not (from_ <= initial_value <= to):
        raise ValueError(f"Initial value {initial_value} is not in the range [{from_}, {to}]")
    slider.set(initial_value)
    slider.last_value = initial_value
    slider.grid(row=row, column=column, padx=25, pady=3)
    return slider


def column_sequence_generator(num_columns: int):
    """
    A generator that yields the next column in the grid layout in the form of tuple: (row, column).
    The generator will cycle through the columns from left to right, top to bottom.
    """
    row = 0
    while True:
        for column in range(0, num_columns):
            yield row, column
        row += 1


def populate_sliders(
        sliders_frame: tk.Frame,
        canvas: tk.Canvas,
        sliders_init_data: Collection,
        num_columns: int = 4
) -> list[tk.Scale]:
    """
    Add sliders for different parameters to the sliders frame.
    Those sliders will be used to control the parameters of the fractal tree displayed on the canvas.

    This function binds each slider to an event of releasing the mouse button after dragging the slider.
    It makes the event handler update the canvas with the new tree after the slider is released.

    Parameters:
        sliders_frame (tk.Frame): The frame to which the sliders will be added.
        canvas (tk.Canvas): The canvas on which the fractal tree will be drawn.
        sliders_init_data (Collection): A collection of slider data:
            - keyword for parameter it controls,
            - label,
            - from (min value o the slider),
            - to (max value of the slider),
            - resolution (increment step for the slider.
        num_columns (int): The number of columns in the grid layout of the sliders frame.

    Returns:
        list[tk.Scale]: A list of sliders created and added to the sliders frame.
    """

    def on_slider_release_update_canvas_with_new_tree(event: tk.Event):
        """
        An event handler for the slider release event.
        Args:
            event (tk.Event): The event object.

        Returns:
            None
        """
        value_from_slider = event.widget.get()

        # Check if the value has changed
        if event.widget.last_value == value_from_slider:
            return  # No update needed if the value hasn't changed

        event.widget.last_value = value_from_slider
        # parameter's name that the slider manipulates
        slider_parameter_name = event.widget.modifies_parameter
        if not slider_parameter_name:
            # raise ValueError("Slider must have a parameter name to modify")
            return

        # new TreeNodeBase that has the value from the slider changed.
        TreeNodeBase.update_tree(**{slider_parameter_name: value_from_slider})

        # Update canvas with new tree
        update_canvas(canvas, draw_fractal_tree, TreeNodeBase.get_current_tree_root())
        return

    # configures the columns of the sliders_frame to have equal weight,
    # which means they will expand and contract equally when the window is resized.
    # This ensures that the sliders are evenly distributed across the available space in the frame.
    for i in range(num_columns):
        sliders_frame.columnconfigure(i, weight=1)

    column_sequence = column_sequence_generator(num_columns)
    sliders = []
    for slider_args in sliders_init_data:
        placement = next(column_sequence)
        # Create and place the slider in the parent widget
        slider = create_slider(sliders_frame, *slider_args, *placement)

        # Bind the slider to the event handler that updates the canvas with the new tree
        slider.bind("<ButtonRelease-1>", on_slider_release_update_canvas_with_new_tree)
        sliders.append(slider)
    return sliders
