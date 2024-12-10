# GUI Package

This package contains modules for creating and managing the graphical user interface (GUI) for the Fractal Matching
Game. The GUI is built using the Tkinter library and includes functionalities for initializing the main window, creating
sliders for user interaction, and updating the canvas with the fractal tree.

## Modules

### `gui_init.py`

This module initializes the main GUI window for the game.

- **Functions:**
    - `initialize_gui(window_width: int = 1300, window_height: int = 900) -> tk.Tk`: Creates and returns a new Tkinter
      window with the specified width and height. The window is not resizable.

### `sliders.py`

This module provides functionalities for creating and managing sliders in the GUI. The sliders control the parameters of
the fractal tree displayed on the canvas.

- **Functions:**
    -
    `create_slider(parent: tk.Widget, parameter_name: str, label: str, from_: int | float, to: int | float, initial_value: int | float, resolution: int | float, row: int, column: int) -> tk.Scale`:
    Creates a slider and adds it to the parent widget at the specified row and column.
    - `column_sequence_generator(num_columns: int) -> tuple[int, int]`: A generator that yields the next column in the
      grid layout in the form of a tuple: (row, column).
    -
    `populate_sliders(sliders_frame: tk.Frame, canvas: tk.Canvas, sliders_init_data: Collection[tuple[str, str, int | float, int | float, int | float, int | float]], num_columns: int = 4) -> list[tk.Scale]`:
    Adds sliders for different parameters to the sliders frame and binds each slider to an event handler that updates
    the canvas with the new tree.

- **Design choices:**

  In the `populate_sliders` function, we avoid passing the `tree` variable directly to the function and to the event
  handlers it assigns to each slider.
  Instead, the handlers access the external state of a tree directly and based on what needs to be changed they call
  the update method of the tree.

    - ✅ What we want is the event handler to fetch an external state (like the current
      Fractal Tree that needs to modified), modifies it, triggers update of the _external_ state
      and then also updates the canvas with the new tree.

    - ❌ Passing the `tree` variable directly to the `populate_sliders` function (if it accepted such a parameter)
      would cause the function to always use the initial state of the `tree` that was passed.
      That's because the event handler is assigned only once. It uses whatever argument it has provided,
      it places it in its local scope at the time of initialization, and that variable never gets reassigned.

  **Advantages:**

    1. **State Consistency**: If the `tree` state changes over time (e.g., due to user interactions with the sliders)
       the
       `populate_sliders` function, and the event handlers assigned to events by it, remain in sync with the current
       external state.

    2. **Event-Driven Updates**: In a GUI application, state changes are often driven by events. By using a mechanism
       like
       callbacks (e.g., `TreeNodeBase.update_tree` within the event handler for the change of a slider's state), the
       function can trigger change to and retrieve state changes as it runs/gets triggered, ensuring that the UI remains
       in sync with the underlying data.

  In summary, avoiding passing the `tree` directly ensures that the function can respond to the current state.

## Usage

1. **Initialize the GUI:**
   ```python
   from gui.gui_init import initialize_gui

   window = initialize_gui()
   window.mainloop()
    ```
2. Create and Populate Sliders:
   ```python
   from gui.sliders import populate_sliders
    
    sliders_frame = tk.Frame(window)
    sliders_frame.pack()
    canvas = tk.Canvas(window)
    canvas.pack()
    
    sliders_init_data = [
        ("angle", "Angle", 0, 180, 90, 1),
        ("length", "Length", 10, 100, 50, 1),
        # Add more sliders as needed
    ]
    
    sliders = populate_sliders(sliders_frame, canvas, sliders_init_data)
    ```

## Dependencies