# -*- coding: utf-8 -*-
"""
Created on Tue Oct 02 22:01:00 2019

@author: Nguyen Tien Nam
"""

import sys
import os

from PyQt5 import QtCore
from PyQt5 import QtWidgets

from ui_editor_window import Ui_EditorWindow
from rotation_dialog import RotationDialog

from wrapper import WindowWrapper
from state import State
from images import Image
from log import LOG

import siso

class EditorWindow(WindowWrapper):
    ### Constructor
    def __init__(self, _parentWidget, originalImg):
        # Initialize attributes of QtWidgets.QparentWidget
        if 3 > sys.version_info[0]:
            # Python 2
            super(EditorWindow, self).__init__()
            
        else:
            # Python 3
            super().__init__()
            
        
        # Initialize UI components
        self.ui = Ui_EditorWindow()
        self.ui.setupUi(self)
        
        # Map labelCanvas pointer to the real instance
        self.labelCanvas = self.ui.labelCanvas
        
        # Widget to be deleted when it is closed
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        
        # Actions
        self.ui.actionCrop.triggered.connect(self.actionCropClickEvt)
        self.ui.actionRotate.triggered.connect(self.actionRotateClickEvt)
        self.ui.actionSave.triggered.connect(self.actionSaveClickEvt)
        self.ui.actionReset.triggered.connect(self.actionResetClickEvt)
        
        # Initialize specific attributes
        self.parentWidget = _parentWidget
        self.originalImg = originalImg
        self.editingImage = Image(Image.BY_DATA, originalImg.data)
        self.curState = State()
        
        # Set title
        imageFileName = originalImg.name.split('.')[0]
        self.setWindowTitle(imageFileName)
        
        # Display Editing Image
        self.display(self.editingImage)
        self.show()
        
    
    ### Destructor
    def __del__(self):
        LOG(self, ' Finalizing ' + self.windowTitle() + ' Window')
        
    
    ### Transformation
    # Flip Horizontal
    def flipHorizontal(self):
        # Rotate Editing Image
        self.editingImage = siso.rotate(self.originalImg, self.curState.rotationAngle)
        
        # Check Flip State
        if self.curState.flippedV:
            self.editingImage = siso.flip(self.editingImage, siso.FLIP_V)
            
        if self.curState.flippedH:
            self.curState.flippedH = False
            
        else:
            self.curState.flippedH = True
            self.editingImage = siso.flip(self.editingImage, siso.FLIP_H)
            
        # Display Rotated Image
        self.display(self.editingImage)
        
    
    # Flip Vetical
    def flipVertical(self):
        # Rotate Editing Image
        self.editingImage = siso.rotate(self.originalImg, self.curState.rotationAngle)
        
        # Check Flip State
        if self.curState.flippedH:
            self.editingImage = siso.flip(self.editingImage, siso.FLIP_H)
            
        if self.curState.flippedV:
            self.curState.flippedV = False
            
        else:
            self.curState.flippedV = True
            self.editingImage = siso.flip(self.editingImage, siso.FLIP_V)
            
        # Display Rotated Image
        self.display(self.editingImage)
        
    
    def getRotationAngle(self):
        return self.curState.rotationAngle
        
    
    def setRotationAngle(self, _rotationAngle):
        # Reset Editing Image
        self.editingImage = self.originalImg
        
        # Update current state
        self.curState.rotationAngle = _rotationAngle
        
        # Check Flip State
        if self.curState.flippedV:
            self.editingImage = siso.flip(self.editingImage, siso.FLIP_V)
        
        if self.curState.flippedH:
            self.editingImage = siso.flip(self.editingImage, siso.FLIP_H)
        
        # Rotate Editing Image
        self.editingImage = siso.rotate(self.editingImage, self.curState.rotationAngle)
        
        # Display Rotated Image
        self.display(self.editingImage)
        
    
    ### Event Handlers
    def actionCropClickEvt(self):
        print('EditorWindow.actionCropClickEvt')
        
    
    def actionRotateClickEvt(self):
        rotationDiaglog = RotationDialog(self)
        self.subWidgets.append(rotationDiaglog)
        
    
    def actionSaveClickEvt(self):
        print('EditorWindow.actionSaveClickEvt')
        
    
    def actionResetClickEvt(self):
        print('EditorWindow.actionResetClickEvt')
        
    
