from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QTextEdit


class ClipBoardService(QObject):
    request_copy_text: Signal = Signal(str)
    request_cut_text: Signal = Signal(str)
    request_paste_text: Signal = Signal(str)

    def __init__(self, editor: QTextEdit) -> None:
        super().__init__()
        self.editor: QTextEdit = editor


    def copy_text(self) -> None:
        """copy just selected text from text editor"""
        self.editor.copy()
        self.request_copy_text.emit()


    def cut_text(self):
        """cut text from text editor"""
        self.editor.cut()
        self.request_cut_text.emit()


    def paste_text(self):
        """paste text to text editor"""
        self.editor.paste()
        self.request_paste_text.emit()