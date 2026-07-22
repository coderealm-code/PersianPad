from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt


class FileManager(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setLayoutDirection(Qt.RightToLeft)
        self.setAutoFillBackground(True)



