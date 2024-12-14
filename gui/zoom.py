"""
Zoom
====
Module provides zoom functionality for a tkinter canvas.

This module includes functions to start panning, perform panning, and zoom in/out on a tkinter canvas.
It also includes a function to bind these events to the canvas.

Functions:
        start_pan(event): Marks the starting point for panning.
        do_pan(event): Drags the canvas to the new position.
        zoom(event): Zooms in or out on the canvas.
        bind_canvas_zoom_events(canvas): Binds the pan and zoom events to the canvas.

Example:
    import tkinter as tk
    from gui import bind_canvas_zoom_events

    # Create a tkinter window and canvas
    window = tk.Tk()
    canvas = tk.Canvas(window, bg="white", width=600, height=450)
    canvas.pack() # or grid()

    # Set the canvas and bind events
    bind_canvas_zoom_events(canvas)

    # Run the tkinter event loop
    window.mainloop()
"""
import tkinter as tk


def start_pan(event: tk.Event):
    """Marks the starting point for panning."""
    canvas: tk.Canvas = event.widget
    canvas.scan_mark(event.x, event.y)


def do_pan(event: tk.Event):
    """Drags the canvas to the new position."""
    canvas: tk.Canvas = event.widget
    canvas.scan_dragto(event.x, event.y, gain=1)


def zoom(event: tk.Event):
    """
    Zooms in or out on the canvas, adjusting for the pan, by scaling the canvas content
    based on the mouse wheel movement.
    The zoom operation aligns the origin coordinates of the scaled piece of the canvas at the mouse position
    (event.x, event.y) with the mouse position when zoom occurred.
    ensuring that the newly displayed piece's origin coordinates (the place at which the mouse was when the scrolling
    started) align with the mouse position when the zoom event handler was called.

    The `canvas.scale` method is called with the following parameters:
    - "all": This indicates that all items on the canvas should be scaled.
    - `canvas.canvasx(event.x)`: The x-coordinate of the mouse event, converted to canvas coordinates.
    - `canvas.canvasy(event.y)`: The y-coordinate of the mouse event, converted to canvas coordinates.
    - `scale`: The scaling factor, which is 1.1 for zooming in and 0.9 for zooming out.

    From the Tkinter documentation on scale function:
    '''Scale item TAGORID with XORIGIN, YORIGIN, XSCALE, YSCALE.'''

    In summary, the `canvas.scale` method called here scales the items on the canvas with respect to the specified
    origin - mouse position in canvas coordinates and scaling factor scale specified for both XSCALE and YSCALE
    parameters.
    """
    canvas: tk.Canvas = event.widget
    scale = 1.1 if event.delta > 0 else 0.9
    canvas.scale("all", canvas.canvasx(event.x), canvas.canvasy(event.y), scale, scale)


def bind_canvas_zoom_events(canvas: tk.Canvas):
    """
    Binds mouse events to the pan and zoom events on the canvas.
    """
    canvas.bind("<MouseWheel>", zoom)
    canvas.bind("<ButtonPress-1>", start_pan)
    canvas.bind("<B1-Motion>", do_pan)
