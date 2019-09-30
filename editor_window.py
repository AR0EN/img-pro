
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

    # Display an image
    def display(self):
        display_editor = CommonFunctions(self.imported_image, self.gui)
        display_editor.display()

    # Edit selected image
    def actionEditorClickEvt(self):
        self.display()
        self.editorWindow.show()
