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


class Main():
    SUPPORT_FORMAT = '(*.bmp *.gif *.jpg *.jpeg *.png *.pbm *.pgm *.ppm *.xbm *.xpm *.svg)'

    def __init__(self):
        self.mainWindow = QtWidgets.QMainWindow()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self.mainWindow)
        self.imgList = Images(self.gui.listWidgetImgList)
        
        # Actions
        self.gui.actionImport.triggered.connect(self.actionImportClickEvt)
        self.gui.actionTBImport.triggered.connect(self.actionImportClickEvt)

        self.gui.actionExit.triggered.connect(self.actionExitClickEvt)
        
        self.gui.listWidgetImgList.currentItemChanged.connect(self.actionCurrentItemChangedEvt)
        
        self.mainWindow.show()
    
    # Display an image
    def display(self, _img):
        if _img.valid:
            # Convert to 8-bit if needed
            LOG(_img.name + ': ' + str(_img.data.dtype))
            if (np.dtype(np.uint16) == _img.data.dtype) :
                LOG('Converting ' + _img.name + ' to 8-bit')
                imgDataU8 = (np.right_shift(_img.data, 8)).astype(np.uint8)
            else:
                imgDataU8 = _img.data
                
            # Resize
            displayWidth = self.gui.labelCanvas.width()
            displayHeight = self.gui.labelCanvas.height()

            height, width, channel = imgDataU8.shape
            
            hFactor = float(displayHeight)/height
            wFactor = float(displayWidth)/width
            
            if (wFactor > hFactor) and (displayHeight < height):
                height = displayHeight
                width = int(width * hFactor)
                imgDataResizedU8 = cv2.resize(imgDataU8,(width,height), interpolation=Image.INTERPOLATION_METHOD)
                
            elif (wFactor < hFactor) and (displayWidth < width):
                height = int(height * wFactor)
                width = displayWidth
                imgDataResizedU8 = cv2.resize(imgDataU8,(width,height), interpolation=Image.INTERPOLATION_METHOD)
                
            elif (displayHeight < height):
                height = displayHeight
                width = displayWidth
                imgDataResizedU8 = cv2.resize(imgDataU8,(displayWidth, displayHeight), interpolation=Image.INTERPOLATION_METHOD)
            else:
                imgDataResizedU8 = imgDataU8
            
            # Convert BGR to RGB
            b,g,r = cv2.split(imgDataResizedU8)
            imgDataResizedU8 = cv2.merge([r,g,b])
            
            bytesPerLine = 3 * width
            qImg = QImage(imgDataResizedU8, width, height, bytesPerLine, QImage.Format_RGB888)
            
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
        self.imgList.importImages()

    # Exit
    def actionExitClickEvt(self):
        self.mainWindow.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())
