"""
This module initializes the GUI window for the game.

The `initialize_gui` function creates a new Tkinter window with the title
"Fractal Matching Game" and the specified width and height.
The window is not resizable.
"""
import tkinter as tk


def initialize_gui() -> tk.Tk:
    window = tk.Tk()
    window.title("Fractal Matching Game")

    window.canvas = tk.Canvas(window, bg='green', width=1000, height=600)

    window.scales_label = tk.LabelFrame(window, text="Adjust Tree Parameters", font=("Arial", 14), padx=10, pady=10)

    return window
