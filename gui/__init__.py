"""
Initialization module for the GUI package.

This module imports and exposes functions for initializing the GUI,
creating sliders, and binding canvas zoom events.
"""

from gui.canvas_operations import draw_fractal_tree, update_canvas
from gui.gui_init import initialize_gui
from gui.sliders import populate_sliders
from gui.zoom import bind_canvas_zoom_events
