from PySide6.QtGui import QTextDocument, QTextCursor
from PySide6.QtWidgets import QTextEdit
from PersianPad.widgets.dialogs.search_dialog.searchDialog import SearchDialog
from PersianPad.widgets.dialogs.replace_dialog.replace_dialog import ReplaceDialog
from PersianPad.UI._edit_widget.editor_tools.find_replace.find_replace_widget import FindReplaceText
from PersianPad.UI._edit_widget.editor_tools.find_replace.model import FindReplaceModel


class FindReplaceController:
    def __init__(self , find_replace: FindReplaceText, editor: QTextEdit, model: FindReplaceModel) -> None:
        self.editor: QTextEdit = editor
        self.find_replace: FindReplaceText = find_replace
        self.model: FindReplaceModel = model

        self.search_dialog: SearchDialog = SearchDialog()
        self.replace_dialog: ReplaceDialog = ReplaceDialog()

        self.find_replace.request_replace.connect(lambda: self.replace_dialog.show())
        self.find_replace.request_search.connect(lambda: self.search_dialog.show())

        self._connect_signals()

    def _connect_signals(self) -> None:
        self.search_dialog.request_search.connect(self.search)
        self.replace_dialog.request_search.connect(self.search)
        self.replace_dialog.request_replace.connect(self.replace)
        self.replace_dialog.request_replace_all.connect(self.replace_all)


    def _cursor(self) -> QTextCursor:
        cursor = QTextCursor(self.editor.textCursor())
        return cursor


    def _build_find_flags(self) -> QTextDocument.FindFlag:
        flags = QTextDocument.FindFlag()

        if self.model.match_case:
            flags |= QTextDocument.FindFlag.FindCaseSensitively

        if self.model.whole_word:
            flags |= QTextDocument.FindFlag.FindWholeWords
        return flags


    def _is_selection_match(self) -> bool:
        cursor = self._cursor()
        if not cursor.hasSelection():
            return False
        selected_text = cursor.selectedText()
        return selected_text == self.model.search_text


    def _update_model(self, data: dict) -> None:
        self.model.search_text = data['search_text']
        self.model.replace_text = data['replace_text']
        self.model.match_case = data['match_case']
        self.model.whole_word = data['whole_word']
        self.model.regex = data['regex']
        self.model.wrap_search = data['wrap_search']
        return None


    def _move_to_start(self) -> None:
        cursor = self._cursor()
        cursor.movePosition(QTextCursor.MoveOperation.Start)
        self.editor.setTextCursor(cursor)


    def _count_result(self) -> None:
        self.model.result_count += 1
        return None


    def _reset_result(self) -> None:
        self.model.result_count = 0
        return None


    def _count_matches(self) -> None:
        self._reset_result()
        flags = self._build_find_flags()
        cursor = self._cursor()
        current_position = cursor.position()

        self._move_to_start()
        while self.editor.find(self.model.search_text, flags):
            self._count_result()

        cursor.setPosition(current_position)
        self.editor.setTextCursor(cursor)

    def search(self, data: dict) -> bool:
        self._update_model(data)
        if not self.model.search_text:
            return False
        self._count_matches()

        flags = self._build_find_flags()
        result = self.editor.find(self.model.search_text, flags)
        if result:
            return True

        if self.model.wrap_search:
            self._move_to_start()
            return self.editor.find(self.model.search_text, flags)
        return False



    def replace(self, data: dict) -> bool:
        self._update_model(data)
        if self._is_selection_match():
            cursor = self._cursor()
            cursor.insertText(self.model.replace_text)
            return True

        if self.search(data):
            if self._is_selection_match():
                cursor = self._cursor()
                cursor.insertText(self.model.replace_text)
                return True
        return False


    def replace_all(self, data: dict) -> int:
        self._update_model(data)
        if not self.model.search_text:
            return 0
        self._reset_result()
        self._move_to_start()
        flags = self._build_find_flags()
        text = self.model.search_text
        while self.editor.find(text, flags):
            cursor = self._cursor()
            cursor.insertText(self.model.replace_text)
            self._count_result()

        return self.model.result_count

