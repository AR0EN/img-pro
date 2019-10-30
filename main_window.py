# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:55:37 2019

@author: Le Huy Hoang
"""

import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets

from ui_main_window import Ui_MainWindow

from editor_window import EditorWindow
from wrapper import WindowWrapper
from images import Images
from log import LOG

class MainWindow(WindowWrapper):
    ### Constructor
    def __init__(self):
        # Initialize attributes of QtWidgets.QMainWindow
        if 3 > sys.version_info[0]:
            # Python 2
            super(MainWindow, self).__init__()
            
        else:
            # Python 3
            super().__init__()
            
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Map labelCanvas pointer to the real instance
        self.labelCanvas = self.ui.labelCanvas
        
        self.imgList = Images(self.ui.listWidgetImgList)
        
        # Actions
        self.ui.actionImport.triggered.connect(self.actionImportClickEvt)
        self.ui.actionEdit.triggered.connect(self.actionEditClickEvt)
        self.ui.actionExit.triggered.connect(self.actionExitClickEvt)
        self.ui.listWidgetImgList.currentItemChanged.connect(self.actionCurrentItemChangedEvt)
        self.show()
        
    
    ### Destructor
    def __del__(self):
        LOG(self, 'Finalizing ' + self.windowTitle() + ' Window')
        
    
    ### Event Handlers
    # Display Current Item when it changed
    def actionCurrentItemChangedEvt(self):
        # Get selected row index
        currentRow = self.ui.listWidgetImgList.currentRow()
        
        # Display selected image
        self.display(self.imgList.images[currentRow])
        
        # Enable Edit Action
        self.ui.actionEdit.setEnabled(True)
        
    
    # Import images
    def actionImportClickEvt(self):
        self.imgList.importImages()
        
    
    # Edit selected image
    def actionEditClickEvt(self):
        selectedIndex = self.ui.listWidgetImgList.currentRow()
        selectedImg = self.imgList.images[selectedIndex]
        editor = EditorWindow(self, selectedImg)
        self.subWidgets.append(editor)
        
    
    # Exit
    def actionExitClickEvt(self):
        self.close()
        
    
