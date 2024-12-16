"""
This module initializes the GUI window for the game and provides a congratulatory popup.

The `initialize_gui` function creates a new Tkinter window with the title
"Fractal Matching Game" and the specified width and height. The window is not resizable.

The `create_congratulatory_popup` function creates a popup window to congratulate the user
and provides a restart button to restart the game.

Issues solved:
- Provides a consistent and non-resizable main window for the game.
- Offers a user-friendly way to restart the game after winning.
"""
import tkinter as tk


def initialize_gui() -> tk.Tk:
    window = tk.Tk()
    window.title("Fractal Matching Game")

    window.canvas = tk.Canvas(window, bg='green', width=1000, height=600)

    window.scales_label = tk.LabelFrame(window, text="Adjust Tree Parameters", font=("Arial", 14), padx=10, pady=10)

    return window

def create_congratulatory_popup(window, restart:  callable):
    congratulatory_popup = tk.Toplevel(window)

    congratulatory_popup.title("Congratulations!")
    congratulatory_popup.geometry("300x130")
    congratulatory_popup.resizable(False, False)
    restart_button = tk.Button(congratulatory_popup, text="Restart", command=lambda: (congratulatory_popup.destroy(), restart()))
    congratulatory_label = tk.Label(congratulatory_popup, text="Congratulations! \n "
                                               'You\'ve matched the random tree!', font=("Arial", 14))
    congratulatory_label.pack(padx=10, pady=10)
    restart_button.pack(padx=10, pady=10)
    window.congratulatory_popup = congratulatory_popup