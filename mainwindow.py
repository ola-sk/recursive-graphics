import tkinter as tk

''' creating main application window'''
window=tk.Tk()
window.title("Fractal Matching Game")
window.geometry("600x900") #set to potrait orientation
window.resizable(False,False) # making window non resizable

'''Adds a canvas for the fractal display '''
canvas = tk.Canvas(window, bg="white", width=500, height=450)
canvas.grid(row=0, column=0, columnspan=3, pady=(20, 10), padx=(50, 0))

'''Add a frame for the sliders below the canvas'''
slidersLabels = tk.Frame(window)
slidersLabels.grid(row=1, column=0, columnspan=3, pady=10)

'''Add sliders for 8 different parameters'''
colour1Scale = tk.Scale(slidersLabels, label="Root Color", from_=0, to=360, orient=tk.HORIZONTAL, length=120)
colour1Scale.grid(row=3, column=0, padx=10, pady=10)

colour2Scale = tk.Scale(slidersLabels, label="Leaf Color", from_=0, to=360, orient=tk.HORIZONTAL, length=120)
colour2Scale.grid(row=3, column=1, padx=10, pady=10)

off_scaleScale = tk.Scale(slidersLabels, label="Angle Offset", from_=-45, to=45, orient=tk.HORIZONTAL, length=120)
off_scaleScale.grid(row=0, column=0, padx=10, pady=10)

angle_detaScale = tk.Scale(slidersLabels, label="Angle Size", from_=0, to=180, orient=tk.HORIZONTAL, length=120)
angle_detaScale.grid(row=0, column=1, padx=10, pady=10)

n_splitsScale = tk.Scale(slidersLabels, label="Number of Branches", from_=2, to=8, orient=tk.HORIZONTAL, length=120)
n_splitsScale.grid(row=1, column=0, padx=10, pady=10)

length_ratioScale = tk.Scale(slidersLabels, label="Length_Ratio", from_=0, to=1, orient=tk.HORIZONTAL, length=120)
length_ratioScale.grid(row=1, column=1, padx=10, pady=10)

init_lengthScale = tk.Scale(slidersLabels, label="Initial Length", from_=0.5, to=0.75, orient=tk.HORIZONTAL, length=120)
init_lengthScale.grid(row=2, column=0, padx=10, pady=10)

width_ratioScale = tk.Scale(slidersLabels, label="Width Ratio", from_=0.5, to=0.75, orient=tk.HORIZONTAL, length=120)
width_ratioScale.grid(row=2, column=1, padx=10, pady=10)

'''Run the Tkinter event loop'''
window.mainloop()