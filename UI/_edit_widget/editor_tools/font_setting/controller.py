from PySide6.QtGui import QTextCharFormat
from PySide6.QtGui import QTextCursor, QTextBlockFormat, QFont, QColor
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

    def color_dialog(self) -> None:
        color: QColor = QColorDialog.getColor()
        if color.isValid():
            self.widget.text_color.setColor(color)
            self.font_color(color)
        return None

    def font_color(self, color: QColor) -> None:
        fmt = QTextCharFormat(self.editor.currentCharFormat())
        fmt.setForeground(color)
        cursor = self.editor.textCursor()
        if cursor.hasSelection():
            cursor.mergeCharFormat(fmt)
        else:
            self.editor.setCurrentCharFormat(fmt)
        return None

    def highlight_font(self) -> None:
        print("highlight_font")
        cursor = self.editor.textCursor()
        if not cursor.hasSelection():
            return
        fmt = QTextCharFormat()  # فرمت جدید، مستقل از فرمت جاری
        fmt.setBackground(Qt.GlobalColor.yellow)  # فقط هایلایت
        cursor.mergeCharFormat(fmt)  # فقط روی متن انتخاب‌شده اعمال می‌شود


    def font_bold(self) -> None:
        print("font_bold")
        fmt: QTextCharFormat = QTextCharFormat(self.editor.currentCharFormat())
        if fmt.fontWeight() == QFont.Weight.Bold:
            fmt.setFontWeight(QFont.Weight.Normal)
        else:
            fmt.setFontWeight(QFont.Weight.Bold)
        self.editor.setCurrentCharFormat(fmt)
        return None


    def font_italic(self) -> None:
        print("font_italic")
        fmt: QTextCharFormat = QTextCharFormat(self.editor.currentCharFormat())
        if fmt.fontItalic():
            fmt.setFontItalic(False)
        else:
            fmt.setFontItalic(True)
        self.editor.setCurrentCharFormat(fmt)
        return None


    def font_underline(self) -> None:
        print("font_underline")
        fmt: QTextCharFormat = QTextCharFormat(self.editor.currentCharFormat())
        if fmt.fontUnderline():
            fmt.setFontUnderline(False)
        else:
            fmt.setFontUnderline(True)
        self.editor.setCurrentCharFormat(fmt)
        return None
