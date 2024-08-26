import json

curr_lang = "en_us"

# Load translations
with open(f'resources/langs/{curr_lang}.json', 'r') as file:
    translation = json.load(file)

version = "v1.0.0-beta1"

# Configuration settings
root_title = translation['root']['title']
editor_font = "resources/monofonto.otf"

##### menubar -> file #####
menubar_file_title = translation['menu_bars']['file']["title"]
menubar_file_new = translation['menu_bars']["file"]['new']
menubar_file_open = translation['menu_bars']["file"]['open']
menubar_file_save = translation['menu_bars']["file"]['save']
menubar_file_terminal = "translation['menu_bars']['file']['terminal']"
menubar_file_exit = translation['menu_bars']["file"]['exit']

##### menubar -> settings #####
menubar_edit_title = translation['menu_bars']['edit']['title']
menubar_edit_preferences = translation['menu_bars']['edit']['preferences']

#### menus -> preferences ####
menus_preferences_title = translation['menus']['preferences']['title']
