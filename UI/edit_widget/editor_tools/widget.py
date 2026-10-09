from PySide6.QtWidgets import QHBoxLayout, QFrame, QTextEdit
from PySide6.QtCore import Qt
from UI.edit_widget.editor_tools.font_shape.widget import FontShape
from UI.edit_widget.editor_tools.font_setting.widget import FontSetting
from UI.edit_widget.editor_tools.clip_board.widget import ClipBoardWidget
from UI.edit_widget.editor_tools.find_replace.widget import FindReplaceText
from UI.edit_widget.editor_tools.text_justification.widget import TextJustify
from UI.edit_widget.editor_tools.controller import EditorToolsController
from shared.metrics import TextSettingsMetrics



class EditorTools(QFrame):
    def __init__(self, editor: QTextEdit, parent=None):
        super().__init__(parent)
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.setMinimumWidth(TextSettingsMetrics.size.width())
        self.setFixedHeight(TextSettingsMetrics.size.height())

         # همه ساخنه شود فقط ادیتور ورودی باشد!
        self.editor = editor
        self.find_replace = FindReplaceText(self)
        self.font_shape = FontShape(self)
        self.clip_board = ClipBoardWidget(self)
        self.font_setting = FontSetting(self)
        self.text_justification = TextJustify(self)
        self.controller = EditorToolsController(self.editor, self.font_shape, self.clip_board, self.find_replace,
                                                self.font_setting, self.text_justification)

        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 5, 0)
        self.main_layout.setSpacing(0)

        widgets: list[QFrame] = [self.clip_board, self.font_setting, self.font_shape, self.text_justification, self.find_replace]
        for w in widgets:
            self.main_layout.addWidget(w)
            self.main_layout.addStretch()

