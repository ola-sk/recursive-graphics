"""
Draw On Canvas
==============

Provides functionality for drawing basic shapes on a canvas.

Functions:
    - draw_squares

Usage example:
    import tkinter as tk
    from module_name import draw_squares

    window = tk.Tk()
    canvas = tk.Canvas(window)
    draw_squares(canvas, 8, 50)
    window.mainloop()
"""
import tkinter as tk


def draw_squares(canvas: tk.Canvas, num_squares: int = 8, square_size: float = 50, color: str = "blue") -> None:
    """
    Draw squares on the canvas.
    Args:
        canvas: tkinter.Canvas object
        num_squares: Number of squares to draw
        square_size: Size of each square
        color: Color of the squares

    Returns:
        None
    """
    for i in range(num_squares):
        x = i * square_size
        y = i * square_size
        canvas.create_rectangle(x, y, x + square_size, y + square_size, outline=color, fill=color)
