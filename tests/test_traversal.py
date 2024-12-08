from collections.abc import Sequence
from typing import Union
from unittest import TestCase

from datastructures.traversal import traverse_breadth_first, traverse_depth_first


class Node:
    def __init__(self, children: Union[None, Sequence] = None):
        self.children = children if children is not None else []


class TestTraversal(TestCase):
    def setUp(self):
        self.results = []

    def test_empty_tree(self):
        self.results = []
        traverse_breadth_first(None, self.results.append)
        self.assertEqual(self.results, [])

        self.results = []
        traverse_depth_first(None, self.results.append)
        self.assertEqual(self.results, [])

    def test_single_node(self):
        root = Node()
        self.results = []
        traverse_breadth_first(root, self.results.append)
        self.assertEqual(self.results, [root])

        self.results = []
        traverse_depth_first(root, self.results.append)
        self.assertEqual(self.results, [root])

    def test_tree_with_multiple_children(self):
        child1 = Node()
        child2 = Node()
        child3 = Node()
        root = Node([child1, child2, child3])
        self.results = []
        traverse_breadth_first(root, self.results.append)
        self.assertEqual(self.results, [root, child1, child2, child3])

        self.results = []
        traverse_depth_first(root, self.results.append)
        self.assertEqual(self.results, [root, child1, child2, child3])

    def test_balanced_tree(self):
        child1 = Node()
        child2 = Node()
        root = Node([child1, child2])
        self.results = []
        traverse_breadth_first(root, self.results.append)
        self.assertEqual(self.results, [root, child1, child2])

        self.results = []
        traverse_depth_first(root, self.results.append)
        self.assertEqual(self.results, [root, child1, child2])

    def test_unbalanced_tree(self):
        child1 = Node()
        child2 = Node([child1])
        child3 = Node()
        child4 = Node([child2, child3])
        child5 = Node()
        root = Node([child4, child5])
        self.results = []
        traverse_breadth_first(root, self.results.append)
        self.assertEqual(self.results, [root, child4, child5, child2, child3, child1])

        self.results = []
        traverse_depth_first(root, self.results.append)
        self.assertEqual(self.results, [root, child4, child2, child1, child3, child5])

    def test_children_is_not_iterable(self):
        child = Node()
        root = Node(child)  # type: ignore
        self.results = []
        with self.assertRaises(TypeError):
            traverse_breadth_first(root, self.results.append)
