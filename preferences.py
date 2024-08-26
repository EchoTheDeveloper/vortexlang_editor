import tkinter as tk
from tkinter import colorchooser, simpledialog
import toml
import os

# Path to the settings file
settings_file = "resources/settings.toml"

if os.path.exists(settings_file):
    with open(settings_file, "r") as file:
        settings = toml.load(file)
else:
    settings = {
        "editor": {
            "font_size": 16,
            "background_color": "#292a2d",
            "foreground_color": "#ffffff",
            "font": "resources/monofonto.otf",
            "fullscreen": False
        }
    }
    with open(settings_file, "w") as file:
        toml.dump(settings, file)

# Save settings function
def save_settings():
    with open(settings_file, "w") as file:
        toml.dump(settings, file)

# Apply changes to the main application
def apply_changes(root, text):
    text.config(bg=settings['editor']['background_color'],
                fg=settings['editor']['foreground_color'],
                font=(settings['editor']['font'], settings['editor']['font_size']))
    if settings['editor']['fullscreen']:
        root.attributes("-fullscreen", True)
    else:
        root.attributes("-fullscreen", False)
    root.update_idletasks()

# Preferences window
def run(root, text):
    def set_font_size():
        font_size = simpledialog.askinteger("Font Size", "Enter font size:", initialvalue=settings['editor']['font_size'])
        if font_size:
            settings['editor']['font_size'] = font_size
            save_settings()

    def set_background_color():
        color = colorchooser.askcolor(initialcolor=settings['editor']['background_color'])[1]
        if color:
            settings['editor']['background_color'] = color
            save_settings()

    def set_foreground_color():
        color = colorchooser.askcolor(initialcolor=settings['editor']['foreground_color'])[1]
        if color:
            settings['editor']['foreground_color'] = color
            save_settings()

    def set_font():
        font_name = simpledialog.askstring("Font", "Enter font path:", initialvalue=settings['editor']['font'])
        if font_name:
            settings['editor']['font'] = font_name
            save_settings()

    def toggle_fullscreen():
        settings['editor']['fullscreen'] = not settings['editor']['fullscreen']
        save_settings()

    def reset_settings():
        global settings
        settings = {
            "editor": {
                "font_size": 16,
                "background_color": "#292a2d",
                "foreground_color": "#ffffff",
                "font": "resources/monofonto.otf",
                "fullscreen": False
            }
        }
        save_settings()
        apply_changes(root, text)

    def apply_changes_and_update():
        apply_changes(root, text)

    pref_window = tk.Toplevel()
    pref_window.title("Preferences")

    tk.Button(pref_window, text="Set Font Size", command=set_font_size).pack(pady=5)
    tk.Button(pref_window, text="Set Background Color", command=set_background_color).pack(pady=5)
    tk.Button(pref_window, text="Set Foreground Color", command=set_foreground_color).pack(pady=5)
    tk.Button(pref_window, text="Set Font", command=set_font).pack(pady=5)
    tk.Checkbutton(pref_window, text="Start in Fullscreen", command=toggle_fullscreen,
                   variable=tk.BooleanVar(value=settings['editor']['fullscreen'])).pack(pady=5)
    tk.Button(pref_window, text="Apply Changes", command=apply_changes_and_update).pack(pady=5)
    tk.Button(pref_window, text="Reset to Default", command=reset_settings).pack(pady=5)

    pref_window.mainloop()
