from PySide6.QtWidgets import QWidget, QTextEdit, QHBoxLayout, QSizePolicy
from PySide6.QtCore import Qt
from PySide6.QtGui import QTextCursor, QFont
import sys
from app.sizes.metrics import TextPlaceMetrics
from app.models.font_format import TextFormatModel, FontFormatModel
from app.services.justification_controller import Justification
from app.widgets.pages.show_widget import ShowWidget



class TextEdit(QTextEdit):
    def __init__(self, edit_widget) -> None:
        super().__init__()
        option = self.document().defaultTextOption()
        option.setTextDirection(Qt.RightToLeft)
        self.document().setDefaultTextOption(option)

        self.edit_widget = edit_widget
        self.font_model = TextFormatModel()
        self.font_format_model = FontFormatModel()
        self.justification = Justification()

        self.setFixedSize(TextPlaceMetrics.width, TextPlaceMetrics.height)

        default_family = self._get_default_font_family()
        default_size = 12
        
        self.current_font_family = default_family
        self.current_font_size = default_size

        self.edit_widget.request_font_family.connect(self.apply_font_family)
        self.edit_widget.request_font_size.connect(self.apply_font_size)
        self.edit_widget.request_align_right.connect(lambda: self.justification.justify_right(editor=self))
        self.edit_widget.request_align_left.connect(lambda: self.justification.justify_left(editor=self))
        self.edit_widget.request_align_center.connect(lambda: self.justification.justify_center(editor=self))
        self.edit_widget.request_align_justify.connect(lambda: self.justification.justify_all(editor=self))
        self.edit_widget.request_copy.connect(self.copy)
        self.edit_widget.request_cut.connect(self.cut)
        self.edit_widget.request_paste.connect(self.paste)
        self.edit_widget.request_undo.connect(self.undo)
        self.edit_widget.request_redo.connect(self.redo)
        self.edit_widget.request_select_all.connect(self.selectAll)
        # self.view.request_zoomIn.connect(self.zoom_in)
        # self.view.request_zoomOut.connect(self.zoom_out)
        # self.view.request_reset_zoom.connect(self.reset)
  

        self._apply_current_font()
        self.setUndoRedoEnabled(True)

        return None



    def _get_default_font_family(self) -> str:
        fonts = self.font_format_model.get_fonts()
        for font in fonts:
            if font.title == "نازنین":
                return font.family
        
        return "Sans Serif"
        

    def apply_font_family(self, family: str) -> None:
        if not family:
            return None

        cursor = self.textCursor()
       

        # اگر متن انتخاب شده بود فقط روی همان متن اعمال شود
        if cursor.hasSelection():
            self.font_format_model.change_font_family(self, family)
            return None

        # اگر انتخابی نبود، فقط state را آپدیت کن
        self.current_font_family = family
        self._apply_current_font()
        return None
        


    def apply_font_size(self, size: int) -> None:

        if size <= 0:
            return None

        cursor = self.textCursor()

        # اگر متن انتخاب شده بود فقط روی همان متن اعمال شود
        if cursor.hasSelection():
            self.font_format_model.change_font_size(self, size)
            return None

        # اگر انتخابی نبود، فقط state را آپدیت کن
        self.current_font_size = size
        self._apply_current_font()
        return None
        

    def _make_current_font(self) -> QFont:
        font = QFont()
        font.setFamily(self.current_font_family)
        font.setPointSize(self.current_font_size)
        return font
    
    def _apply_current_font(self):
        font = self._make_current_font()
        self.setFont(font)
        self.setCurrentFont(font)
        self.document().setDefaultFont(font)

    def zoom_in(self):
        print("zoom in")
        self.zoomIn(2)

    def zoom_out(self):
        print("zoom out")
        self.zoomOut(2)

    def reset(self):
        self._apply_current_font()
        