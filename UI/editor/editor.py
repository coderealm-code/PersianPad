import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFrame, QTextEdit
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PersianPad.shared.metrics import EditorMetrics
from PersianPad.core.font_loader import FontLoader
from PersianPad.shared.fonts import Fonts


class Editor(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        # حالت اولیه اشاره گر از سمت راست شروع میشود
        option = self.document().defaultTextOption()
        option.setTextDirection(Qt.LayoutDirection.RightToLeft)
        self.document().setDefaultTextOption(option)
        self.setFixedSize(EditorMetrics.A4)

        self.fon_loader = FontLoader()

        self.default_font: QFont = self.fon_loader.load_font(font_name=Fonts.DEFAULT_FONT_NAME, size=12)
        self.font = QFont()


    def get_font_family(self, font_name: str) -> str:
        fonts = Fonts()
        for item in fonts:
            if font_name != item:
                raise ValueError("Font family not supported")
        font = self.fon_loader.load_font(font_name=font_name).family()
        return font


    def _set_font(self, font: QFont | None = None) -> None:
        if font is not None:
            self.setFont(font)
        else:
            self.setFont(self.default_font)
        return None





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Editor()
    window.show()
    sys.exit(app.exec())