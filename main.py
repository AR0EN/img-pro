# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:55:37 2019

@author: Le Huy Hoang
"""

import sys

import cv2

import numpy as np

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap, QImage

from images import Image, Images
from main_window import MainWindow

# Enable/Disable Debug Mode
import os

debugFlag = os.getenv('DEBUG')
print('debugFlag: ' + str(debugFlag))
if 'ON' == debugFlag:
    print('Executing application in Debug Mode!')
    def LOG(message):
        print('[Debug] ' + message)
    
else:
    print('Executing application in Optimized Mode!')
    print('Note: Set environment variable DEBUG to \'ON\' before executing to enable Debug Mode.')
    def LOG(message):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
