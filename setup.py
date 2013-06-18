"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup, find_packages

APP = ['vtr/app/app.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': True}

setup(
    name='VTR Controller',
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    packages=find_packages('src')
    install_requires=['wxPython'],
)
