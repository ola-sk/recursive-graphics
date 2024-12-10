"""
Data Structures Module
======================

This module provides base classes and traversal functions for various data structures.

Classes:
    - TreeNodeBase: A base class for tree nodes.

Functions:
    - traverse_depth_first: Function to traverse a tree in depth-first order.
    - traverse_breadth_first: Function to traverse a tree in breadth-first order.

Usage example:
    from datastructures import TreeNodeBase, traverse_breadth_first

    # Create tree node
    root = TreeNodeBase()
    def draw_fractal_tree(canvas: tk.Canvas, root_node: TreeNodeBase=None) -> None:

        def draw_line(node: TreeNodeBase):
            canvas.create_line(node.start_x, node.start_y, node.end_x, node.end_y, fill="green")
        if root_node is None:
            return
        # Traverse the tree
        traverse_breadth_first(root_node, draw_line)

        ...
        draw_fractal_tree(
            canvas,
            TreeNodeBase(
                canvas_width/2, canvas_height, 150, radians(-90), 3, 0.7, radians(25), max_depth=7
            )
)
"""

from datastructures.fractal_tree_base import TreeNodeBase
from datastructures.traversal import traverse_depth_first, traverse_breadth_first
