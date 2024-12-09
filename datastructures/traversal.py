from collections import deque


def traverse_breadth_first(root, node_process_function: callable) -> None:
    """
    BFT(Breadth-First Traversal): Traverse the tree and process each node.

    To efficiently traverse the tree, a queue is used to store and consume the nodes in a FIFO order.
    That way we can pop elements from the start of the queue and add elements to its end in O(1) time.
    Double ended queue (deque) is Python's standard library implementation of a queue that supports this operation.

    Args:
        root: The root node of the tree.
        node_process_function: A callable (function, method, etc.) that processes the node.

    Returns:
        None
    """
    if root is None:
        return
    queue = deque([root])
    while queue:  # While the queue is not empty
        node = queue.popleft()  # Pop the first element from the queue; O(1) operation
        # Process the current node (e.g., draw the branch)
        node_process_function(node)
        if node.children is not None:
            queue.extend(
                node.children
            )  # Append each child as the last element of the queue


def traverse_depth_first(root, node_process_function: callable):
    """
    DFT(Depth-First Traversal): Traverse the tree and process each node.

    To efficiently traverse the tree, a stack is used to store and consume the nodes in a LIFO order.
    That way we can pop elements from the end of the stack and add elements to its end in O(1) time.

    Args:
        root: The root node of the tree.
        node_process_function: A callable (function, method, etc.) that processes the node.

    Returns:
        None
    """
    if root is None:
        return
    stack = [root]
    while stack:
        # pop the last (top) element from the stack
        node = stack.pop()

        # Process the current node (e.g. draw the branch)
        node_process_function(node)

        if node.children is not None:
            stack.extend(
                reversed(node.children)
            )  # Append the last elem first so that the first child is popped first
