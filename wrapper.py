from cv2 import cv2
from PyQt5.QtGui import QPixmap, QImage
from images import Image


class CommonFunctions():

    @staticmethod
    # Display an image
    def display(image, gui_label_canvas):
        if image.valid:
            # Resize
            displayWidth = gui_label_canvas.width()
            displayHeight = gui_label_canvas.height()
            height, width, _ = image.displayData.shape
            hFactor = float(displayHeight)/height
            wFactor = float(displayWidth)/width

            if (wFactor > hFactor) and (displayHeight < height):
                height = displayHeight
                width = int(width * hFactor)
                imgDataResized = cv2.resize(image.displayData,(width,height), interpolation=Image.INTERPOLATION_METHOD)

            elif (wFactor < hFactor) and (displayWidth < width):
                height = int(height * wFactor)
                width = displayWidth
                imgDataResized = cv2.resize(image.displayData,(width,height), interpolation=Image.INTERPOLATION_METHOD)

            elif (displayHeight < height):
                height = displayHeight
                width = displayWidth
                imgDataResized = cv2.resize(image.displayData,(displayWidth, displayHeight), interpolation=Image.INTERPOLATION_METHOD)
            else:
                imgDataResized = image.displayData

            bytesPerLine = 3 * width
            qImg = QImage(imgDataResized, width, height, bytesPerLine, QImage.Format_RGB888)
            
            pixmap = QPixmap(qImg)
            gui_label_canvas.setPixmap(pixmap)

        else:
            pass
