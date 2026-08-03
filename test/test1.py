import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QColorDialog, QTextEdit
from PersianPad.UI._edit_widget.editor_tools.font_setting.widget import FontSetting
from PersianPad.UI._edit_widget.editor_tools.font_setting.controller import FontSettingController
from PersianPad.UI._edit_widget.editor_tools._font_shape.widget import FontShape
from PersianPad.UI._edit_widget.editor_tools._font_shape.controller import FontShapeController


class Test(QWidget):
    def __init__(self):
        super().__init__()

        font_setting = FontSetting()
        text_edit = QTextEdit()
        font_shape = FontShape()

        self.font_setting_controller = FontSettingController(text_edit, font_setting)
        self.font_shape_controller = FontShapeController(text_edit, font_shape)

        layout = QVBoxLayout(self)
        layout.addWidget(font_setting)
        layout.addWidget(font_shape)
        layout.addStretch()
        layout.addWidget(text_edit)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec())