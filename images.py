# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:55:37 2019

@author: Le Huy Hoang
"""

import os

import numpy as np
import cv2

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Image:
    # Supported Image Formats (refer to OpenCV imread() for more details)
    SUPPORT_FORMAT = '(*.bmp *.dib *.jpeg *.jpg *.png *.pbm *.pgm *.ppm *.tiff *.tif)'
    
    def __init__(self, _fullPath):
        if '' != _fullPath:
            self.fullPath = _fullPath
            self.name = os.path.basename(_fullPath)
            self.mat = cv2.imread(_fullPath, cv2.IMREAD_UNCHANGED)
            if isinstance(self.mat, type(None)):
                self.valid = False
                
            else:
                self.valid = True
            
        else:
            self.valid = False

    def getData(self):
        return self.mat.data

    # Browse an image
    @staticmethod
    def browse():
        fileBrowser = QFileDialog()
        fileBrowser.setFileMode(QFileDialog.ExistingFile)
        fileBrowser.setNameFilter('Images ' + Image.SUPPORT_FORMAT)
        if fileBrowser.exec_():
            fileNames = fileBrowser.selectedFiles()
            img = Image(fileNames[0])
        else:
            img = Image('')
        
        return img
