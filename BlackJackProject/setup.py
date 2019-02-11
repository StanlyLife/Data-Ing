#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 18:07:09 2018

@author: Stian
"""

from setuptools import setup

APP = ['blackJackGUI.py']
DATA_FILES = []
OPTIONS = {
 'iconfile':'logoapp.png',
 'argv_emulation': True,
 'packages': ['certifi'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)