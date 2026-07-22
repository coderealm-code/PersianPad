import sys
from PersianPad.core.path_handler import PathHandler
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap, QFont


class VerticalButton(QPushButton):
    def __init__(self, text: str, icon: str, parent=None) -> None:
        super().__init__(parent)
        self.setMinimumSize(50, 75)

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.text_label = QLabel(text)
        self.text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_label.setStyleSheet("QLabel { color: black;"
                                      "background-color: transparent;"
                                      "font-size: 10px;"
                                      "font-family: nazanin;"
                                      "font-weight: bold;}")
        self.text_label.setFixedSize(75, 25)

        path = PathHandler.icon(icon)
        pixmap = QPixmap(path)
        scaled_pixmap = pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.pic_label = QLabel()
        self.pic_label.setPixmap(scaled_pixmap)
        self.pic_label.setFixedSize(72, 72)
        self.pic_label.setAlignment(Qt.AlignmentFlag.AlignCenter)



        self.layout.addWidget(self.pic_label)
        self.layout.addSpacing(15)
        self.layout.addWidget(self.text_label)


        self.setLayout(self.layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VerticalButton(icon="document.png", text="document")
    window.show()
    window.show()
    sys.exit(app.exec_())