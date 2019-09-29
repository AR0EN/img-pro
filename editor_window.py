
from cv2 import cv2

import numpy as np

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap, QImage

from images import Image, Images
from ui_editor_window import Ui_EditorWindow

class EditorWindow():
    SUPPORT_FORMAT = '(*.bmp *.gif *.jpg *.jpeg *.png *.pbm *.pgm *.ppm *.xbm *.xpm *.svg)'

    def __init__(self, imported_image):
        self.editorWindow = QtWidgets.QMainWindow()
        self.imported_image = imported_image
        self.editor = Ui_EditorWindow()
        self.editor.setupUi(self.editorWindow)
        self.gui = Ui_EditorWindow()
        self.gui.setupUi(self.editorWindow)

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

    # Edit selected image
    def actionEditorClickEvt(self):
        self.display(self.imported_image)
        self.editorWindow.show()
