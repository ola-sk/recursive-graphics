import numpy as np
from numpy import radians as rad
import tkinter as tk
from helper_funcs import draw_sine_wave_segment
from helper_funcs import generate_gradient

# create comments for the function below

def fractal_canopy(canvas: tk.Canvas, x: int, y: int, init_length = 200, angle_delta = 10, start_angle = -90, n_splits = 2, n_iters = 3,length_ratio=0.75, off_angle = 0, wave_amp=0, first_iter = True, width=1, width_ratio=0.75, color = "#000000") -> None:
    """
    This function recursively draws a fractal canopy (a tree-like structure) on the provided Tkinter canvas. The fractal canopy is created by splitting each branch into multiple smaller branches at specified angles and lengths, and optionally adding sine wave segments to the branches.

    Args:
        canvas (tk.Canvas): The Tkinter canvas on which to draw the fractal canopy.
        x (int): The x-coordinate of the starting point of the fractal canopy.
        y (int): The y-coordinate of the starting point of the fractal canopy.
        init_length (int, optional): The initial length of the first branch. Defaults to 200.
        angle_delta (int, optional): The angle between the branches in degrees. Defaults to 10.
        start_angle (int, optional): The starting angle of the first branch in degrees. Defaults to -90 (upwards).
        n_splits (int, optional): The number of branches to split into at each iteration. Defaults to 2.
        n_iters (int, optional): The number of recursive iterations to perform. Defaults to 3.
        length_ratio (float, optional): The ratio by which the length of each branch decreases at each iteration. Defaults to 0.75.
        off_angle (int, optional): The offset angle for the branches in degrees. Defaults to 0.
        wave_amp (int, optional): The amplitude of the sine wave segments. Defaults to 0. If non-zero, sine wave segments will be added to the branches and performance will be slower.
        first_iter (bool, optional): A flag indicating whether this is the first iteration. Defaults to True. Do not touch this.
        width (int, optional): The width of the branches. Defaults to 1.
        width_ratio (float, optional): The ratio by which the width of each branch decreases at each iteration. Defaults to 0.75.
        color ([str, list], optional): The color of the branches in hex format. Defaults to "#000000" (black). If a list of hex values of len(n_iters) is provided, the color will change with each iteration. The last color in the list will be used for the final iteration.

    Returns:
        None
    """

    # base case
    if n_iters == 1:
        return

    # The first iteration behaves differently than the rest of the iterations, it's just a straight line
    elif first_iter:

        # turn start_angle into radians
        start_angle = rad(start_angle)

        # calculate the x and y coordinates of the end of the branch
        end_x = x + np.cos(start_angle)*init_length 
        end_y = y + np.sin(start_angle)*init_length

        # if wave_amp is not 0, draw a sine wave segment
        if wave_amp != 0:
            # if color is a string, use that color, else use the color from the list of colors
            if type(color) == str:
                draw_sine_wave_segment(canvas, x, y, end_x, end_y, init_length, wave_amp, width=width, fill=color)
            else:
                draw_sine_wave_segment(canvas, x, y, end_x, end_y, init_length, wave_amp, width=width, fill=color[-(n_iters-1)])
        # if wave_amp is 0, draw a straight line
        else:

            # if color is a string, use that color, else use the color from the list of colors
            if type(color) == str:
                canvas.create_line(x, y, end_x, end_y, width=width, fill=color)
            else:
                canvas.create_line(x, y, end_x, end_y, width=width, fill=color[-(n_iters-1)])
        
        

        # Recursive call
        fractal_canopy(canvas, end_x, end_y, n_iters=n_iters-1, first_iter=False, n_splits=n_splits, angle_delta=angle_delta, start_angle=np.degrees(start_angle)+off_angle, init_length=init_length*length_ratio, off_angle = off_angle+off_angle, wave_amp=wave_amp, width=width*width_ratio, width_ratio=width_ratio, color=color)
    
    # The rest of the iterations
    else:
        # calculate the angles of the splits
        left_angle = start_angle-(angle_delta/2)
        right_angle = start_angle+(angle_delta/2)
        # linspace gets us n_splits angles between left_angle and right_angle
        angles = np.linspace(left_angle, right_angle, n_splits, )
        
        # iterate over the angles
        for angle in angles:
            
            # turn angle into radians
            angle = rad(angle)

            # calculate the x and y coordinates of the end of the branch
            end_x = x + np.cos(angle)*init_length 
            end_y = y + np.sin(angle)*init_length

            # if wave_amp is not 0, draw a sine wave segment
            if wave_amp != 0:
                # if color is a string, use that color, else use the color from the list of colors
                if type(color) == str:
                    draw_sine_wave_segment(canvas, x, y, end_x, end_y, init_length, wave_amp, width=width, fill=color)
                else:
                    draw_sine_wave_segment(canvas, x, y, end_x, end_y, init_length, wave_amp, width=width, fill=color[-(n_iters-1)])
            # if wave_amp is 0, draw a straight line
            else:
                # if color is a string, use that color, else use the color from the list of colors
                if type(color) == str:
                    canvas.create_line(x, y, end_x, end_y, width=width, fill=color)
                else:
                    canvas.create_line(x, y, end_x, end_y, width=width, fill=color[-(n_iters-1)])

            # Recursive call
            fractal_canopy(canvas, end_x, end_y, n_iters=n_iters-1, first_iter=False, init_length=init_length*length_ratio, start_angle=np.degrees(angle)+off_angle, n_splits=n_splits, angle_delta=angle_delta, off_angle=off_angle+off_angle, wave_amp=wave_amp, width=width*width_ratio, width_ratio=width_ratio, color=color)





    






