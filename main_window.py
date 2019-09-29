
from cv2 import cv2

import numpy as np

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap, QImage

from images import Image, Images
from ui_main_window import Ui_MainWindow
from editor_window import EditorWindow

class MainWindow():
    SUPPORT_FORMAT = '(*.bmp *.gif *.jpg *.jpeg *.png *.pbm *.pgm *.ppm *.xbm *.xpm *.svg)'

    def __init__(self):
        self.mainWindow = QtWidgets.QMainWindow()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self.mainWindow)
        
        self.subWindows = []
        
        self.imgList = Images(self.gui.listWidgetImgList)
        
        # Actions
        self.gui.actionImport.triggered.connect(self.actionImportClickEvt)
        
        self.gui.actionEdit.triggered.connect(self.actionEditClickEvt)
        
        self.gui.actionExit.triggered.connect(self.actionExitClickEvt)
        
        self.gui.listWidgetImgList.currentItemChanged.connect(self.actionCurrentItemChangedEvt)
        
        self.mainWindow.show()
    
    # Display an image
    def display(self, _img):
        if _img.valid:
            # Resize
            displayWidth = self.gui.labelCanvas.width()
            displayHeight = self.gui.labelCanvas.height()

            height, width, channel = _img.displayData.shape
            
            hFactor = float(displayHeight)/height
            wFactor = float(displayWidth)/width
            
            if (wFactor > hFactor) and (displayHeight < height):
                height = displayHeight
                width = int(width * hFactor)
                imgDataResized = cv2.resize(_img.displayData,(width,height), interpolation=Image.INTERPOLATION_METHOD)
                
            elif (wFactor < hFactor) and (displayWidth < width):
                height = int(height * wFactor)
                width = displayWidth
                imgDataResized = cv2.resize(_img.displayData,(width,height), interpolation=Image.INTERPOLATION_METHOD)
                
            elif (displayHeight < height):
                height = displayHeight
                width = displayWidth
                imgDataResized = cv2.resize(_img.displayData,(displayWidth, displayHeight), interpolation=Image.INTERPOLATION_METHOD)
            else:
                imgDataResized = _img.displayData
            
            bytesPerLine = 3 * width
            qImg = QImage(imgDataResized, width, height, bytesPerLine, QImage.Format_RGB888)
            
            pixmap = QPixmap(qImg)
            self.gui.labelCanvas.setPixmap(pixmap)
            
        else:
            pass
    
    # Display Current Item when it changed
    def actionCurrentItemChangedEvt(self):
        currentRow = self.gui.listWidgetImgList.currentRow()
        self.display(self.imgList.images[currentRow])
        # Enable Edit Action
        self.gui.actionEdit.setEnabled(True)
        return self.imgList.images[currentRow]

    # Import images
    def actionImportClickEvt(self):
        self.imgList.importImages()
    
    # Edit selected image
    def actionEditClickEvt(self):
        editor = EditorWindow(self.actionCurrentItemChangedEvt())
        self.subWindows.append(editor.editorWindow)
        editor.actionEditorClickEvt()

    # Exit
    def actionExitClickEvt(self):
        self.mainWindow.close()
