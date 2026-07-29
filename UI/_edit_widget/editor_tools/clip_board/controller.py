from PersianPad.UI._edit_widget.editor_tools.clip_board.service import ClipBoardService
from PySide6.QtCore import QObject, Signal
from PersianPad.UI._edit_widget.editor_tools.clip_board.clip_board import ClipBoardWidget


class ClipBoardController(QObject):
    def __init__(self, service: ClipBoardService, clip_board: ClipBoardWidget) -> None:
        super().__init__()
        self.service: ClipBoardService = service
        self.clip_board: ClipBoardWidget = clip_board

        self.clip_board.request_copy.connect(self.copy)
        self.clip_board.request_cut.connect(self.cut)
        self.clip_board.request_paste.connect(self.paste)


    def copy(self) -> None:
        self.service.copy_text()
        return None

    def cut(self) -> None:
        self.service.cut_text()
        return None

    def paste(self) -> None:
        self.service.paste_text()
        return None