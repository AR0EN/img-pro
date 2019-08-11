from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QFileDialog, QLabel
from PyQt5.QtGui import QIcon, QPixmap

from main_window import *

import sys

class Ui():
    SUPPORT_FORMAT = '(*.bmp *.gif *.jpg *.jpeg *.png *.pbm *.pgm *.ppm *.xbm *.xpm *.svg)'

    def __init__(self):
        self.mainWindow = QtWidgets.QMainWindow()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self.mainWindow)
        # Actions
        self.gui.actionOpen.triggered.connect(self.actionOpenClickEvt)
        self.gui.actionTBOpen.triggered.connect(self.actionOpenClickEvt)
        
        self.gui.actionExport.triggered.connect(self.actionExportClickEvt)
        self.gui.actionTBExport.triggered.connect(self.actionExportClickEvt)
        
        self.gui.actionSave.triggered.connect(self.actionSaveClickEvt)
        self.gui.actionTBSave.triggered.connect(self.actionSaveClickEvt)
        self.gui.actionExit.triggered.connect(self.actionExitClickEvt)
        self.mainWindow.show()

    # Open an image
    def actionOpenClickEvt(self):
        fileBrowser = QFileDialog()
        fileBrowser.setFileMode(QFileDialog.ExistingFile)
        fileBrowser.setNameFilter('Images ' + Ui.SUPPORT_FORMAT)
        if fileBrowser.exec_():
            displayWidth = self.gui.labelCanvas.width()
            displayHeight = self.gui.labelCanvas.height()
            fileNames = fileBrowser.selectedFiles()
            pixmap = QPixmap(fileNames[0])
            if (displayWidth < pixmap.width()) or (displayHeight < pixmap.height()):
                pixmap = pixmap.scaled(displayWidth, displayHeight, QtCore.Qt.KeepAspectRatio)
            
            self.gui.labelCanvas.setPixmap(pixmap)

    # Export changes to a new image
    def actionExportClickEvt(self):
        pass

    # Save changes
    def actionSaveClickEvt(self):
        pass

    # Exit
    def actionExitClickEvt(self):
        self.mainWindow.close()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())
