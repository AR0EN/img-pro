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
    SUPPORT_FORMAT = '(*.bmp *.gif *.jpg *.jpeg *.png *.pbm *.pgm *.ppm *.xbm *.xpm *.svg)'

    def __init__(self):
        # Initialize attributes of QtWidgets.QMainWindow
        if 3 > sys.version_info[0]:
            # Python 2
            super(MainWindow, self).__init__()
            
        else:
            # Python 3
            super().__init__()
            
        self.gui = Ui_MainWindow()
        #self.gui.setupUi(self.mainWindow)
        self.gui.setupUi(self)
        self.subWindows = []
        self.imgList = Images(self.gui.listWidgetImgList)
        
        # Actions
        self.gui.actionImport.triggered.connect(self.actionImportClickEvt)
        self.gui.actionEdit.triggered.connect(self.actionEditClickEvt)
        self.gui.actionExit.triggered.connect(self.actionExitClickEvt)
        self.gui.listWidgetImgList.currentItemChanged.connect(self.actionCurrentItemChangedEvt)
        self.show()
    
    # Display Current Item when it changed
    def actionCurrentItemChangedEvt(self):
        currentRow = self.gui.listWidgetImgList.currentRow()
        CommonFunctions.display(self.imgList.images[currentRow], self.gui.labelCanvas)
        # Enable Edit Action
        self.gui.actionEdit.setEnabled(True)

    # Import images
    def actionImportClickEvt(self):
        self.imgList.importImages()
    
    # Edit selected image
    def actionEditClickEvt(self):
        editor = EditorWindow(self, self.imgList.images[self.gui.listWidgetImgList.currentRow()])
        self.subWindows.append(editor)
    
    # Terminate an Editor Window
    def terminateEditorWindow(self, editorWindow):
        self.subWindows.remove(editorWindow)
    
    # Exit
    def actionExitClickEvt(self):
        self.close()
