# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 21:34:48 2019

@author: Admin
"""

class State():
    def __init__(self):
        # Flip State
        self.flippedV = False
        self.flippedH = False

        # Rotated Angle (degree)
        self.rotationAngle = 0.0
        
        # Crop Rectangle Position
        self.cropRectX = 0
        self.cropRectY = 0
        
        # Crop Rectangle Dimensions
        self.cropRectW = 0
        self.cropRectH = 0
    
    def set(self, _flippedV, _flippedH, _rotationAngle, _cropRectX, _cropRectY, _cropRectW, _cropRectH):
        # Flip State
        if True == _flippedV:
            self.flippedV = True
            
        else:
            self.flippedV = False
        
        if True == _flippedH:
            self.flippedH = True
            
        else:
            self.flippedH = False
        
        # Rotated Angle (degree)
        self.rotationAngle = _rotationAngle
        
        # Crop Rectangle Position
        self.cropRectX = _cropRectX
        self.cropRectY = _cropRectY
        
        # Crop Rectangle Dimensions
        self.cropRectW = _cropRectW
        self.cropRectH = _cropRectH
    
