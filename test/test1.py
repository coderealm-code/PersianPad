import sys

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QColorDialog, QTextEdit
from PersianPad.UI._edit_widget.editor_tools.font_setting.widget import FontSetting
from PersianPad.UI._edit_widget.editor_tools.font_setting.controller import FontSettingController



class Test(QWidget):
    def __init__(self):
        super().__init__()

        window = FontSetting()
        text_edit = QTextEdit()

        self.controller = FontSettingController(text_edit, window)  # ← این مهم‌ترین خط است

        layout = QVBoxLayout(self)
        layout.addWidget(window)
        layout.addStretch()
        layout.addWidget(text_edit)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec())