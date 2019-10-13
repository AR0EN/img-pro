
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from ui_save_window import Ui_SaveWindow
from images import Image
from cv2 import cv2
import numpy as np


class SaveWindow():

    def __init__(self, imageInfo):
        self.saveWindow = QtWidgets.QMainWindow()
        self.imageInfo = imageInfo
        self.save = Ui_SaveWindow()
        self.save.setupUi(self.saveWindow)
        self.height, self.width, _ = imageInfo.displayData.shape
        self.save.sbWidth.setValue(self.width)
        self.save.sbHeight.setValue(self.height)
        self.save.btnSave.clicked.connect(self.onClickSave)
        self.saveWindow.show()

    def onClickSave(self):
        self.height = self.save.sbHeight.value()
        self.width = self.save.sbWidth.value()
        dim = (self.width, self.height)
        resized = cv2.resize(self.imageInfo.displayData, dim, interpolation = cv2.INTER_AREA)
        resizedRGB = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(None,"Save Image File","","Image Files (*.bmp *.dib *.jpeg *.jpg *.png *.pbm *.pgm *.ppm *.tiff *.tif)", options=options)
        cv2.imwrite(fileName, resizedRGB)


