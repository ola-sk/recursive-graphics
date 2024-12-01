import tkinter as tk

# Create main application window
window=tk.Tk()
window.title("Fractal Matching Game") 
window.geometry("600x750") # Set to portrait orientation
window.resizable(False,False) # Making window non-resizable

# Add a canvas for the fractal display
canvas = tk.Canvas(window, bg="white", width=500, height=450)
canvas.grid(row=0, column=0, columnspan=3, pady=(20, 10), padx=(50, 0))

# Add a frame for the sliders below the canvas
slidersLabels = tk.Frame(window)
slidersLabels.grid(row=1, column=0, columnspan=3, pady=10)

# Add sliders for 6 different parameters
off_scaleScale = tk.Scale(slidersLabels, label="off_scale", from_=0, to=100, orient=tk.HORIZONTAL, length=120)
off_scaleScale.grid(row=0, column=0, padx=10, pady=10)

angle_detaScale = tk.Scale(slidersLabels, label="angle_deta", from_=0, to=100, orient=tk.HORIZONTAL, length=120)
angle_detaScale.grid(row=0, column=1, padx=10, pady=10)

n_splitsScale = tk.Scale(slidersLabels, label="n_splits", from_=0, to=100, orient=tk.HORIZONTAL, length=120)
n_splitsScale.grid(row=1, column=0, padx=10, pady=10)

length_ratioScale = tk.Scale(slidersLabels, label="length_ratio", from_=0, to=100, orient=tk.HORIZONTAL, length=120)
length_ratioScale.grid(row=1, column=1, padx=10, pady=10)

init_lengthScale = tk.Scale(slidersLabels, label="init_length", from_=0, to=100, orient=tk.HORIZONTAL, length=120)
init_lengthScale.grid(row=2, column=0, padx=10, pady=10)

width_ratioScale = tk.Scale(slidersLabels, label="width_ratio", from_=0, to=100, orient=tk.HORIZONTAL, length=120)
width_ratioScale.grid(row=2, column=1, padx=10, pady=10)

# Run the Tkinter event loop
window.mainloop()
