from PySide6.QtWidgets import QTextEdit
from PySide6.QtCore import QObject, Signal, Qt
from PySide6.QtGui import QGuiApplication
from PersianPad.UI._edit_widget.editor_tools.clip_board.widget import ClipBoardWidget


class ClipBoardController(QObject):
    def __init__(self, editor: QTextEdit, widget: ClipBoardWidget) -> None:
        super().__init__()
        self.editor: QTextEdit = editor
        self.clip_board: ClipBoardWidget = widget
        self._connect_signals()


    def _connect_signals(self) -> None:
        self.clip_board.request_copy.connect(self.copy)
        self.clip_board.request_cut.connect(self.cut)
        self.clip_board.request_paste.connect(self.paste)
        return None


    def copy(self) -> None:
        self.editor.copy()
        return None


    def cut(self) -> None:
        self.editor.cut()
        return None


    def paste(self) -> None:
        clipboard = QGuiApplication.clipboard()
        text = clipboard.text()
        if not text:
            return None
        cursor = self.editor.textCursor()
        cursor.insertText(text)
        return None


    def selectAll(self) -> None:
        self.editor.selectAll()
        return None


    def undo(self) -> None:
        self.editor.undo()
        return None


    def redo(self) -> None:
        self.editor.redo()
        return None


    def clear(self) -> None:
        self.editor.clear()
        return None