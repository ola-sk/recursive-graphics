from tkinter import Tk, Canvas

def canvas_setup(geometry_x, geometry_y, *draw_funcs):
    # Creating main application window
    window = Tk()
    window.title("Fractal Matching Game")
    window.geometry(str(geometry_x)+"x"+str(geometry_y))    # Set window size
    window.resizable(False, False)              # Make window non-resizable

    # create a canvas
    canvas = Canvas(bg="white", height=geometry_y, width=geometry_x)
    canvas.grid(row=0, column=0)

    for draw_func in draw_funcs:
        draw_func(canvas)

    # Run the Tkinter event loop
    window.mainloop()
    return
