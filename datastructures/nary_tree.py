import numpy as np
from datastructures.transformation import Transformation


class CanopyTreeNode:

    def __init__(self, depth, start_x, start_y, length, angle, num_children, length_scale, delta_angle, max_depth=6):
        self.depth = depth                  # Depth in the fractal tree - the further from the root the lesser the depth
        self.start_x = start_x              # Start x-coordinate
        self.start_y = start_y              # Start y-coordinate
        self.length = length                # Length of the branch
        self.angle = angle                  # Display angle (in pi radians)
        self.end_x = self.start_x + np.cos(self.angle) * length    # End x-coordinate
        self.end_y = self.start_y + np.sin(self.angle) * length    # End y-coordinate
        self.num_children = num_children    # Number of children
        self.length_scale = length_scale    # Ratio of the length of the child branch to the parent branch
        self.delta_angle = delta_angle      # Angles in between the branches
        self.children = None                # Declare children variable for children nodes
        # Create children nodes
        if self.depth <= max_depth and self.num_children > 0:
            self.children = np.ndarray(
                self.num_children,
                dtype=CanopyTreeNode
            )                               # Fixed-size array of CanopyTreeNode objects
            self.set_children(self.depth + 1, self.end_x, self.end_y, self.length * self.length_scale, self.angle,
                              self.num_children, self.length_scale, self.delta_angle)


    def set_children(self,
                     depth: int,
                     start_x: float,
                     start_y: float,
                     length: float,
                     parent_angle: float,
                     num_children: int,
                     length_scale: float,
                     delta_angle: float):
        angle_spectrum = self.angle_spectrum(parent_angle, delta_angle, num_children)
        if len(angle_spectrum) != num_children:
            raise ValueError("The number of children must match the number of angles in the spectrum.")
        for i, angle in enumerate(angle_spectrum):
            self.children[i] = CanopyTreeNode(
                depth,
                start_x,
                start_y,
                length,
                angle,
                num_children,
                length_scale,
                delta_angle)


    @staticmethod
    def angle_spectrum(
            parent_angle: float,
            delta_angle: float,
            num_children: int,
            transformation: Transformation = Transformation.SYMMETRIC,
            depth: int | None = None
    ) -> np.ndarray:
        angle_range = (num_children-1) * delta_angle
        return np.linspace(parent_angle - angle_range / 2, parent_angle + angle_range / 2, num_children)
