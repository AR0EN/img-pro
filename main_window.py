
from PyQt5 import QtWidgets
from images import Images
from ui_main_window import Ui_MainWindow
from editor_window import EditorWindow
from wrapper import CommonFunctions

class MainWindow():
    SUPPORT_FORMAT = '(*.bmp *.gif *.jpg *.jpeg *.png *.pbm *.pgm *.ppm *.xbm *.xpm *.svg)'

    def __init__(self):
        self.mainWindow = QtWidgets.QMainWindow()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self.mainWindow)
        
        self.subWindows = []
        
        self.imgList = Images(self.gui.listWidgetImgList)
        
        # Actions
        self.gui.actionImport.triggered.connect(self.actionImportClickEvt)
        
        self.gui.actionEdit.triggered.connect(self.actionEditClickEvt)
        
        self.gui.actionExit.triggered.connect(self.actionExitClickEvt)
        
        self.gui.listWidgetImgList.currentItemChanged.connect(self.actionCurrentItemChangedEvt)
        
        self.mainWindow.show()
    
    # Display Current Item when it changed
    def actionCurrentItemChangedEvt(self):
        currentRow = self.gui.listWidgetImgList.currentRow()
        display_main = CommonFunctions(self.imgList.images[currentRow], self.gui)
        display_main.display()
        # Enable Edit Action
        self.gui.actionEdit.setEnabled(True)
        return self.imgList.images[currentRow]

    # Import images
    def actionImportClickEvt(self):
        self.imgList.importImages()
    
    # Edit selected image
    def actionEditClickEvt(self):
        editor = EditorWindow(self.actionCurrentItemChangedEvt())
        self.subWindows.append(editor.editorWindow)
        editor.actionEditorClickEvt()

    # Exit
    def actionExitClickEvt(self):
        self.mainWindow.close()