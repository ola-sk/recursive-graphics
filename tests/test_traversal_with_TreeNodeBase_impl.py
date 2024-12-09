from unittest import TestCase

import numpy as np

from datastructures import TreeNodeBase, traverse_breadth_first, traverse_depth_first


class TestTraversal(TestCase):
    def test_traverse_breadth_first(self):
        # Create a sample tree structure
        tree_node = TreeNodeBase(
            0, 0, 100, 0, 2, 0.7, np.radians(30), max_depth=3
        )

        # Define a list to capture the traversal order
        traversal_order = []

        # Perform breadth-first traversal appending to the traversal_order list as we go
        traverse_breadth_first(tree_node, traversal_order.append)

        # Define the expected order of traversal
        expected_order = [
            tree_node,
            tree_node.children[0], tree_node.children[1],
            tree_node.children[0].children[0], tree_node.children[0].children[1],
            tree_node.children[1].children[0], tree_node.children[1].children[1],
            tree_node.children[0].children[0].children[0], tree_node.children[0].children[0].children[1],
            tree_node.children[0].children[1].children[0], tree_node.children[0].children[1].children[1],
            tree_node.children[1].children[0].children[0], tree_node.children[1].children[0].children[1],
            tree_node.children[1].children[1].children[0], tree_node.children[1].children[1].children[1]
        ]

        # Assert the traversal order is as expected
        self.assertEqual(traversal_order, expected_order)

    def test_traverse_depth_first(self):
        tree_node = TreeNodeBase(
            0, 0, 100, 0, 2, 0.7, np.radians(30), max_depth=3
        )

        traversal_order = []
        traverse_depth_first(tree_node, traversal_order.append)

        expected_order = [
            tree_node,
            tree_node.children[0],
            tree_node.children[0].children[0],
            tree_node.children[0].children[0].children[0],
            tree_node.children[0].children[0].children[1],
            tree_node.children[0].children[1],
            tree_node.children[0].children[1].children[0],
            tree_node.children[0].children[1].children[1],
            tree_node.children[1],
            tree_node.children[1].children[0],
            tree_node.children[1].children[0].children[0],
            tree_node.children[1].children[0].children[1],
            tree_node.children[1].children[1],
            tree_node.children[1].children[1].children[0],
            tree_node.children[1].children[1].children[1]
        ]

        # Assert the traversal order is as expected
        self.assertEqual(traversal_order, expected_order)
