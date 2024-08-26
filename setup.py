from setuptools import setup

APP = ['vortexlang_editor.py']  # Your main script
DATA_FILES = ['resources']  # Include your resources folder if you have one
OPTIONS = {
    'argv_emulation': True,
    'packages': [],  # No additional packages needed since you're using built-in libraries
    'plist': {
        'CFBundleName': 'Vortexlang Editor',  # Application name
        'CFBundleShortVersionString': '1.0.0',
        'CFBundleIdentifier': 'com.yourname.vortexlangeditor',  # Customize with your identifier
        'CFBundleDevelopmentRegion': 'English',
        'CFBundleDisplayName': 'Vortexlang Editor',
    },
    'includes': [],  # Add additional packages if necessary
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
