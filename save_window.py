
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from ui_save_window import Ui_SaveWindow
from images import Image
from cv2 import cv2
import numpy as np


class SaveWindow():

    def __init__(self, imageInfo):
        self.imageResized = None
        self.saveWindow = QtWidgets.QMainWindow()
        self.imageInfo = imageInfo
        self.save = Ui_SaveWindow()
        self.save.setupUi(self.saveWindow)
        self.save.sbWidth.setValue(self.imageInfo.displayData.shape[1])
        self.save.sbHeight.setValue(self.imageInfo.displayData.shape[0])
        self.save.btnSave.clicked.connect(self.onClickSave)
        self.save.rbWiHe.clicked.connect(self.enableWiHe)
        self.save.rbPercent.clicked.connect(self.enablePercent)
        self.saveWindow.show()

    def onClickSave(self):
        imageResized = self.resizeImage()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(None,"Save Image File","","Image Files (*.bmp *.dib *.jpeg *.jpg *.png *.pbm *.pgm *.ppm *.tiff *.tif)", options=options)
        cv2.imwrite(fileName, imageResized)

    def enableWiHe(self):
        self.save.sbPercent.lineEdit().setEnabled(False)
        self.save.sbWidth.lineEdit().setEnabled(True)
        self.save.sbHeight.lineEdit().setEnabled(True)

    def enablePercent(self):
        self.save.sbWidth.lineEdit().setEnabled(False)
        self.save.sbHeight.lineEdit().setEnabled(False)
        self.save.sbPercent.lineEdit().setEnabled(True)

    def resizeImage(self):
        if self.save.rbPercent.isChecked():
            scale_percent = self.save.sbPercent.value()
            width = int(self.imageInfo.displayData.shape[1] * scale_percent / 100)
            height = int(self.imageInfo.displayData.shape[0] * scale_percent / 100)
        elif self.save.rbWiHe.isChecked():
            width = self.save.sbWidth.value()
            height = self.save.sbHeight.value()
        dim = (width, height)
        resized = cv2.resize(self.imageInfo.displayData, dim, interpolation = cv2.INTER_AREA)
        resizedRGB = Image.convertToRGBU8(resized)
        return resizedRGB


