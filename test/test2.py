import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QMainWindow, QTextEdit)
from PersianPad.UI._edit_widget.FilePage.FileManager.file_manager import FileManager
from PersianPad.UI._edit_widget.FilePage.FileManager.controller import FileController


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Persian Pad")
        self.editor = QTextEdit(self)
        self.widget = FileManager(parent=self)
        self.controller = FileController(editor=self.editor, widget=self.widget)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.widget)
        self.main_layout.addWidget(self.editor)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())