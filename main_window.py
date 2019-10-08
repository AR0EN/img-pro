# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:55:37 2019

@author: Le Huy Hoang
"""

import sys

from PyQt5 import QtWidgets
from images import Images
from ui_main_window import Ui_MainWindow
from editor_window import EditorWindow
from wrapper import CommonFunctions

class MainWindow(QtWidgets.QMainWindow):
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
        self.subWindows = []
        self.imgList = Images(self.ui.listWidgetImgList)
        
        # Actions
        self.ui.actionImport.triggered.connect(self.actionImportClickEvt)
        self.ui.actionEdit.triggered.connect(self.actionEditClickEvt)
        self.ui.actionExit.triggered.connect(self.actionExitClickEvt)
        self.ui.listWidgetImgList.currentItemChanged.connect(self.actionCurrentItemChangedEvt)
        self.show()
    
    # Display Current Item when it changed
    def actionCurrentItemChangedEvt(self):
        currentRow = self.ui.listWidgetImgList.currentRow()
        CommonFunctions.display(self.imgList.images[currentRow], self.ui.labelCanvas)
        # Enable Edit Action
        self.ui.actionEdit.setEnabled(True)

    # Import images
    def actionImportClickEvt(self):
        self.imgList.importImages()
    
    # Edit selected image
    def actionEditClickEvt(self):
        editor = EditorWindow(self, self.imgList.images[self.ui.listWidgetImgList.currentRow()])
        self.subWindows.append(editor)
    
    # Terminate an Editor Window
    def terminateEditorWindow(self, editorWindow):
        self.subWindows.remove(editorWindow)
    
    # Exit
    def actionExitClickEvt(self):
        self.close()
