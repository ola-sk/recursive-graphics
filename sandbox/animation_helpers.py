import tkinter as tk
import numpy as np


def draw_tree_animated(canvas, x, y, length, angle, iterations, branch_angle, length_ratio, tag, delay=50):
    """
    Draws a fractal tree with animation on the given canvas.
    """
    branch_queue = [(x, y, length, angle, iterations)]

    def draw_next_branch():
        if not branch_queue:
            return  # Stop when no branches are left

        current_x, current_y, current_length, current_angle, current_iterations = branch_queue.pop(0)
        if current_iterations == 0:
            return  # Stop when iterations reach 0

        # Calculate the end coordinates of the branch
        x_end = current_x + current_length * np.cos(np.radians(current_angle))
        y_end = current_y - current_length * np.sin(np.radians(current_angle))

        # Draw the branch
        canvas.create_line(current_x, current_y, x_end, y_end, fill="blue", tags=tag)

        # Add child branches to the queue
        branch_queue.append(
            (x_end, y_end, current_length * length_ratio, current_angle + branch_angle, current_iterations - 1))
        branch_queue.append(
            (x_end, y_end, current_length * length_ratio, current_angle - branch_angle, current_iterations - 1))

        # Schedule the next branch to be drawn
        canvas.after(delay, draw_next_branch)

    # Start drawing
    draw_next_branch()


def animate_tree(canvas, params, tag="animated", delay=50):
    """
    Animates the tree-growing process for given parameters.
    """
    draw_tree_animated(
        canvas,
        params['x'], params['y'],
        params['length'], params['angle'],
        params['iterations'], params['branch_angle'],
        params['length_ratio'], tag, delay
    )


def add_animation_buttons(canvas, sliders_frame, random_tree_params):
    """
    Adds buttons for animating user and random trees to the GUI.
    """

    def get_user_params():
        # Get the current slider values
        return {
            'x': 600,
            'y': 600,
            'length': length_slider.get(),
            'angle': angle_slider.get(),
            'iterations': iteration_slider.get(),
            'branch_angle': branch_angle_slider.get(),
            'length_ratio': length_ratio_slider.get(),
        }

    # Buttons for animation
    animate_user_button = tk.Button(sliders_frame, text="Animate User Tree",
                                    command=lambda: animate_tree(canvas, get_user_params(), tag="user_animated"))
    animate_user_button.grid(row=2, column=0, padx=10, pady=10)

    animate_random_button = tk.Button(sliders_frame, text="Animate Random Tree",
                                      command=lambda: animate_tree(canvas, random_tree_params, tag="random_animated"))
    animate_random_button.grid(row=2, column=1, padx=10, pady=10)


# Sliders for user parameters (to avoid dependency issues, define them locally)
length_slider = tk.Scale(from_=50, to=200, orient=tk.HORIZONTAL, label="Initial Branch Length", resolution=1,
                         length=200)
angle_slider = tk.Scale(from_=0, to=180, orient=tk.HORIZONTAL, label="Branch Angle", resolution=1, length=200)
iteration_slider = tk.Scale(from_=1, to=10, orient=tk.HORIZONTAL, label="Iterations", resolution=1, length=200)
branch_angle_slider = tk.Scale(from_=0, to=90, orient=tk.HORIZONTAL, label="Angle Between Branches", resolution=1,
                               length=200)
length_ratio_slider = tk.Scale(from_=0.1, to=1, orient=tk.HORIZONTAL, label="Length Ratio", resolution=0.01, length=200)
