
from PyQt5 import QtWidgets
from ui_editor_window import Ui_EditorWindow
from wrapper import CommonFunctions


class EditorWindow():

    def __init__(self, imported_image):
        self.editorWindow = QtWidgets.QMainWindow()
        self.imported_image = imported_image
        self.editor = Ui_EditorWindow()
        self.editor.setupUi(self.editorWindow)
        CommonFunctions.display(self.imported_image, self.editor.labelCanvas)
        self.editorWindow.show()
