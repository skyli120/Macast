"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

import os
from setuptools import setup

APP = ['Macast.py']
DATA_FILES = ['xml', '.version', 'i18n', 'assets']
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps'],
    'iconfile': os.path.abspath('assets/icon.icns')
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    py_modules=['mpv', 'utils', 'ssdp', 'plugin']
)
