
from PyQt5 import QtWidgets
from ui_editor_window import Ui_EditorWindow
from save_window import SaveWindow
from wrapper import CommonFunctions
from cv2 import cv2


class EditorWindow():

    def __init__(self, imported_image):
        self.editorWindow = QtWidgets.QMainWindow()
        self.imported_image = imported_image
        self.editor = Ui_EditorWindow()
        self.editor.setupUi(self.editorWindow)
        self.subWindows = None

        self.editor.actionSave.triggered.connect(self.actionSaveClickEvt)

        CommonFunctions.display(self.imported_image, self.editor.labelCanvas)
        self.editorWindow.show()

    def actionSaveClickEvt(self):
        save = SaveWindow()
        self.subWindows = save.saveWindow