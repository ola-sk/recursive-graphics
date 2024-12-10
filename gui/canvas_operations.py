"""
Draw On Canvas
==============

Provides functionality for drawing fractal trees on a canvas.

Functions:
    - draw_fractal_tree
    - update_canvas

Usage example:
    import tkinter as tk
    from gui.canvas_operations import draw_fractal_tree

    window = tk.Tk()
    canvas = tk.Canvas(window)
    TreeNodeBase(...)
    draw_fractal_tree(canvas, TreeNodeBase.get_current_tree_root())
    window.mainloop()
"""
import tkinter as tk

from datastructures import TreeNodeBase, traverse_breadth_first


def draw_fractal_tree(canvas: tk.Canvas, root_node: TreeNodeBase=None) -> None:
    """
    Draw a fractal tree on the canvas.
    Args:
        canvas: tkinter.Canvas object
        root_node: Node object representing the fractal tree (root node)

    Returns:
        None
    """
    def draw_line(node: TreeNodeBase):
        canvas.create_line(node.start_x, node.start_y, node.end_x, node.end_y, fill="green")
    if root_node is None:
        return
    traverse_breadth_first(root_node, draw_line)


def update_canvas(canvas: tk.Canvas, drawing_function: callable = draw_fractal_tree, *args) -> None:
    """
    Update the canvas based on the slider values.
    Parameters:
        canvas (tk.Canvas): The canvas to update.
        drawing_function (callable): The drawing function to use, e.g. draw_fractal_tree (default)
        *args: Additional arguments for the drawing function, e.g. TreeNodeBase object.
    Returns:
        None
    """
    canvas.delete("all")
    drawing_function(canvas, *args)
