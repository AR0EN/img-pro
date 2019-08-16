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
from main_window import Ui_MainWindow



class Ui():
    SUPPORT_FORMAT = '(*.bmp *.gif *.jpg *.jpeg *.png *.pbm *.pgm *.ppm *.xbm *.xpm *.svg)'

    def __init__(self):
        self.mainWindow = QtWidgets.QMainWindow()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self.mainWindow)
        self.imgList = Images(self.gui.listWidgetImgList)
        
        # Actions
        self.gui.actionImport.triggered.connect(self.actionImportClickEvt)
        self.gui.actionTBImport.triggered.connect(self.actionImportClickEvt)
        
        self.gui.actionExport.triggered.connect(self.actionExportClickEvt)
        self.gui.actionTBExport.triggered.connect(self.actionExportClickEvt)
        
        self.gui.actionSave.triggered.connect(self.actionSaveClickEvt)
        self.gui.actionTBSave.triggered.connect(self.actionSaveClickEvt)
        self.gui.actionExit.triggered.connect(self.actionExitClickEvt)
        
        self.gui.listWidgetImgList.currentItemChanged.connect(self.actionCurrentItemChangedEvt)
        
        self.mainWindow.show()
    
    # Display an image
    def display(self, _img):
        if _img.valid:
            # Convert to 8-bit if needed
            print(_img.name + ': ' + str(_img.mat.dtype))
            if (np.dtype(np.uint16) == _img.mat.dtype) :
                print('Converting ' + _img.name + ' to 8-bit')
                matU8 = (np.right_shift(_img.mat, 8)).astype(np.uint8)
            else:
                matU8 = _img.mat
                
            # Resize
            displayWidth = self.gui.labelCanvas.width()
            displayHeight = self.gui.labelCanvas.height()

            height, width, channel = matU8.shape
            
            hFactor = float(displayHeight)/height
            wFactor = float(displayWidth)/width
            
            if (wFactor > hFactor) and (displayHeight < height):
                height = displayHeight
                width = int(width * hFactor)
                matU8Resized = cv2.resize(matU8,(width,height))
                
            elif (wFactor < hFactor) and (displayWidth < width):
                height = int(height * wFactor)
                width = displayWidth
                matU8Resized = cv2.resize(matU8,(width,height))
                
            elif (displayHeight < height):
                height = displayHeight
                width = displayWidth
                matU8Resized = cv2.resize(matU8,(displayWidth, displayHeight))
            else:
                matU8Resized = matU8
            
            # Convert BGR to RGB
            b,g,r = cv2.split(matU8Resized)
            matU8Resized = cv2.merge([r,g,b])
            
            bytesPerLine = 3 * width
            qImg = QImage(matU8Resized, width, height, bytesPerLine, QImage.Format_RGB888)
            
            pixmap = QPixmap(qImg)
            self.gui.labelCanvas.setPixmap(pixmap)
            
        else:
            pass
    
    # Display Current Item when it changed
    def actionCurrentItemChangedEvt(self):
        currentRow = self.gui.listWidgetImgList.currentRow()
        self.display(self.imgList.images[currentRow])

    # Import images
    def actionImportClickEvt(self):
        self.imgList.addImages()

    # Export changes to a new image
    def actionExportClickEvt(self):
        pass

    # Save changes
    def actionSaveClickEvt(self):
        pass

    # Exit
    def actionExitClickEvt(self):
        self.mainWindow.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())
