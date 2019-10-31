
from PyQt5.QtWidgets import QFileDialog
from ui_save_window import Ui_SaveWindow
from images import Image
from cv2 import cv2
import numpy as np
from wrapper import WindowWrapper
import sys


class SaveWindow(WindowWrapper):

    def __init__(self, _parentWidget, imageInfo):
        # Initialize attributes of QtWidgets.QparentWidget
        if 3 > sys.version_info[0]:
            # Python 2
            super(SaveWindow, self).__init__()
            
        else:
            # Python 3
            super().__init__()

        self.parentWidget = _parentWidget
        self.imageInfo = imageInfo
        self.ui = Ui_SaveWindow()
        self.ui.setupUi(self)
        self.imageResized = None
        self.ui.sbWidth.setValue(self.imageInfo.displayData.shape[1])
        self.ui.sbHeight.setValue(self.imageInfo.displayData.shape[0])
        # Actions
        self.ui.btnSave.clicked.connect(self.onClickSave)
        self.ui.rbWiHe.clicked.connect(self.enableWiHe)
        self.ui.rbPercent.clicked.connect(self.enablePercent)
        self.show()

    def onClickSave(self):
        imageResized = self.resizeImage()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(None,"Save Image File","","Image Files (*.bmp *.dib *.jpeg *.jpg *.png *.pbm *.pgm *.ppm *.tiff *.tif)", options=options)
        cv2.imwrite(fileName, imageResized)

    def enableWiHe(self):
        self.ui.sbPercent.lineEdit().setEnabled(False)
        self.ui.sbWidth.lineEdit().setEnabled(True)
        self.ui.sbHeight.lineEdit().setEnabled(True)

    def enablePercent(self):
        self.ui.sbWidth.lineEdit().setEnabled(False)
        self.ui.sbHeight.lineEdit().setEnabled(False)
        self.ui.sbPercent.lineEdit().setEnabled(True)

    def resizeImage(self):
        if self.ui.rbPercent.isChecked():
            scale_percent = self.ui.sbPercent.value()
            width = int(self.imageInfo.displayData.shape[1] * scale_percent / 100)
            height = int(self.imageInfo.displayData.shape[0] * scale_percent / 100)
        elif self.ui.rbWiHe.isChecked():
            width = self.ui.sbWidth.value()
            height = self.ui.sbHeight.value()
        dim = (width, height)
        resized = cv2.resize(self.imageInfo.displayData, dim, interpolation = cv2.INTER_AREA)
        resizedRGB = Image.convertToRGBU8(resized)
        return resizedRGB


