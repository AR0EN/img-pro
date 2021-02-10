# -*- coding: utf-8 -*-
"""
Created on Tue Oct 02 22:01:00 2019

@author: Nguyen Tien Nam
"""

from PyQt5 import QtCore
from PyQt5.QtWidgets import QFileDialog
from ui_save_dialog import Ui_SaveDialog
from images import Image
import cv2
import numpy as np
from wrapper import DialogWrapper
import sys

from log import LOG

class SaveDialog(DialogWrapper):

    def __init__(self, _parentWidget, _editingImg):
        # Initialize attributes of QtWidgets.QparentWidget
        if 3 > sys.version_info[0]:
            # Python 2
            super(SaveWindow, self).__init__()
            
        else:
            # Python 3
            super().__init__()

        self.parentWidget = _parentWidget
        self._editingImg = _editingImg
        self.ui = Ui_SaveDialog()
        self.ui.setupUi(self)
        
        # Widget to be deleted when it is closed
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        
        self.imageResized = None
        h, w, _ = self._editingImg.data.shape
        self.ui.sbWidth.setValue(w)
        self.ui.sbHeight.setValue(h)
        
        # Actions
        self.ui.buttonBox.accepted.connect(self.onClickOK)
        self.ui.buttonBox.rejected.connect(self.onClickCancel)
        self.ui.rbWiHe.clicked.connect(self.enableWiHe)
        self.ui.rbPercent.clicked.connect(self.enablePercent)
        self.ui.sbWidth.valueChanged.connect(self.sbWidthValueChanged)
        self.ui.sbHeight.valueChanged.connect(self.sbHeightValueChanged)
        self.show()

    def onClickOK(self):
        imageResized = self.resizeImage()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(None,"Save Image File","","Image Files (*.bmp *.dib *.jpeg *.jpg *.png *.pbm *.pgm *.ppm *.tiff *.tif)", options=options)
        LOG(self, "File path: " + fileName)
        cv2.imwrite(fileName, imageResized)
        self.close()
    
    def onClickCancel(self):
        self.close()
        pass
    
    def enableWiHe(self):
        self.ui.rbPercent.setChecked(False)
        self.ui.sbPercent.setEnabled(False)
        self.ui.sbWidth.setEnabled(True)
        self.ui.sbHeight.setEnabled(True)

    def enablePercent(self):
        self.ui.rbWiHe.setChecked(False)
        self.ui.sbWidth.setEnabled(False)
        self.ui.sbHeight.setEnabled(False)
        self.ui.sbPercent.setEnabled(True)
    
    def sbWidthValueChanged(self):
        h, w, _ = self._editingImg.data.shape
        newWidth = self.ui.sbWidth.value()
        newHeight = int((newWidth * h) / w)
        self.ui.sbHeight.setValue(newHeight)
    
    def sbHeightValueChanged(self):
        h, w, _ = self._editingImg.data.shape
        newHeight = self.ui.sbHeight.value()
        newWidth = int((newHeight * w) / h)
        self.ui.sbWidth.setValue(newWidth)
    
    def resizeImage(self):
        if self.ui.rbPercent.isChecked():
            scale_percent = self.ui.sbPercent.value()
            h, w, _ = self._editingImg.data.shape
            newWidth = int((w * scale_percent) / 100)
            newHeight = int((h * scale_percent) / 100)
        elif self.ui.rbWiHe.isChecked():
            newWidth = self.ui.sbWidth.value()
            newHeight = self.ui.sbHeight.value()
        dim = (newWidth, newHeight)
        resized = cv2.resize(self._editingImg.data, dim, interpolation = cv2.INTER_AREA)
        return resized


