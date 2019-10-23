# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 20:50:00 2019

@author: Le Huy Hoang
"""

import sys
import os

from PyQt5 import QtWidgets
from ui_rotation_dialog import Ui_RotationDialog

from wrapper import CommonFunctions

from images import Image

from state import State

from log import LOG

class RotationDialog(QtWidgets.QDialog):
    ### Constants
    BY_DATA = 1
    
    ### Constructor
    def __init__(self, _editorWindow):
        # Initialize attributes of QtWidgets.QDialog
        if 3 > sys.version_info[0]:
            # Python 2
            super(RotationDialog, self).__init__()
            
        else:
            # Python 3
            super().__init__()
        
        self.editorWindow = _editorWindow
        
        self.ui = Ui_RotationDialog()
        self.ui.setupUi(self)
        
        # Actions
        self.ui.horizontalSliderAngle.sliderReleased.connect(self.actionHorizontalSliderAngleSliderReleasedEvt)
        self.ui.pushButtonRL.clicked.connect(self.actionPushButtonRLClickEvt)
        self.ui.pushButtonRR.clicked.connect(self.actionPushButtonRRClickEvt)
        self.ui.pushButtonFlipH.clicked.connect(self.actionPushButtonFlipHClickEvt)
        self.ui.pushButtonFlipV.clicked.connect(self.actionPushButtonFlipVClickEvt)
        
        self.show()
        
    
    ### Event Handlers
    def actionHorizontalSliderAngleSliderReleasedEvt(self):
        # Get new Rotation Angle
        rotationAngle = self.ui.horizontalSliderAngle.value()
        
        # Update Rotation Angle Text Box
        self.ui.lineEditAngle.setText(str(rotationAngle))
        
        # Notify Editor Window
        self.editorWindow.setRotationAngle(rotationAngle)
        
    
    def actionPushButtonRLClickEvt(self):
        # Calculate new Rotation Angle
        rotationAngle = self.editorWindow.getRotationAngle() - 90
        if 0 > rotationAngle:
            rotationAngle = rotationAngle + 360
        else:
            pass
            
        # Update Rotation Angle Slider
        self.ui.horizontalSliderAngle.setValue(rotationAngle)
        
        # Update Rotation Angle Text Box
        self.ui.lineEditAngle.setText(str(rotationAngle))
        
        # Notify Editor Window
        self.editorWindow.setRotationAngle(rotationAngle)
        
    
    def actionPushButtonRRClickEvt(self):
        # Calculate new Rotation Angle
        rotationAngle = self.editorWindow.getRotationAngle() + 90
        if 360 < rotationAngle:
            rotationAngle = rotationAngle - 360
        else:
            pass
            
        # Update Rotation Angle Slider
        self.ui.horizontalSliderAngle.setValue(rotationAngle)
        
        # Update Rotation Angle Text Box
        self.ui.lineEditAngle.setText(str(rotationAngle))
        
        # Notify Editor Window
        self.editorWindow.setRotationAngle(rotationAngle)
        
    
    def actionPushButtonFlipHClickEvt(self):
        self.editorWindow.flipHorizontal()
        
    
    def actionPushButtonFlipVClickEvt(self):
        self.editorWindow.flipVertical()
        
    
    def closeEvent(self, event):
        LOG("[RotationDialog.closeEvent()] Closing " + self.windowTitle() + " Window")
        # Notify Editor Window
        self.editorWindow.terminateSubDialog(self)
        
        # Terminate sub-attributes/processes
        
        # Call QtWidgets.QMainWindow 's procedure
        if 3 > sys.version_info[0]:
            # Python 2
            super(RotationDialog, self).closeEvent(event)
            
        else:
            # Python 3
            super().closeEvent(event)
            
