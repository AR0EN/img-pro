# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 20:34:00 2019

@author: Le Huy Hoang
"""

import os
import subprocess
import glob

from pyui_compiler import PyUiCompiler

print("Checking generated files:")

RootPath = './'

# Get the list of UI files
UiBasePath = './ui/'
UiExt = '*.ui'
UiSrcExt = '.py'

uiList = glob.glob(UiBasePath + UiExt)

# Get the list of Resource files
ResBasePath = './'
ResExt = '*.qrc'
ResSrcExt = '_rc.py'
resList = glob.glob(ResBasePath + ResExt)

# Check generated UI files
pyUiCompiler = PyUiCompiler()

for uiFilePath in uiList:
    # Get generated file name
    genFilePath = RootPath + os.path.basename(uiFilePath).split('.')[0] + UiSrcExt
    # Check if the generated file exists
    if os.path.isfile(genFilePath):
        # Check if the generated file is out of date
        if os.path.getmtime(genFilePath) < os.path.getmtime(uiFilePath):
            print(genFilePath + ' is out of date!')
            # Generate the file
            argumentList = [uiFilePath, "-o", genFilePath]
            pyUiCompiler.generate(argumentList)
            
        else:
            print(genFilePath + ' is up to date!')
            
        
    else:
        print(genFilePath + ' does not exist!')
        # Generate the file
        argumentList = [uiFilePath, "-o", genFilePath]
        pyUiCompiler.generate(argumentList)
        
# Check generated Resource files
for resFilePath in resList:
    # Get generated file name
    genFilePath = RootPath + os.path.basename(resFilePath).split('.')[0] + ResSrcExt
    # Check if the generated file exists
    if os.path.isfile(genFilePath):
        # Check if the generated file is out of date
        if os.path.getmtime(genFilePath) < os.path.getmtime(resFilePath):
            print(genFilePath + ' is out of date!')
            # Generate the file
            argumentList = ["pyrcc5", resFilePath, "-o", genFilePath]
            subprocess.call(argumentList)
            
        else:
            print(genFilePath + ' is up to date!')
            
        
    else:
        print(genFilePath + ' does not exist!')
        # Generate the file
        argumentList = ["pyrcc5", resFilePath, "-o", genFilePath]
        subprocess.call(argumentList)
        
print('')
