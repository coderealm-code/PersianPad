import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTextEdit,
    QHBoxLayout
)

from PySide6.QtGui import QTextCharFormat


# ==========================
# Model
# ==========================

class TextFormatModel:

    def toggle_bold(self, editor):
        fmt = editor.currentCharFormat()

        if fmt.fontWeight() == 700:
            fmt.setFontWeight(400)
        else:
            fmt.setFontWeight(700)

        editor.mergeCurrentCharFormat(fmt)


    def toggle_italic(self, editor):
        fmt = editor.currentCharFormat()

        fmt.setFontItalic(
            not fmt.fontItalic()
        )

        editor.mergeCurrentCharFormat(fmt)


    def toggle_underline(self, editor):
        fmt = editor.currentCharFormat()

        fmt.setFontUnderline(
            not fmt.fontUnderline()
        )

        editor.mergeCurrentCharFormat(fmt)



# ==========================
# Toolbar
# ==========================

class Toolbar(QWidget):

    def __init__(self):
        super().__init__()

        self.bold = QPushButton("Bold")
        self.italic = QPushButton("Italic")
        self.underline = QPushButton("Underline")

        layout = QHBoxLayout(self)

        layout.addWidget(self.bold)
        layout.addWidget(self.italic)
        layout.addWidget(self.underline)



# ==========================
# Text Edit
# ==========================

class MyTextEdit(QTextEdit):

    def __init__(self):
        super().__init__()

        self.format_model = TextFormatModel()



# ==========================
# Main
# ==========================

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.editor = MyTextEdit()

        self.toolbar = Toolbar()

        layout = QVBoxLayout(self)

        layout.addWidget(self.toolbar)
        layout.addWidget(self.editor)


        # مدل
        self.format_model = TextFormatModel()


        # اتصال سیگنال ها
        self.toolbar.bold.clicked.connect(
            lambda: self.format_model.toggle_bold(
                self.editor
            )
        )

        self.toolbar.italic.clicked.connect(
            lambda: self.format_model.toggle_italic(
                self.editor
            )
        )

        self.toolbar.underline.clicked.connect(
            lambda: self.format_model.toggle_underline(
                self.editor
            )
        )



if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = Window()
    window.resize(700, 400)
    window.show()

    sys.exit(app.exec())