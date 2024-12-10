"""
Each of sliders is a tuple with 4 elements:
    0. parameter name
    1. label for the slider
    2. minimum value for the slider
    3. maximum value for the slider
    4. initial value for the slider
    5. resolution:  the increment step for the slider

This sets the initial values for the sliders in the GUI.
This is used in the mainwindow.py file to populate the sliders.
The way code works is each of those items in the `sliders_init_data` list is used to create a slider in the GUI.

✨ Nice and clean way to set initial values for the sliders without hardcoding them in the GUI code.
"""
sliders_init_data = [
    ('num_children', "Number of Branches", 2, 8, 3, 1),
    ('length_scale', "Length Ratio", 0.1, 10, 0.7, 0.1),
    ('max_depth', "Depth", 1, 10, 7, 1),
    ('length', "Trunk's Length", 10, 330, 150, 10),
    ('delta_angle', "Angle Size", 0, 180, 35, 5),  # in degrees
    # (None, "Angle Offset", -45, 45, 0, 1),
    # (None, "Width Ratio", 0.5, 1, 1, 0.1),
    # (None, "Root Color", 0, 360, 0, 10),
    # (None, "Leaf Color", 0, 360, 0, 10)
]
