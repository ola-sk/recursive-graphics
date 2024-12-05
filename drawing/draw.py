from canvas_setup import canvas_setup
from numpy import pi, radians

from datastructures.nary_tree import CanopyTreeNode


# canvas.create_line(x, y, end_x, end_y, width=width, fill=color)
def draw(canvas):
    canvas.create_line(100, 200, 200, 35, fill="gold", width=5)
    canvas.create_line(250, 500, 250, 400, fill="black", width=5)

geometry_x = 500
geometry_y = 500
def draw_tree(canvas):
    # Create the tree at root node
    root = CanopyTreeNode(
        0,
        geometry_x/2,
        geometry_y,
        100,
        radians(-90),
        4,
        0.75,
        radians(30),
        20)

    def traverse_tree(node):
        # Draw the line for the current node
        canvas.create_line(node.start_x, node.start_y, node.end_x, node.end_y)

        # Recursively draw lines for each child node
        if node.children is not None:
            for child in node.children:
                traverse_tree(child)

    traverse_tree(root)

canvas_setup(geometry_x, geometry_y, draw_tree)
