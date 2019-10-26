# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:55:37 2019

@author: Le Huy Hoang
"""

import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from images import Images
from ui_main_window import Ui_MainWindow
from editor_window import EditorWindow
from wrapper import CommonFunctions

from log import LOG

class MainWindow(QtWidgets.QMainWindow):
    ### Constructor
    def __init__(self):
        # Initialize attributes of QtWidgets.QMainWindow
        if 3 > sys.version_info[0]:
            # Python 2
            super(MainWindow, self).__init__()
            
        else:
            # Python 3
            super().__init__()
            
        # Widget to be deleted when it is closed
        #self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.subWidgets = []
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
        
    
    # Remove a SubWidget
    def removeSubWidget(self, subWidget):
        self.subWidgets.remove(subWidget)
        
    
    ### Event Handlers
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
        self.subWidgets.append(editor)
        
    
    def closeEvent(self, event):
        LOG(self, 'Closing ' + self.windowTitle() + ' Window')
        # Terminate sub-attributes/processes
        for subWidget in self.subWidgets:
            subWidget.unlinkToParentWidget()
            subWidget.close()
            
        self.subWidgets.clear()
        
        # Notify Parent Widget
        
        # Call QtWidgets.QMainWindow 's procedure
        if 3 > sys.version_info[0]:
            # Python 2
            super(EditorWindow, self).closeEvent(event)
            
        else:
            # Python 3
            super().closeEvent(event)
            
        
    
    # Exit
    def actionExitClickEvt(self):
        self.close()
    
