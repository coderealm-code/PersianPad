from app.models.search_part_model import SearchReplaceModel
from PySide6.QtWidgets import QTextEdit
from PySide6.QtGui import QTextCursor
from PySide6.QtCore import Qt


class Justification:
    def __init__(self):
        pass

    def _set_alignment(self, editor: QTextEdit, alignment: Qt.AlignmentFlag) -> None:
        cursor = editor.textCursor()
        block_format = cursor.blockFormat()
        block_format.setAlignment(alignment)

        cursor.mergeBlockFormat(block_format)
        editor.setTextCursor(cursor)
        return None

    def justify_right(self, editor) -> None:
        self._set_alignment(editor, Qt.AlignmentFlag.AlignRight)
        return None

    def justify_left(self, editor) -> None:
        self._set_alignment(editor, Qt.AlignmentFlag.AlignLeft)
        return None

    def justify_center(self, editor) -> None:
        self._set_alignment(editor, Qt.AlignmentFlag.AlignCenter)
        return None

    def justify_all(self, editor) -> None:
        self._set_alignment(editor, Qt.AlignmentFlag.AlignJustify)
        return None