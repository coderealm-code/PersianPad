from PySide6.QtGui import QTextCharFormat
from PySide6.QtGui import QTextCursor,QFont, QColor
from PySide6.QtWidgets import QTextEdit, QColorDialog
from PySide6.QtCore import QObject, Qt
from PersianPad.UI._edit_widget.editor_tools.font_setting.widget import FontSetting


class FontSettingController(QObject):
    def __init__(self, editor: QTextEdit, widget: FontSetting, parent=None):
        super().__init__(parent)
        self.editor: QTextEdit = editor
        self.widget: FontSetting = widget
        self._connect_signals()


    def _connect_signals(self):
        self.widget.request_bold.connect(self.font_bold)
        self.widget.request_italic.connect(self.font_italic)
        self.widget.request_underLine.connect(self.font_underline)
        self.widget.request_color.connect(self.color_dialog)
        self.widget.request_highlight.connect(self.highlight_font)


    def _setCharFormat(self, fmt: QTextCharFormat) -> None:
        cursor: QTextCursor = self.editor.textCursor()
        if cursor.hasSelection():
            cursor.mergeCharFormat(fmt)
        else:
            self.editor.mergeCurrentCharFormat(fmt)
        return None


    def color_dialog(self) -> None:
        color: QColor = QColorDialog.getColor()
        if color.isValid():
            self.widget.text_color.setColor(color)
            self.font_color(color)
        return None


    def font_color(self, color: QColor) -> None:
        fmt: QTextCharFormat = self.editor.currentCharFormat()
        fmt.setForeground(color)
        self._setCharFormat(fmt)
        return None


    def highlight_font(self):
        cursor = self.editor.textCursor()
        fmt: QTextCharFormat = QTextCharFormat(cursor.charFormat())
        if fmt.background().color() == Qt.GlobalColor.yellow:
            fmt.setBackground(Qt.GlobalColor.transparent)
        else:
            fmt.setBackground(Qt.GlobalColor.yellow)
        self._setCharFormat(fmt)
        return None


    def font_bold(self) -> None:
        cursor = self.editor.textCursor()
        fmt: QTextCharFormat = QTextCharFormat(cursor.charFormat())
        if fmt.fontWeight() == QFont.Weight.Bold:
            fmt.setFontWeight(QFont.Weight.Normal)
        else:
            fmt.setFontWeight(QFont.Weight.Bold)
        self._setCharFormat(fmt)
        return None


    def font_italic(self) -> None:
        cursor = self.editor.textCursor()
        fmt: QTextCharFormat = QTextCharFormat(cursor.charFormat())
        fmt.setFontItalic(not self.editor.fontItalic())
        self._setCharFormat(fmt)
        return None


    def font_underline(self) -> None:
        cursor = self.editor.textCursor()
        fmt: QTextCharFormat = QTextCharFormat(cursor.charFormat())
        fmt.setFontUnderline(not self.editor.fontUnderline())
        self._setCharFormat(fmt)
        return None
