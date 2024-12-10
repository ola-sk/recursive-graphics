import numpy as np


class TreeNodeBase:
    """
    Base class for the tree node in the fractal tree.

    The children nodes are created during the initialization of the TreeNodeBase object.
    Current implementation balances memory usage and computational efficiency by initializing
    the children array upfront.
    This children array holds references to direct children.
    This approach is computationally (slightly) less expensive than extending the list of children
    (extending list may need to reallocate memory as new elements are added).

    Attributes:

        start_x (float): Start x-coordinate.
        start_y (float): Start y-coordinate.
        length (float): Length of the branch.
        angle (float): Display angle (in pi radians).
        end_x (float): End x-coordinate.
        end_y (float): End y-coordinate.
        num_children (int): Number of children.
        length_scale (float): Ratio of the length of the child branch to the parent branch.
        delta_angle (float): Angles in between the branches are delta_angle (radians) apart.
        depth (int): Depth in the fractal tree. If depth equals max_depth, no children are created further.
        max_depth (int): Maximum depth in the fractal tree.
        children (np.ndarray): Declare children variable for children nodes.

    Methods:

        set_children: Create children nodes.
        angle_spectrum: Generate the angles for the children.
    """
    # define a static property to store the current tree node
    _current_tree_root = None
    def __init__(
        self,
        start_x: float,
        start_y: float,
        length: float,
        angle: float,
        num_children: int,
        length_scale: float,
        delta_angle: float,
            depth: int = 0,
            max_depth: int = 7,
    ):
        if num_children < 0:
            raise ValueError("Number of children must be greater than or equal to 0.")
        if TreeNodeBase._current_tree_root is None:
            TreeNodeBase._current_tree_root = self
        self.start_x = start_x  # Start x-coordinate
        self.start_y = start_y  # Start y-coordinate
        self.length = length  # Length of the branch
        self.angle = angle  # Angle (in pi radians)
        self.end_x = self.start_x + np.cos(self.angle) * length  # End x-coordinate
        self.end_y = self.start_y + np.sin(self.angle) * length  # End y-coordinate
        self.num_children = num_children  # Number of children
        self.length_scale = (
            length_scale  # Ratio of the length of the child branch to the parent branch
        )
        self.delta_angle = delta_angle  # Angles in between the branches
        self.depth = depth  # Depth in the fractal tree
        self.max_depth = max_depth  # Maximum depth in the fractal tree
        self.children = None  # Declare children variable for children nodes
        # Create children nodes
        if self.depth < self.max_depth and self.num_children > 0:
            self.children = np.ndarray(
                self.num_children, dtype=self.__class__
            )  # Fixed-size array of TreeNode objects
            self.set_children(
                self.end_x,
                self.end_y,
                self.length * self.length_scale,
                self.angle,
                self.num_children,
                self.length_scale,
                self.delta_angle,
                self.depth + 1,
                self.max_depth
            )

    def set_children(
        self,
        start_x: float,
        start_y: float,
        length: float,
        parent_angle: float,
        num_children: int,
        length_scale: float,
        delta_angle: float,
            depth: int,
            max_depth: int
    ):
        angle_spectrum: np.ndarray[float] = self.angle_spectrum(
            parent_angle, delta_angle, num_children
        )
        if len(angle_spectrum) != num_children:
            raise ValueError(
                "The number of children must match the number of angles in the spectrum."
            )
        for i, angle in enumerate(angle_spectrum):  # type: int, float
            self.children[i] = TreeNodeBase(
                start_x,
                start_y,
                length,
                angle,
                num_children,
                length_scale,
                delta_angle,
                depth,
                max_depth
            )

    @classmethod
    def get_current_tree_root(cls):
        return cls._current_tree_root

    @classmethod
    def update_tree(cls, **kwargs) -> None:
        """
        Generate a new tree node with altered values.

        It effectively creates a new tree from old reusing its parameters
        except for those that are provided as keywords arguments (in kwargs).

        This function can be run on a separate thread to offload the heavy computation from the GUI thread.
        The canvas should then get updated after a part or all of the calculations are done.

        With the help of multithreading we should be able to keep the GUI responsive,
        displaying the old fractal and the user still being able to zoom and pan it,
        (also displaying calculation indicators or even progress bar if possible),
        while computing the new fractal on a thread other that what the GUI is running on.

        Args:
            kwargs: Keyword arguments with which the new tree is generated.

        Returns:
            TreeNodeBase: The new TreeNodeBase object.
        """
        # This could run on another thread
        new_tree_root = TreeNodeBase(
            start_x=kwargs.get('start_x', cls._current_tree_root.start_x),
            start_y=kwargs.get('start_y', cls._current_tree_root.start_y),
            length=kwargs.get('length', cls._current_tree_root.length),
            angle=kwargs.get('angle', cls._current_tree_root.angle),
            num_children=kwargs.get('num_children', cls._current_tree_root.num_children),
            length_scale=kwargs.get('length_scale', cls._current_tree_root.length_scale),
            delta_angle=kwargs.get('delta_angle', cls._current_tree_root.delta_angle),
            depth=kwargs.get('depth', cls._current_tree_root.depth),
            max_depth=kwargs.get('max_depth', cls._current_tree_root.max_depth)
        )
        cls._current_tree_root = new_tree_root


    @staticmethod
    def angle_spectrum(
        parent_angle: float, delta_angle: float, num_children: int
    ) -> np.ndarray:
        """
        Generate the angles for the children nodes in the tree data structure.

        Args:
            parent_angle (float): The angle of the parent branch.
            delta_angle (float): The angle difference between each child branch.
            num_children (int): The number of children branches.

        Returns:
            np.ndarray: An array of angles for the children branches.
        """
        if num_children < 0:
            raise ValueError("Number of children must be greater than or equal to 0.")
        if num_children == 0:
            result = np.array([])
            return result
        angle_range = (num_children - 1) * delta_angle
        result = np.linspace(
            parent_angle - (angle_range / 2),
            parent_angle + (angle_range / 2),
            num=num_children
        )
        return result
