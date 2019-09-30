
from PyQt5 import QtWidgets
from ui_editor_window import Ui_EditorWindow
from wrapper import CommonFunctions


class EditorWindow():

    def __init__(self, imported_image):
        self.editorWindow = QtWidgets.QMainWindow()
        self.imported_image = imported_image
        self.editor = Ui_EditorWindow()
        self.editor.setupUi(self.editorWindow)
        self.gui = Ui_EditorWindow()
        self.gui.setupUi(self.editorWindow)
        self.display_editor = CommonFunctions(self.imported_image, self.gui)

    # Edit selected image
    def actionEditorClickEvt(self):
        self.display_editor.display()
        self.editorWindow.show()
