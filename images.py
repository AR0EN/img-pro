# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:55:37 2019

@author: Le Huy Hoang
"""

import os

import cv2

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QListWidget, QListWidgetItem

class Image:
    # Supported Image Formats (refer to OpenCV imread() for more details)
    SUPPORT_FORMAT = '(*.bmp *.dib *.jpeg *.jpg *.png *.pbm *.pgm *.ppm *.tiff *.tif)'
    INTERPOLATION_METHOD = cv2.INTER_AREA
    
    def __init__(self, _fullPath):
        if '' != _fullPath:
            self.filePath = _fullPath
            self.name = os.path.basename(_fullPath)
            self.data = cv2.imread(_fullPath, cv2.IMREAD_UNCHANGED)
            if isinstance(self.data, type(None)):
                self.valid = False
                
            else:
                self.valid = True
            
        else:
            self.valid = False


class Images():
    # Maximum Size of the queue
    MAX_SIZE = 7
    
    def __init__(self, _listWidget):
        self.listWidget = _listWidget
        self.images = []
        
        
    def addImage(self, _path):
        if (Images.MAX_SIZE > len(self.images)):
            # Read the image
            img = Image(_path)
            
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
