import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QColorDialog, QTextEdit
from PersianPad.UI._edit_widget.editor_tools.widget import EditorTools
from PersianPad.UI._edit_widget.editor_tools.controller import EditorToolsController
from PersianPad.UI._edit_widget.editor_tools._font_shape.widget import FontShape
from PersianPad.UI._edit_widget.editor_tools.font_setting.widget import FontSetting
from PersianPad.UI._edit_widget.editor_tools.clip_board.widget import ClipBoardWidget
from PersianPad.UI._edit_widget.editor_tools.find_replace.widget import FindReplaceText
from PersianPad.UI._edit_widget.editor_tools.text_justification.widget import TextJustify


class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.editor = QTextEdit()

        self.font_shape = FontShape()
        self.font_setting = FontSetting()
        self.text_justify = TextJustify()
        self.Find_Replace_Text = FindReplaceText()
        self.Clip_Board_Widget = ClipBoardWidget()
        self.controller = EditorToolsController(font_shape=self.font_shape, font_setting=self.font_setting, text_justification=self.text_justify,
                                                find_replace=self.Find_Replace_Text, clip_board=self.Clip_Board_Widget, editor=self.editor)
        self.editor_tools = EditorTools(font_shape=self.font_shape, font_setting=self.font_setting, text_justification=self.text_justify,
                                                find_replace=self.Find_Replace_Text, clip_board=self.Clip_Board_Widget, controller=self.controller)


        layout = QVBoxLayout(self)
        layout.addWidget(self.editor_tools)
        layout.addWidget(self.editor)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec())