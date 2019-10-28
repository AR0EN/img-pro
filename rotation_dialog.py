# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 20:50:00 2019

@author: Le Huy Hoang
"""

import sys
import os

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from ui_rotation_dialog import Ui_RotationDialog

from wrapper import DialogWrapper
from log import LOG

class RotationDialog(DialogWrapper):
    ### Constants
    BY_DATA = 1
    
    ### Constructor
    def __init__(self, _parentWidget):
        # Initialize attributes of QtWidgets.QDialog
        if 3 > sys.version_info[0]:
            # Python 2
            super(RotationDialog, self).__init__()
            
        else:
            # Python 3
            super().__init__()
        
        # Widget to be deleted when it is closed
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        
        self.parentWidget = _parentWidget
        
        # Initialize UI components
        self.ui = Ui_RotationDialog()
        self.ui.setupUi(self)
        
        # Get current Rotation Angle of Editing Image
        rotationAngle = self.parentWidget.getRotationAngle()
        
        # Update Rotation Angle Slider
        self.ui.horizontalSliderAngle.setValue(rotationAngle)
        
        # Update Rotation Angle Text Box
        self.ui.lineEditAngle.setText(str(rotationAngle))
        
        # Actions
        self.ui.horizontalSliderAngle.sliderReleased.connect(self.actionHorizontalSliderAngleSliderReleasedEvt)
        self.ui.pushButtonRL.clicked.connect(self.actionPushButtonRLClickEvt)
        self.ui.pushButtonRR.clicked.connect(self.actionPushButtonRRClickEvt)
        self.ui.pushButtonFlipH.clicked.connect(self.actionPushButtonFlipHClickEvt)
        self.ui.pushButtonFlipV.clicked.connect(self.actionPushButtonFlipVClickEvt)
        
        self.show()
        
    
    ### Destructor
    def __del__(self):
        LOG(self, 'Finalizing ' + self.windowTitle() + ' Window')
        
    
    ### Event Handlers
    def actionHorizontalSliderAngleSliderReleasedEvt(self):
        # Get new Rotation Angle
        rotationAngle = self.ui.horizontalSliderAngle.value()
        
        # Update Rotation Angle Text Box
        self.ui.lineEditAngle.setText(str(rotationAngle))
        
        # Notify Editor Window
        self.parentWidget.setRotationAngle(rotationAngle)
        
    
    def actionPushButtonRLClickEvt(self):
        # Calculate new Rotation Angle
        rotationAngle = self.parentWidget.getRotationAngle() - 90
        if 0 > rotationAngle:
            rotationAngle = rotationAngle + 360
        else:
            pass
            
        # Update Rotation Angle Slider
        self.ui.horizontalSliderAngle.setValue(rotationAngle)
        
        # Update Rotation Angle Text Box
        self.ui.lineEditAngle.setText(str(rotationAngle))
        
        # Notify Editor Window
        self.parentWidget.setRotationAngle(rotationAngle)
        
    
    def actionPushButtonRRClickEvt(self):
        # Calculate new Rotation Angle
        rotationAngle = self.parentWidget.getRotationAngle() + 90
        if 360 < rotationAngle:
            rotationAngle = rotationAngle - 360
        else:
            pass
            
        # Update Rotation Angle Slider
        self.ui.horizontalSliderAngle.setValue(rotationAngle)
        
        # Update Rotation Angle Text Box
        self.ui.lineEditAngle.setText(str(rotationAngle))
        
        # Notify Editor Window
        self.parentWidget.setRotationAngle(rotationAngle)
        
    
    def actionPushButtonFlipHClickEvt(self):
        self.parentWidget.flipHorizontal()
        
    
    def actionPushButtonFlipVClickEvt(self):
        self.parentWidget.flipVertical()
        
    
