import tkinter as tk
from random import randint

import numpy as np

from gui_init import initialize_gui, create_congratulatory_popup

win: tk.Tk = initialize_gui()
random_params: dict[str, int | float] = {}

def start():
    def restart():
        global win
        win.destroy() #TODO: Block sliders instead and restart sliders to random values and canvas to random tree once restart button is clicked
        win = initialize_gui()
        start()


    def draw_tree(x, y, length, angle, canvas, iteration, branch_angle, length_ratio: float, tag, first_iter=True):
        if iteration == 0:
            return

        current_angle = 90 if first_iter else angle

        x_end = x + length * np.cos(np.radians(current_angle))
        y_end = y - length * np.sin(np.radians(current_angle))

        canvas.create_line(x, y, x_end, y_end, fill='red', tags=tag)

        draw_tree(x_end, y_end, length * length_ratio, angle + branch_angle, canvas, iteration - 1, branch_angle,
                  length_ratio, tag, first_iter=False, )
        draw_tree(x_end, y_end, length * length_ratio, angle - branch_angle, canvas, iteration - 1, branch_angle,
                  length_ratio, tag, first_iter=False)

    def update_tree():
        # Clear the previous tree
        win.canvas.delete("updated")

        # Get slider values
        length = length_slider.get()
        angle = angle_slider.get()
        iterations = iteration_slider.get()
        branch_angle = branch_angle_slider.get()  # Get angle between branches value
        length_ratio = length_ratio_slider.get()

        # Draw the updated tree
        draw_tree(600, 600, length, angle, win.canvas, iterations, branch_angle, length_ratio, tag="updated",
                  first_iter=True)
        check_match()

    def check_match():
        try:
            # I think we can even assume this is always in globals.
            # We can only check if the window object is not destroyed by checking if accessing it causes errors.
            if hasattr(win, 'congratulatory_popup') and win.congratulatory_popup.winfo_exists():
                win.congratulatory_popup.destroy()
        except tk.TclError:
            pass
        length_tolerance = 2
        angle_tolerance = 2
        iteration_tolerance = 0
        branch_angle_tolerance = 2
        length_ratio_tolerance = 0.02

        length_diff = abs(random_params['length'] - length_slider.get())
        angle_diff = abs(random_params['angle'] - angle_slider.get())
        iteration_diff = abs(random_params['iteration'] - iteration_slider.get())
        branch_angle_diff = abs(random_params['branch_angle'] - branch_angle_slider.get())
        length_ratio_diff = abs(random_params['length_ratio'] - length_ratio_slider.get())

        if (
                length_diff < length_tolerance and
                angle_diff < angle_tolerance and
                iteration_diff <= iteration_tolerance and
                branch_angle_diff < branch_angle_tolerance and
                length_ratio_diff < length_ratio_tolerance
        ):
            # The congratulatory popup destroys itself once the restart button is clicked and also restarts the game.
            create_congratulatory_popup(win, restart)
        


    def generate_random_tree():
        global random_params
        random_params = {
            'x': 300,
            'y': 600,
            'length': randint(80, 180),
            'angle': randint(0, 180),
            'canvas': win.canvas,
            'iteration': randint(3, 6),
            'branch_angle': randint(10, 90),
            'length_ratio': randint(1, 100) / 100
        }
        print(random_params)
        draw_tree(**random_params, first_iter=True, tag="random")

    global win

    # Create sliders for controlling the tree's parameters
    length_slider = tk.Scale(win.scales_label, from_=50, to=200, orient=tk.HORIZONTAL, label="Initial Branch Length",
                             resolution=1, command=lambda e: update_tree(), length=200)
    length_slider.set(100)
    length_slider.grid(row=0, column=0, padx=10, pady=10)

    angle_slider = tk.Scale(win.scales_label, from_=0, to=180, orient=tk.HORIZONTAL, label="Branch Angle", resolution=1,
                            command=lambda e: update_tree(), length=200)
    angle_slider.set(45)
    angle_slider.grid(row=0, column=1, padx=10, pady=10)

    iteration_slider = tk.Scale(win.scales_label, from_=1, to=10, orient=tk.HORIZONTAL, label="Iterations",
                                resolution=1, command=lambda e: update_tree(), length=200)
    iteration_slider.set(6)
    iteration_slider.grid(row=0, column=2, padx=10, pady=10)
    # Add a slider for controlling the angle between the branches
    branch_angle_slider = tk.Scale(win.scales_label, from_=0, to=90, orient=tk.HORIZONTAL,
                                   label="Angle Between Branches", resolution=1, command=lambda e: update_tree(),
                                   length=200)
    branch_angle_slider.set(30)
    branch_angle_slider.grid(row=0, column=3, padx=10, pady=10)

    length_ratio_slider = tk.Scale(win.scales_label, from_=0.1, to=1, orient=tk.HORIZONTAL, label="Length Ratio",
                                   resolution=0.01, command=lambda e: update_tree(), length=200)
    length_ratio_slider.set(0.7)
    length_ratio_slider.grid(row=0, column=4, padx=10, pady=10)

    generate_random_tree()

    update_tree()

    win.canvas.pack(padx=10, pady=10)
    win.scales_label.pack(padx=10, pady=10)
    win.mainloop()

start()
