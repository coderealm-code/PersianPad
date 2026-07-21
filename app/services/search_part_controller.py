from app.models.search_part_model import SearchReplaceModel
from PySide6.QtWidgets import QTextEdit
from PySide6.QtGui import QTextCursor


class SearchReplaceController:
    def __init__(self, model: SearchReplaceModel, editor: QTextEdit):
        self._model = model
        self._editor = editor


    def search(self) -> bool:
        """داخل تکست ادیت متن را جستجو میکند و هایلایت میکند و اگر به آخر متن رسید و چیزی پیدا نکرد دوباره 
        جستجو میکند! """
        text = self._model.get_search_text
        if not text:
            return False
        
        if self._editor.find(text):
            return True
        
        cursor = self._editor.textCursor() # کرسر متن را میگیرد 
        cursor.movePosition(QTextCursor.Start) # به اول برمیگرداند

        self._editor.setTextCursor(cursor) # در نمایشگر نمایش میدهد
        
        return self._editor.find(text)


    def replace(self) -> bool:
        """Replace
            |
            ▼
            آیا متن انتخاب شده است؟
            |
            ├── بله → آیا همان متن جستجو است؟
            |             |
            |             ├── بله → جایگزین کن
            |             |
            |             └── نه → جستجو کن
            |
            └── نه → جستجو کن"""
        search_text = self._model.get_search_text
        replace_text = self._model.get_replace_text

        if not search_text:
            return False
        if not replace_text:
            return False
        
        cursor = self._editor.textCursor()
        if cursor.hasSelection():
            selected_text = cursor.selectedText()

            if selected_text == search_text:
                cursor.insertText(replace_text)
                return self.search()
            
        return self.search()


    def replace_all(self) -> int:
        """برو ابتدای متن
            │
            ▼
        جستجو کن
            │
            ├── پیدا شد؟
            │      │
            │      ├── بله
            │      │      │
            │      │      ▼
            │      │  جایگزین کن
            │      │      │
            │      │      ▼
            │      │ count += 1
            │      │
            │      └───────↺
            │
            └── خیر
                    │
                    ▼
                count را برگردان"""
        search_text = self._model.get_search_text
        replace_text = self._model.get_replace_text

        if not search_text:
            return 0
        
        if not replace_text:
            return 0
        
        cursor = self._editor.textCursor()
        cursor.movePosition(QTextCursor.Start)
        self._editor.setTextCursor(cursor)

        count = 0
        while self._editor.find(search_text):
            cursor = self._editor.textCursor()
            cursor.insertText(replace_text)
            count += 1

        return count


    def _move_to_start(self) -> None:
        cursor = self._editor.textCursor()
        cursor.movePosition(QTextCursor.Start)
        self._editor.setTextCursor(cursor)
        return None