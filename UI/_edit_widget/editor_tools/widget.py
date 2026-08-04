import sys
from PySide6.QtWidgets import QHBoxLayout, QApplication, QFrame
from PySide6.QtCore import Qt
from PersianPad.UI._edit_widget.editor_tools._font_shape.widget import FontShape
from PersianPad.UI._edit_widget.editor_tools.font_setting.widget import FontSetting
from PersianPad.UI._edit_widget.editor_tools.clip_board.clip_board import ClipBoardWidget
from PersianPad.UI._edit_widget.editor_tools.find_replace.find_replace_widget import FindReplaceText
from PersianPad.UI._edit_widget.editor_tools.text_justification.text_justification import TextJustify


class EditorTools(QFrame):
    def __init__(self, controller, font_shape: FontShape, clip_board: ClipBoardWidget, find_replace: FindReplaceText,
                 font_setting: FontSetting, text_justification: TextJustify, parent=None):
        super().__init__(parent)
        self.layoutDirection(Qt.LayoutDirection.RightToLeft)

        self.controller = controller
        self.find_replace = find_replace
        self.font_shape = font_shape
        self.clip_board = clip_board
        self.font_setting = font_setting
        self.text_justification = text_justification

        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)

        self.main_layout.addStretch()
        self.main_layout.addWidget(self.clip_board)
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.font_shape)
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.font_setting)
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.text_justification)
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.find_replace)
        self.main_layout.addStretch()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EditorTools()
    window.show()
    sys.exit(app.exec())