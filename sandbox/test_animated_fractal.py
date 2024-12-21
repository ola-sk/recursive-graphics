from tkinter import Tk, Canvas
from sandbox.animation_helpers import fractal_canopy_with_animation, animate_fractal

# Set up the Tkinter window
root = Tk()
root.geometry("600x600")  # Set the window size

# Create a canvas to draw on
canvas = Canvas(root, bg="white", width=600, height=600)
canvas.pack()

# Create a queue for storing branch details
queue = []

# Generate the fractal and store branch details in the queue
fractal_canopy_with_animation(
canvas=canvas,
    x=300,  # Starting x-coordinate
    y=550,  # Starting y-coordinate
    n_iters=5,  # Number of recursive iterations
    init_length=100,  # Initial branch length
    n_splits=3,  # Number of branches at each split
    angle_delta=60,  # Angle spread between branches
    length_ratio=0.7,  # Shrink factor for branch length
    width=10,  # Initial branch width
    width_ratio=0.7,  # Shrink factor for branch width
    color="#000000",  # Branch color
    queue=queue  # Queue to store branches for animation
)

# Animate the fractal growth
animate_fractal(
    canvas=canvas,
    queue=queue,
    delay=100  # Delay between drawing each branch (in milliseconds)
)

# Run the Tkinter main loop
root.mainloop()
