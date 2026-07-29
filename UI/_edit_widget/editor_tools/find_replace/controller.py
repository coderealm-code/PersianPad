from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTextEdit
from PersianPad.widgets.dialogs.search_dialog.searchDialog import SearchDialog
from PersianPad.widgets.dialogs.replace_dialog.replace_dialog import ReplaceDialog
from PersianPad.UI._edit_widget.editor_tools.find_replace.find_replace_widget import FindReplaceText


class FindReplaceController:
    def __init__(self , find_replace: FindReplaceText) -> None:
        # self.editor = editor
        self.find_replace = find_replace

        self.find_replace.request_replace.connect(self.show_replace_dialog)
        self.find_replace.request_search.connect(self.show_search_dialog)


    def show_search_dialog(self) -> None:
        print("from search_dialog")
        search_dialog: QDialog = SearchDialog()
        search_dialog.exec()
        return None


    def show_replace_dialog(self) -> None:
        print("from replace_dialog")
        replace_dialog: QDialog = ReplaceDialog()
        replace_dialog.exec()
        return None

