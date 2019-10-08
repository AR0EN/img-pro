
from PyQt5 import QtWidgets
from ui_save_window import Ui_SaveWindow
from cv2 import cv2


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
        self.height = self.save.sbHeight.Value()
        self.width = self.save.sbWidth.Value()
        dim = (self.width, self.height)
        resized = cv2.resize(self.imageInfo.displayData, dim, interpolation = cv2.INTER_AREA)
        newName = ("_" + self.height + "_" + self.width + ".").join(self.imageInfo.name.split("."))
        cv2.imwrite(newName, resized)

