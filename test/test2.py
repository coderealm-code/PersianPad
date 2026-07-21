
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTextEdit,
    QHBoxLayout
)

from PySide6.QtCore import Qt


class dddd(QWidget):
    def __init__(self):
        super().__init__()

        self.editor = QTextEdit()
        # self.editor.setLayoutDirection(Qt.RightToLeft)

        self.layouts = QVBoxLayout()
        self.layouts.addWidget(self.editor)
        self.setLayout(self.layouts)
        


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = dddd()
    window.resize(700, 400)
    window.show()

    sys.exit(app.exec())