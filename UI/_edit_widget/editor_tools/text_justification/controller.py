from PySide6.QtCore import Qt, QObject
from PySide6.QtGui import QTextCursor, QTextBlockFormat, QTextListFormat
from PySide6.QtWidgets import QTextEdit
from PersianPad.UI._edit_widget.editor_tools.text_justification.text_justification import TextJustify


class TextJustificationController(QObject):
    def __init__(self, editor: QTextEdit, text_justification: TextJustify, parent=None):
        super().__init__(parent)
        self.editor = editor
        self.text_justification = text_justification
        self._connect_signals()

    def _connect_signals(self) -> None:
        self.text_justification.request_right.connect(self.align_right)
        self.text_justification.request_left.connect(self.align_left)
        self.text_justification.request_center.connect(self.align_center)
        self.text_justification.justify.connect(self.justify)
        self.text_justification.request_list.connect(self.disk_list)
        self.text_justification.request_num_lines.connect(self.number_list)
        return None

    def _set_alignment(self, flag: Qt.AlignmentFlag) -> None:
        cursor: QTextCursor = QTextCursor(self.editor.textCursor())
        block_format: QTextBlockFormat = QTextBlockFormat(cursor.blockFormat())
        block_format.setAlignment(flag)

        cursor.mergeBlockFormat(block_format)
        self.editor.setTextCursor(cursor)
        return None

    def _set_list(self, format: QTextListFormat.Style) -> None:
        cursor: QTextCursor = QTextCursor(self.editor.textCursor())
        list_format: QTextListFormat = QTextListFormat()
        list_format.setStyle(format)
        cursor.createList(list_format)
        return None

    def align_right(self) -> None:
        self._set_alignment(Qt.AlignmentFlag.AlignRight)
        return None

    def align_left(self) -> None:
        self._set_alignment(Qt.AlignmentFlag.AlignLeft)
        return None

    def align_center(self) -> None:
        self._set_alignment(Qt.AlignmentFlag.AlignCenter)
        return None

    def justify(self) -> None:
        self._set_alignment(Qt.AlignmentFlag.AlignJustify)
        return None

    def disk_list(self) -> None:
        self._set_list(QTextListFormat.Style.ListDisc)
        return None

    def number_list(self) -> None:
        self._set_list(QTextListFormat.Style.ListDecimal)
        return None
