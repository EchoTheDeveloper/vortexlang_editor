import tkinter as tk
from tkinter import filedialog, font
import toml
import preferences as menuone
from config import *
import subprocess
import platform
import os

def open_terminal():
    current_directory = os.getcwd()
    os_type = platform.system()

    if os_type == "Darwin":  # macOS
        subprocess.run(["open", "-a", "Terminal", current_directory])
    elif os_type == "Linux":  # Linux
        # For GNOME Terminal, the `--working-directory` flag sets the initial directory
        subprocess.run(["gnome-terminal", "--working-directory", current_directory])
    elif os_type == "Windows":  # Windows
        # Use PowerShell to open the terminal in the specified directory
        subprocess.run(["powershell", "-NoExit", "-Command", f"Set-Location -Path '{current_directory}'"])
    else:
        print("Unsupported OS")

settings_file = "resources/settings.toml"
with open(settings_file, "r") as file:
    settings = toml.load(file)

root = tk.Tk()
root.title(root_title)
root.geometry('600x400')

text = tk.Text(root,
               wrap="word",
               undo=True,
               bg=settings['editor']['background_color'],        # Background color
               fg=settings['editor']['foreground_color'],        # Foreground color (text color)
               font=(settings['editor']['font'], settings['editor']['font_size']))  # Font and font size

tab_width = tk.font.Font(font=text['font']).measure(' ' * 4)
text.config(tabs=(tab_width,))

text.pack(expand="yes", fill="both")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

def new_file():
    text.delete("1.0", tk.END)
    root.title(f'{root_title} | {version}')

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".vlang",
                                           filetypes=[("Vortexlang Files", "*.vlang")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text.delete("1.0", tk.END)
            text.insert(tk.END, content)
        root.title(file_path)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".vlang", filetypes=[("Vortexlang Files", "*.vlang")])
    if file_path:
        with open(file_path, "w") as file:
            content = text.get("1.0", tk.END)
            file.write(content)
        root.title(file_path)

def preferences():
    menuone.run(root, text)

file_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu = tk.Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label=menubar_file_title, menu=file_menu)
file_menu.add_command(label=menubar_file_new, command=new_file)
file_menu.add_command(label=menubar_file_open, command=open_file)
file_menu.add_command(label=menubar_file_save, command=save_file)
file_menu.add_command(label=menubar_file_terminal, command=open_terminal)
file_menu.add_separator()
file_menu.add_command(label=menubar_file_exit, command=root.destroy)

menu_bar.add_cascade(label=menubar_edit_title, menu=edit_menu)
edit_menu.add_command(label=menubar_edit_preferences, command=preferences)

# Set fullscreen if the option is enabled
if settings['editor']['fullscreen']:
    root.attributes("-fullscreen", True)

root.mainloop()
