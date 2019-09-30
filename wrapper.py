from cv2 import cv2
from PyQt5.QtGui import QPixmap, QImage
from images import Image


class CommonFunctions():

    def __init__(self, image, display_gui):
        self.image = image
        self.display_gui = display_gui

    # Display an image
    def display(self):
        if self.image.valid:
            # Resize
            displayWidth = self.display_gui.labelCanvas.width()
            displayHeight = self.display_gui.labelCanvas.height()

            height, width, _ = self.image.displayData.shape
            
            hFactor = float(displayHeight)/height
            wFactor = float(displayWidth)/width
            
            if (wFactor > hFactor) and (displayHeight < height):
                height = displayHeight
                width = int(width * hFactor)
                imgDataResized = cv2.resize(self.image.displayData,(width,height), interpolation=Image.INTERPOLATION_METHOD)
                
            elif (wFactor < hFactor) and (displayWidth < width):
                height = int(height * wFactor)
                width = displayWidth
                imgDataResized = cv2.resize(self.image.displayData,(width,height), interpolation=Image.INTERPOLATION_METHOD)
                
            elif (displayHeight < height):
                height = displayHeight
                width = displayWidth
                imgDataResized = cv2.resize(self.image.displayData,(displayWidth, displayHeight), interpolation=Image.INTERPOLATION_METHOD)
            else:
                imgDataResized = self.image.displayData
            
            bytesPerLine = 3 * width
            qImg = QImage(imgDataResized, width, height, bytesPerLine, QImage.Format_RGB888)
            
            pixmap = QPixmap(qImg)
            self.display_gui.labelCanvas.setPixmap(pixmap)
            
        else:
            pass
