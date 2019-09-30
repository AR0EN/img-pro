# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 22:00:00 2019

@author: Le Huy Hoang
"""

import sys

print("Checking dependencies:")

result = True

# OpenCV
try:
    import cv2
    print("\tOpenCV: " + cv2.__version__ + " -- passed!")
    
except:
    result = False
    print("\tOpenCV: " + " -- failed!")


# PyQt5
try:
    from PyQt5.Qt import PYQT_VERSION_STR
    print("\tPyQt: " + PYQT_VERSION_STR + " -- passed!")
    
except:
    result = False
    print("\tPyQt: " + " -- failed!")

print('')

# Return
if result:
    sys.exit(0)
    
else:
    sys.exit(1)
