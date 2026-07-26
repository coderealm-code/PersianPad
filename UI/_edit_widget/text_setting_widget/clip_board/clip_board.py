import sys
from PySide6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QGroupBox, QApplication
from PySide6.QtCore import Qt
from PersianPad.shared.fonts import Fonts
from PersianPad.widgets.RibbonButton.vertical_button import VerticalButton


class ClipBoardWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayoutDirection(Qt.RightToLeft)
        self.main_layout = QVBoxLayout()

        self.groupBox = QGroupBox(self, title="کلیپ بورد")
        self.groupBox.setLayoutDirection(Qt.RightToLeft)
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.group_layout = QHBoxLayout(self.groupBox)
        self.group_layout.setContentsMargins(0,0,0,0)
        self.group_layout.setSpacing(0)

        self.copy_btn = VerticalButton(text="کپی", icon_name="copy.png", font=Fonts.FONT_VAZIR)
        self.cut_btn = VerticalButton(text="انتقال", icon_name="cut.png", font=Fonts.FONT_VAZIR)
        self.paste_btn = VerticalButton(text="چسپاندن", icon_name="paste.png", font=Fonts.FONT_VAZIR)

        self.group_layout.addStretch()
        self.group_layout.addWidget(self.copy_btn)
        self.group_layout.addWidget(self.cut_btn)
        self.group_layout.addWidget(self.paste_btn)
        self.group_layout.addStretch()
        self.groupBox.setLayout(self.group_layout)

        self.main_layout.addWidget(self.groupBox)
        self.setLayout(self.main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClipBoardWidget()
    window.show()
    sys.exit(app.exec())
