import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QMainWindow, QTextEdit)
from UI.edit_widget.FilePage.file_page import FilePage


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Persian Pad")
        self.editor = QTextEdit(self)
        self.file_page = FilePage(editor=self.editor)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.file_page)
        self.main_layout.addWidget(self.editor)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())