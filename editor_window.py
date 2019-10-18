# -*- coding: utf-8 -*-
"""
Created on Tue Oct 02 22:01:00 2019

@author: Nguyen Tien Nam
"""

import sys
import os

from PyQt5 import QtWidgets
from ui_editor_window import Ui_EditorWindow
from rotation_dialog import RotationDialog

from wrapper import CommonFunctions

from images import Image

import siso

from state import State

from log import LOG

class EditorWindow(QtWidgets.QMainWindow):
    def __init__(self, _mainWindow, imported_image):
        # Initialize attributes of QtWidgets.QMainWindow
        if 3 > sys.version_info[0]:
            # Python 2
            super(EditorWindow, self).__init__()
            
        else:
            # Python 3
            super().__init__()
        
        self.mainWindow = _mainWindow
        self.imported_image = imported_image
        self.editingImage = Image(Image.BY_DATA, imported_image.data)
        self.curState = State()
        
        self.ui = Ui_EditorWindow()
        self.ui.setupUi(self)
        
        self.subDialogs = []
        
        # Actions
        self.ui.actionCrop.triggered.connect(self.actionCropClickEvt)
        self.ui.actionRotate.triggered.connect(self.actionRotateClickEvt)
        self.ui.actionSave.triggered.connect(self.actionSaveClickEvt)
        self.ui.actionReset.triggered.connect(self.actionResetClickEvt)
                
        # Set title
        imageFileName = imported_image.name.split('.')[0]
        self.setWindowTitle(imageFileName)
        
        CommonFunctions.display(self.editingImage, self.ui.labelCanvas)
        self.show()
        
    def getRotationAngle(self):
        return self.curState.rotationAngle
    
    def setRotationAngle(self, _rotationAngle):
        # Update current state
        self.curState.rotationAngle = _rotationAngle
        
        # Rotate Editing Image
        self.editingImage = siso.rotate(self.imported_image, self.curState.rotationAngle)
        
        # Display Rotated Image
        CommonFunctions.display(self.editingImage, self.ui.labelCanvas)
    
    def actionCropClickEvt(self):
        print('EditorWindow.actionCropClickEvt')
        pass
    
    def actionRotateClickEvt(self):
        rotationDiaglog = RotationDialog(self)
        self.subDialogs.append(rotationDiaglog)
        pass
    
    def actionSaveClickEvt(self):
        print('EditorWindow.actionSaveClickEvt')
        pass
    
    def actionResetClickEvt(self):
        print('EditorWindow.actionResetClickEvt')
        pass
    
    # Terminate an Editor Window
    def terminateSubDialog(self, subDialog):
        self.subDialogs.remove(subDialog)
    
    def closeEvent(self, event):
        LOG("[EditorWindow.closeEvent()] Closing " + self.windowTitle() + " Window")
        # Notify MainWindow
        self.mainWindow.terminateSubWindow(self)
        
        # Terminate sub-attributes/processes
        
        # Call QtWidgets.QMainWindow 's procedure
        if 3 > sys.version_info[0]:
            # Python 2
            super(EditorWindow, self).closeEvent(event)
            
        else:
            # Python 3
            super().closeEvent(event)
            
