import numpy as np
from numpy import radians as rad
import tkinter as tk
from helper_funcs import draw_sine_wave_segment
from helper_funcs import generate_gradient

def fractal_canopy(canvas: tk.Canvas, x: int, y: int, init_length = 200, angle_delta = 10, start_angle = -90, n_splits = 2, n_iters = 3,length_ratio=0.75, off_angle = 0, first_iter = True) -> None:
    """
    
    Parameters
    ----------
    canvas : tk.Canvas
        The canvas object to draw on.
    x : int
        The x coordinate of the starting point.
    y : int
        The y coordinate of the starting point.
    init_length : int, optional
        The initial length of the line. The default is 200.
    angle_delta : int, optional
        The angle between the splits. The default is 10.
    start_angle : int, optional
        The starting angle. The default is -90. In tkinter, this goes straight up.
    n_splits : int, optional
        The number of branch splits per level. The default is 2.
    n_iters : int, optional
        The number of iterations of the recursive tree. The default is 3.
    length_decay : int, optional
        The decay factor of the length of the branches. The default is 2.
    first_iter : bool, optional
        The first iteration. The default is True. Don't touch this.

    Returns
    -------
    None.

    Description
    -------
    
    This function draws a fractal tree on a tkinter canvas. The tree is drawn using a recursive algorithm. The tree starts at the point (x, y) and branches out in n_splits directions. The angle between the splits is angle_delta. The length of the branches is init_length. The length of the branches decays by a factor of length_decay at each iteration. The tree has n_iters levels of recursion. The start_angle is the angle of the first branch.
    """

    if n_iters == 1:
        # base case
        return

    # The first iteration behaves differently than the rest of the iterations, it's just a straight line

    elif first_iter:

        
        # turn start_angle into radians
        start_angle = rad(start_angle)

        # calculate the x and y coordinates of the end of the branch
        end_x = x + np.cos(start_angle)*init_length 
        end_y = y + np.sin(start_angle)*init_length

        # draw the branch
        canvas.create_line(x, y, end_x, end_y)

        # recursive call
        fractal_canopy(canvas, end_x, end_y, n_iters=n_iters-1, first_iter=False, n_splits=n_splits, angle_delta=angle_delta, start_angle=np.degrees(start_angle)+off_angle, init_length=init_length)
    
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

            # draw the branch
            canvas.create_line(x, y, end_x, end_y)

            # recursive call
            fractal_canopy(canvas, end_x, end_y, n_iters=n_iters-1, first_iter=False, init_length=init_length*length_ratio, start_angle=np.degrees(angle)+off_angle, n_splits=n_splits, angle_delta=angle_delta)

def fractal_canopy_wave(canvas: tk.Canvas, x: int, y: int, init_length = 200, angle_delta = 10, start_angle = -90, n_splits = 2, n_iters = 3,length_ratio=0.75, off_angle = 0, wave_amp=1, first_iter = True, width=1, width_ratio=0.75, gradient_list = None) -> None:
    """
    
    Parameters
    ----------
    canvas : tk.Canvas
        The canvas object to draw on.
    x : int
        The x coordinate of the starting point.
    y : int
        The y coordinate of the starting point.
    init_length : int, optional
        The initial length of the line. The default is 200.
    angle_delta : int, optional
        The angle between the splits. The default is 10.
    start_angle : int, optional
        The starting angle. The default is -90. In tkinter, this goes straight up.
    n_splits : int, optional
        The number of branch splits per level. The default is 2.
    n_iters : int, optional
        The number of iterations of the recursive tree. The default is 3.
    length_decay : int, optional
        The decay factor of the length of the branches. The default is 2.
    first_iter : bool, optional
        The first iteration. The default is True. Don't touch this.

    Returns
    -------
    None.

    Description
    -------
    
    This function draws a fractal tree on a tkinter canvas. The tree is drawn using a recursive algorithm. The tree starts at the point (x, y) and branches out in n_splits directions. The angle between the splits is angle_delta. The length of the branches is init_length. The length of the branches decays by a factor of length_decay at each iteration. The tree has n_iters levels of recursion. The start_angle is the angle of the first branch.
    """

    if n_iters == 1:
        # base case
        return

    # The first iteration behaves differently than the rest of the iterations, it's just a straight line

    elif first_iter:

        # turn start_angle into radians
        start_angle = rad(start_angle)

        # calculate the x and y coordinates of the end of the branch
        end_x = x + np.cos(start_angle)*init_length 
        end_y = y + np.sin(start_angle)*init_length

        #canvas.create_line(x, y, end_x, end_y)
        # draw a sine wave segment from 0 to 2pi on the canvas, rotated and translated so it starts from x,y to end_x, end_y

        draw_sine_wave_segment(canvas, x, y, end_x, end_y, init_length, wave_amp, width=width, fill=gradient_list[-(n_iters-1)])
        
        

        # recursive call
        fractal_canopy_wave(canvas, end_x, end_y, n_iters=n_iters-1, first_iter=False, n_splits=n_splits, angle_delta=angle_delta, start_angle=np.degrees(start_angle)+off_angle, init_length=init_length*length_ratio, off_angle = off_angle+off_angle, wave_amp=wave_amp, width=width*width_ratio, width_ratio=width_ratio, gradient_list=gradient_list)
    
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

            # draw the branch
            draw_sine_wave_segment(canvas, x, y, end_x, end_y, init_length, wave_amp, width=width, fill=gradient_list[-(n_iters-1)])

            # recursive call
            fractal_canopy_wave(canvas, end_x, end_y, n_iters=n_iters-1, first_iter=False, init_length=init_length*length_ratio, start_angle=np.degrees(angle)+off_angle, n_splits=n_splits, angle_delta=angle_delta, off_angle=off_angle+off_angle, wave_amp=wave_amp, width=width*width_ratio, width_ratio=width_ratio, gradient_list=gradient_list)





    






