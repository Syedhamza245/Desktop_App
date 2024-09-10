import subprocess
import tkinter as tk
from tkinter import messagebox
import os

BACKGROUND_COLOR = '#2e2e2e'
TEXT_COLOR = '#f0f0f0'
BUTTON_COLOR = '#4a4a4a'
BUTTON_HOVER_COLOR = '#6a6a6a'

selection_window = None

folder_paths = {
    "s": "therapy/Letter_s",
    "p": "therapy/Letter_p",
    "k": "therapy/Letter_k"
}

def open_letter_selection_window():
    global selection_window
    if selection_window is not None:
        selection_window.destroy()

    selection_window = tk.Toplevel(root)
    selection_window.title("Select Letter")
    selection_window.configure(bg=BACKGROUND_COLOR)

    tk.Label(selection_window, text="Select Letter:", bg=BACKGROUND_COLOR, fg=TEXT_COLOR).pack(pady=5)
    letter_options = ['s', 'p', 'k']
    letter_var = tk.StringVar(value=letter_options[0])
    letter_menu = tk.OptionMenu(selection_window, letter_var, *letter_options)
    letter_menu.config(bg=BUTTON_COLOR, fg=TEXT_COLOR, activebackground=BUTTON_HOVER_COLOR)
    letter_menu.pack(pady=5)

    submit_button = tk.Button(selection_window, text="Submit", command=lambda: handle_letter_selection(letter_var.get()), bg=BUTTON_COLOR, fg=TEXT_COLOR, activebackground=BUTTON_HOVER_COLOR)
    submit_button.pack(pady=10)

def handle_letter_selection(letter):
    folder_path = folder_paths.get(letter)
    if folder_path:
        level_stages_file = os.path.join(folder_path, "level_stages.py")
        if os.path.exists(level_stages_file):
            try:
                subprocess.run(['python', level_stages_file], check=True)
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"Failed to run {level_stages_file}: {str(e)}")
        else:
            messagebox.showerror("Error", f"level_stages.py not found in {folder_path}")
    else:
        messagebox.showerror("Error", "Invalid letter selection.")

root = tk.Tk()
root.title("Letter Selector")
root.configure(bg=BACKGROUND_COLOR)

open_letter_selection_window()
root.mainloop()
