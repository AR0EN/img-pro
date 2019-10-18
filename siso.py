# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 21:44:28 2019

@author: Le Huy Hoang
"""

import cv2
import numpy as np

from images import Image

# Rotate input image by an angle of degrees (Clockwise)
def rotate(iImg, angle):
    print('Rotation Angle: ' + str(angle))
    if 90 == angle:
        oImg = Image(Image.BY_DATA, cv2.rotate(iImg.data,rotateCode = cv2.ROTATE_90_CLOCKWISE))
        
    elif 180 == angle:
        oImg = Image(Image.BY_DATA, cv2.rotate(iImg.data,rotateCode = cv2.ROTATE_180))
        
    elif 270 == angle:
        oImg = Image(Image.BY_DATA, cv2.rotate(iImg.data,rotateCode = cv2.ROTATE_90_COUNTERCLOCKWISE))
        
    else:
        # Calculate Rotation Matrix
        h, w, _ = iImg.data.shape
        cx = w >> 1
        cy = h >> 1
        rotMatrix = cv2.getRotationMatrix2D((w >> 1, h >> 1), -angle, 1.0)
        cos = np.abs(rotMatrix[0, 0])
        sin = np.abs(rotMatrix[0, 1])
     
        # compute the new bounding dimensions of the image
        nW = int((h * sin) + (w * cos))
        nH = int((h * cos) + (w * sin))
     
        # adjust the rotation matrix to take into account translation
        rotMatrix[0, 2] += (nW / 2) - cx
        rotMatrix[1, 2] += (nH / 2) - cy
        
        # perform the actual rotation and return the image
        oImg = Image(Image.BY_DATA, cv2.warpAffine(iImg.data, rotMatrix, (nW, nH)))
        
    
    return oImg

def flip(iImg, dimension):
    return iImg