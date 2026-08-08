from PySide6.QtWidgets import QTextEdit

from PersianPad.UI._edit_widget.editor_tools._font_shape.controller import FontShapeController
from PersianPad.UI._edit_widget.editor_tools.font_setting.controller import FontSettingController
from PersianPad.UI._edit_widget.editor_tools.clip_board.controller import ClipBoardController
from PersianPad.UI._edit_widget.editor_tools.find_replace.controller import FindReplaceController
from PersianPad.UI._edit_widget.editor_tools.text_justification.controller import TextJustificationController

from PersianPad.UI._edit_widget.editor_tools._font_shape.widget import FontShape
from PersianPad.UI._edit_widget.editor_tools.font_setting.widget import FontSetting
from PersianPad.UI._edit_widget.editor_tools.clip_board.widget import ClipBoardWidget
from PersianPad.UI._edit_widget.editor_tools.find_replace.widget import FindReplaceText
from PersianPad.UI._edit_widget.editor_tools.text_justification.widget import TextJustify

from PersianPad.UI._edit_widget.editor_tools.find_replace.model import FindReplaceModel

class EditorToolsController:
    def __init__(self, editor: QTextEdit, font_shape: FontShape, clip_board: ClipBoardWidget, find_replace: FindReplaceText,
                 font_setting: FontSetting, text_justification: TextJustify):
        self.editor = editor
        #-------------------- widgets ------------------------------
        self.font_shape = font_shape
        self.clip_board = clip_board
        self.find_replace = find_replace
        self.font_setting = font_setting
        self.text_justification = text_justification
        # -------------------- models --------------------------------
        self.find_replace_model = FindReplaceModel()
        # -------------------- controllers ---------------------------
        self.Font_Shape_Controller: FontShapeController = FontShapeController(editor=self.editor, widget=self.font_shape)
        self.Clip_Board_Controller: ClipBoardController = ClipBoardController(editor=self.editor, widget=self.clip_board)
        self.Font_setting_controller: FontSettingController = FontSettingController(editor=self.editor, widget=self.font_setting)
        self.find_replace_controller: FindReplaceController = FindReplaceController(widget=self.find_replace, editor=self.editor, model=self.find_replace_model)
        self.text_justification_controller: TextJustificationController = TextJustificationController(editor=self.editor, widget=self.text_justification)


