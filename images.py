# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:55:37 2019

@author: Le Huy Hoang
"""

import os

import cv2

import numpy as np

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QListWidget, QListWidgetItem

class Image:
    # Initiation Types
    BY_PATH = 0
    BY_DATA = 1
    
    # Supported Image Formats (refer to OpenCV imread() for more details)
    SUPPORT_FORMAT = '(*.bmp *.dib *.jpeg *.jpg *.png *.pbm *.pgm *.ppm *.tiff *.tif)'
    INTERPOLATION_METHOD = cv2.INTER_AREA
    
    # Create a new Image instance with path to image file
    def __init__(self, initiationType, arg):
        if Image.BY_PATH == initiationType:
            # arg is full path to image file
            if '' != arg:
                self.filePath = arg
                self.name = os.path.basename(arg)
                self.data = cv2.imread(arg, cv2.IMREAD_UNCHANGED)
                self.displayData = Image.convertToRGBU8(self.data)
                if isinstance(self.data, type(None)):
                    self.valid = False
                    
                else:
                    self.valid = True
                    
            else:
                self.valid = False
            
        elif Image.BY_DATA == initiationType:
            # arg is image data
            self.filePath = None
            self.name = None
            self.data = arg
            self.displayData = Image.convertToRGBU8(self.data)
            self.valid = True
            
        else:
            # Unrecognized initiationType
            print('[Image.__init__()] Unrecognized initiationType: ' + str(initiationType))
            self.filePath = None
            self.name = None
            self.data = None
            self.displayData = None
            self.valid = False
            
        
    # Convert input data int 8-bit RGB data (for display purpose)
    @staticmethod
    def convertToRGBU8(inputData):
        if (np.dtype(np.uint16) == inputData.dtype) :
            dataBGRU8 = (np.right_shift(inputData, 8)).astype(np.uint8)
        else:
            dataBGRU8 = inputData
        
        # Convert BGR to RGB
        b,g,r = cv2.split(dataBGRU8)
        dataRGBU8 = cv2.merge([r,g,b])
        
        return dataRGBU8
    

class Images():
    # Maximum Size of the queue
    MAX_SIZE = 7
    
    def __init__(self, _listWidget):
        self.listWidget = _listWidget
        self.images = []
        
        
    def addImage(self, _path):
        if (Images.MAX_SIZE > len(self.images)):
            # Read the image
            img = Image(Image.BY_PATH, _path)
            
            if (img.valid):
                # Add image to the queue
                self.images.append(img)
                
                # Update list widget
                item = QListWidgetItem(img.name)
                item.setCheckState(Qt.Checked)
                item.setCheckState(Qt.Checked)
                self.listWidget.addItem(item)
                
            else:
                pass
            
        else:
            pass
    
    def removeImage(self, _index):
        if (0 <= _index) and (len(self.imageList) > _index):
            del self.imageList[_index]
            self.listWidget.removeItemWidget(self.listWidget.item(_index))
        else:
            pass
    
    # Import images
    def importImages(self):
        fileBrowser = QFileDialog()
        fileBrowser.setFileMode(QFileDialog.ExistingFiles)
        fileBrowser.setNameFilter('Images ' + Image.SUPPORT_FORMAT)
        if fileBrowser.exec_():
            filePaths = fileBrowser.selectedFiles()
            for path in filePaths:
                self.addImage(path)
            
            lastItem = self.listWidget.item(self.listWidget.count() - 1)
            self.listWidget.setCurrentItem(lastItem)
        else:
            pass
        
        return
