# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 21:34:48 2019

@author: Admin
"""

class State():
    def __init__(self):
        # Rotated Angle (degree)
        self.rotationAngle = 0.0
        
        # Crop Rectangle Position
        self.cropRectX = 0
        self.cropRectY = 0
        
        # Crop Rectangle Dimensions
        self.cropRectW = 0
        self.cropRectH = 0
    
    def set(self, _rotationAngle, _cropRectX, _cropRectY, _cropRectW, _cropRectH):
        # Rotated Angle (degree)
        self.rotationAngle = _rotationAngle
        
        # Crop Rectangle Position
        self.cropRectX = _cropRectX
        self.cropRectY = _cropRectY
        
        # Crop Rectangle Dimensions
        self.cropRectW = _cropRectW
        self.cropRectH = _cropRectH
    
