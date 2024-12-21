import tkinter as tk
import numpy as np
from random import randint

def start():
    def exit_app():
        win.destroy()

    def restart():
        win.destroy()
        congrat_win.destroy()
        start()

    def centrum_window(window,title: str, width, height): # Function to center the window
        screen_width = window.winfo_screenwidth() # takes the width of the screen
        screen_height = window.winfo_screenheight() # takes the height of the screen

        x = (screen_width // 2) - (width // 2) # calculates the x position
        y = (screen_height // 2) - (height // 2) # calculates the y position

        window.geometry(f'{width}x{height}+{x}+{y}')
        window.title(title)
        window.resizable(False,False)
        return window


    def draw_tree(x, y, length, angle, canvas, iteration, branch_angle , length_ratio: float ,tag, first_iter = True,):
        if iteration == 0:
            return
        

        current_angle = 90 if first_iter else angle

        x_end = x + length * np.cos(np.radians(current_angle))
        y_end = y - length * np.sin(np.radians(current_angle))

        canvas.create_line(x, y, x_end, y_end, fill='red' , tags=tag)

        draw_tree(x_end, y_end, length * length_ratio, angle + branch_angle, canvas, iteration-1, branch_angle, length_ratio,tag, first_iter= False, )
        draw_tree(x_end, y_end, length * length_ratio, angle - branch_angle, canvas, iteration-1, branch_angle, length_ratio,tag, first_iter= False)


    def update_tree():
        # Clear the previous tree
        canvas.delete("updated")
        
        

        # Get slider values
        length = length_slider.get()
        angle = angle_slider.get()
        iterations = iteration_slider.get()
        branch_angle = branch_angle_slider.get()  # Get angle between branches value
        lengthRatio = length_ratio_slider.get()
        """
        if length == random_params['length']:
            length_slider.config(state='disabled')
        if angle == random_params['angle']:
            angle_slider.config(state='disabled')
        if iterations == random_params['iteration']:
            iteration_slider.config(state='disabled')
        if branch_angle == random_params['branch_angle']:
            branch_angle_slider.config(state='disabled')
        if lengthRatio == random_params['length_ratio']:
            length_ratio_slider.config(state='disabled')
        else:
            length_slider.config(state='normal')
            angle_slider.config(state='normal')
            iteration_slider.config(state='normal')
            branch_angle_slider.config(state='normal')
            length_ratio_slider.config(state='normal')
            """
        
        
        # Draw the updated tree
        draw_tree(600, 600, length, angle, canvas, iterations, branch_angle, lengthRatio, tag="updated", first_iter=True)
        check_match()

    def calculate_progress():
        """
        Calculate the percentage match between the user's tree and the random tree.

        Compares the user's slider values with the randomly generated tree's parameters.
        Each parameter's difference is normalised within its tolerance range, and the
        average of these normalised differences is used to calculate the match percentage.

        Returns:
            int: The match percentage (0 to 100).
        """
        length_tolerance = 2
        angle_tolerance = 2
        iteration_tolerance = 0
        branch_angle_tolerance = 2
        length_ratio_tolerance = 0.02

        # Differences between user and random parameters
        length_diff = abs(random_params['length'] - length_slider.get())
        angle_diff = abs(random_params['angle'] - angle_slider.get())
        iteration_diff = abs(random_params['iteration'] - iteration_slider.get())
        branch_angle_diff = abs(random_params['branch_angle'] - branch_angle_slider.get())
        length_ratio_diff = abs(random_params['length_ratio'] - length_ratio_slider.get())

        # Normalise the differences within tolerance ranges
        progress_length = max(0, 1 - (length_diff / length_tolerance))
        progress_angle = max(0, 1 - (angle_diff / angle_tolerance))
        progress_iteration = max(0, 1 - (iteration_diff / iteration_tolerance)) if iteration_tolerance > 0 else 1
        progress_branch_angle = max(0, 1 - (branch_angle_diff / branch_angle_tolerance))
        progress_length_ratio = max(0, 1 - (length_ratio_diff / length_ratio_tolerance))

        # Average progress
        progress = (
                           progress_length +
                           progress_angle +
                           progress_iteration +
                           progress_branch_angle +
                           progress_length_ratio
                   ) / 5  # Divide by the number of parameters

        return int(progress * 100)  # Return percentage

    def check_match():
        """
        Check if the user's tree matches the random tree and update progress.

        Compares the user's slider values with the random tree parameters. If the progress
        reaches 100%, the sliders are disabled, and the congratulatory window is shown.
        Otherwise, the progress label is updated dynamically.

        Returns:
            None
        """
        global progress_label
        try:
            if 'congrat_win' in globals() and congrat_win.winfo_exists():
                congrat_win.destroy()
        except tk.TclError:
            pass

        if 'congrat_win' in globals():
            congrat_win.destroy()

        # Calculate the progress percentage
        progress = calculate_progress()
        progress_label.config(text=f"Progress: {progress}%")  # Update the label dynamically

        if progress == 100:
            length_slider.config(state='disabled')
            angle_slider.config(state='disabled')
            iteration_slider.config(state='disabled')
            branch_angle_slider.config(state='disabled')
            length_ratio_slider.config(state='disabled')
            show_congratulations()

    def show_congratulations():
    

        global congrat_win
        congrat_win = tk.Toplevel(win)
        centrum_window(congrat_win, "Congratulations!", 300, 300) # Centers the window on the screen
        
        

        
        restart_button = tk.Button(congrat_win, text="Restart", command= lambda: restart())
        congrat_label = tk.Label(congrat_win, text="Congratulations! \n "
                                'You\'ve matched the random tree!', font=("Arial", 14))
        exit_button = tk.Button(congrat_win, text="Exit", command= lambda: exit_app())
        congrat_label.pack(padx=10, pady=10)
        restart_button.pack(padx=10, pady=10)
        exit_button.pack(padx=10, pady=10)

    def update_tree():
        canvas.delete("updated")

        length = length_slider.get()
        angle = angle_slider.get()
        iterations = iteration_slider.get()
        branch_angle = branch_angle_slider.get()
        lengthRatio = length_ratio_slider.get()

        draw_tree(600, 600, length, angle, canvas, iterations, branch_angle, lengthRatio, tag="updated",
                  first_iter=True)
        check_match()


    def generate_random_tree():
        global random_params
        random_params = {
            'x': 300,
            'y': 600,
            'length': randint(80, 180),
            'angle': randint(0, 180),
            'canvas': canvas,
            'iteration': randint(3, 6),
            'branch_angle': randint(10, 90),
            'length_ratio': randint(1, 100) / 100
        }
        print(random_params)
        draw_tree(**random_params, first_iter=True , tag="random")



    global win, progress_label


    win = tk.Tk()   
    centrum_window(win, "Tree Matching Game", 1200, 800) # Centers the window on the screen

    # Add a progress label
    progress_label = tk.Label(win, text="Progress: 0%", font=("Arial", 14), fg="blue")
    progress_label.pack(pady=(10, 0))

    canvas = tk.Canvas(win, bg='green', width=1000, height=600)
    ScalesLabel = tk.LabelFrame(win, text="Adjust Tree Parameters", font=("Arial", 14), padx=10, pady=10)

    # Create sliders for controlling the tree's parameters
    length_slider = tk.Scale(ScalesLabel, from_=50, to=200, orient=tk.HORIZONTAL, label="Initial Branch Length", resolution=1, command=lambda e: update_tree() , length=200)
    length_slider.set(100)
    length_slider.grid(row=0, column=0, padx=10, pady=10)

    angle_slider = tk.Scale(ScalesLabel, from_=0, to=180, orient=tk.HORIZONTAL, label="Branch Angle", resolution=1, command=lambda e: update_tree() , length=200)
    angle_slider.set(45)
    angle_slider.grid(row=0, column=1, padx=10, pady=10)

    iteration_slider = tk.Scale(ScalesLabel, from_=1, to=10, orient=tk.HORIZONTAL, label="Iterations", resolution=1, command=lambda e: update_tree() , length=200)
    iteration_slider.set(6)
    iteration_slider.grid(row=0, column=2, padx=10, pady=10)
    # Add a slider for controlling the angle between the branches
    branch_angle_slider = tk.Scale(ScalesLabel, from_=0, to=90, orient=tk.HORIZONTAL, label="Angle Between Branches", resolution=1, command=lambda e: update_tree() , length=200)
    branch_angle_slider.set(30)
    branch_angle_slider.grid(row=0, column=3, padx=10, pady=10)

    length_ratio_slider = tk.Scale(ScalesLabel, from_=0.1, to=1, orient=tk.HORIZONTAL, label="Length Ratio", resolution=0.01, command= lambda e: update_tree(),  length=200)
    length_ratio_slider.set(0.7)
    length_ratio_slider.grid(row=0, column=4, padx=10, pady=10)



    generate_random_tree()

    update_tree()



    canvas.pack(padx=10, pady=10)
    ScalesLabel.pack(padx=10, pady=10)
    win.mainloop()

start()

