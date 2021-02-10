# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 19:58:00 2019

@author: Le Huy Hoang
"""

import sys

import cv2
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QImage

from images import Image
from log import LOG

class WindowWrapper(QtWidgets.QMainWindow):
    ### Static attributes
    
    ### Static methods
    
    ### Constructor
    def __init__(self):
        # Initialize attributes of QtWidgets.QMainWindow
        if 3 > sys.version_info[0]:
            # Python 2
            super(WindowWrapper, self).__init__()
            
        else:
            # Python 3
            super().__init__()
            
        # Initialize parent widget
        self.parentWidget = None
        
        # Initialize the list of sub-widgets
        self.subWidgets = []
        
        self.labelCanvas = None
        
    
    # Display an image
    def display(self, displayImg):
        if None != displayImg:
            if displayImg.valid:
                displayData = displayImg.displayData
                
                # Resize
                displayWidth = self.labelCanvas.width()
                displayHeight = self.labelCanvas.height()
                height, width, _ = displayData.shape
                hFactor = float(displayHeight)/height
                wFactor = float(displayWidth)/width

                if (wFactor > hFactor) and (displayHeight < height):
                    height = displayHeight
                    width = int(width * hFactor)
                    imgDataResized = cv2.resize(displayData,(width,height), interpolation=Image.INTERPOLATION_METHOD)

                elif (wFactor < hFactor) and (displayWidth < width):
                    height = int(height * wFactor)
                    width = displayWidth
                    imgDataResized = cv2.resize(displayData,(width,height), interpolation=Image.INTERPOLATION_METHOD)

                elif (displayHeight < height):
                    height = displayHeight
                    width = displayWidth
                    imgDataResized = cv2.resize(displayData,(displayWidth, displayHeight), interpolation=Image.INTERPOLATION_METHOD)
                else:
                    imgDataResized = displayData

                bytesPerLine = 3 * width
                qImg = QImage(imgDataResized, width, height, bytesPerLine, QImage.Format_RGB888)
                
                pixmap = QPixmap(qImg)
                self.labelCanvas.setPixmap(pixmap)

            else:
                pass
                
            
        else:
            pass
            
        
    
    # Remove a SubWidget
    def removeSubWidget(self, subWidget):
        self.subWidgets.remove(subWidget)
        
    
    ### Event Handlers
    def closeEvent(self, event):
        LOG(self, 'Closing ' + self.windowTitle() + ' Window')
        # Terminate sub-attributes/processes
        for subWidget in self.subWidgets:
            # Remove the link to Parent Widget
            subWidget.parentWidget = None
            subWidget.close()
            
        self.subWidgets.clear()
        
        # Notify Parent Widget
        if None != self.parentWidget:
            self.parentWidget.removeSubWidget(self)
        
        # Call QtWidgets.QMainWindow 's procedure
        if 3 > sys.version_info[0]:
            # Python 2
            super(WindowWrapper, self).closeEvent(event)
            
        else:
            # Python 3
            super().closeEvent(event)
            
        
    

class DialogWrapper(QtWidgets.QDialog):
    ### Static attributes
    
    ### Static methods
    
    ### Constructor
    def __init__(self):
        # Initialize attributes of QtWidgets.QMainWindow
        if 3 > sys.version_info[0]:
            # Python 2
            super(DialogWrapper, self).__init__()
            
        else:
            # Python 3
            super().__init__()
            
        # Initialize parent widget
        self.parentWidget = None
        
        # Initialize the list of sub-widgets
        self.subWidgets = []
        
    
    # Remove a SubWidget
    def removeSubWidget(self, subWidget):
        self.subWidgets.remove(subWidget)
        
    
    ### Event Handlers
    def closeEvent(self, event):
        LOG(self, 'Closing ' + self.windowTitle() + ' Window')
        # Terminate sub-attributes/processes
        for subWidget in self.subWidgets:
            # Remove the link to Parent Widget
            subWidget.parentWidget = None
            subWidget.close()
            
        self.subWidgets.clear()
        
        # Notify Parent Widget
        if None != self.parentWidget:
            self.parentWidget.removeSubWidget(self)
        
        # Call QtWidgets.QMainWindow 's procedure
        if 3 > sys.version_info[0]:
            # Python 2
            super(DialogWrapper, self).closeEvent(event)
            
        else:
            # Python 3
            super().closeEvent(event)
            
        
    