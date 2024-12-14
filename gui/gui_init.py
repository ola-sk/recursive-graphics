"""
This module initializes the GUI window for the game.

The `initialise_gui` function creates a new Tkinter window with the title
"Fractal Matching Game" and the specified width and height.
The window is not resizable.
"""
import tkinter as tk


def initialise_gui(window_width: int = 1200, window_height: int = 900):
    window = tk.Tk()
    window.title("Fractal Matching Game")
    window.geometry(f"{window_width}x{window_height}")
    window.resizable(False, False)
    return window
