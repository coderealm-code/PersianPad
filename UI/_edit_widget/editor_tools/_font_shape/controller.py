from PySide6.QtGui import QFont
from PySide6.QtWidgets import QTextEdit
from PySide6.QtCore import QObject
from PersianPad.core.font_loader import FontLoader
from PersianPad.shared.fonts import Fonts
from PersianPad.UI._edit_widget.editor_tools._font_shape.widget import FontShape


class FontShapeController(QObject):
    def __init__(self, editor: QTextEdit, widget: FontShape, parent=None):
        super().__init__(parent)
        self.editor = editor
        self.widget = widget
        self.font_loader = FontLoader()
        self.current_font_family: str = Fonts.DEFAULT_FONT_NAME
        self.current_font_size: int = 12
        self._connect_signals()


    def _connect_signals(self):
        self.widget.request_font_family.connect(self.get_font_family)
        self.widget.request_font_size.connect(self.get_font_size)


    def apply_font(self) -> None:
        font: QFont = QFont(self.current_font_family, self.current_font_size)
        if font is not None:
            self.editor.setFont(font)
        else:
            self.editor.setFont(self.font_loader.load_font(Fonts.DEFAULT_FONT_NAME))
        return None


    def get_font_size(self, size: int) -> None:
        self.current_font_size: int = size
        self.apply_font()
        return None


    def get_font_family(self, family: str) -> None:
        font = self.font_loader.load_font(family).family()
        self.current_font_family: str = font
        self.apply_font()
        return None