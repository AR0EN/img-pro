# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:55:37 2019

@author: Le Huy Hoang
"""

import cv2

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap, QImage

from images import Image
from main_window import Ui_MainWindow

import sys

class Ui():
    SUPPORT_FORMAT = '(*.bmp *.gif *.jpg *.jpeg *.png *.pbm *.pgm *.ppm *.xbm *.xpm *.svg)'

    def __init__(self):
        self.mainWindow = QtWidgets.QMainWindow()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self.mainWindow)
        # Actions
        self.gui.actionOpen.triggered.connect(self.actionOpenClickEvt)
        self.gui.actionTBOpen.triggered.connect(self.actionOpenClickEvt)
        
        self.gui.actionExport.triggered.connect(self.actionExportClickEvt)
        self.gui.actionTBExport.triggered.connect(self.actionExportClickEvt)
        
        self.gui.actionSave.triggered.connect(self.actionSaveClickEvt)
        self.gui.actionTBSave.triggered.connect(self.actionSaveClickEvt)
        self.gui.actionExit.triggered.connect(self.actionExitClickEvt)
        self.mainWindow.show()

    # Open an image
    def actionOpenClickEvt(self):
        img = Image.browse()
        if img.valid:
            displayWidth = self.gui.labelCanvas.width()
            displayHeight = self.gui.labelCanvas.height()
            
            
            height, width, channel = img.mat.shape
            
            hFactor = float(displayHeight)/height
            wFactor = float(displayWidth)/width
            
            if (wFactor > hFactor) and (displayHeight < height):
                height = displayHeight
                width = int(width * hFactor)
                resizedImg = cv2.resize(img.mat,(width,height))
                
            elif (wFactor < hFactor) and (displayWidth < width):
                height = int(height * wFactor)
                width = displayWidth
                resizedImg = cv2.resize(img.mat,(width,height))
                
            elif (displayHeight < height):
                height = displayHeight
                width = displayWidth
                resizedImg = cv2.resize(img.mat,(displayWidth, displayHeight))
            else:
                resizedImg = img.mat
            
            bytesPerLine = 3 * width
            qImg = QImage(resizedImg, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
            
            pixmap = QPixmap(qImg)
            self.gui.labelCanvas.setPixmap(pixmap)

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
