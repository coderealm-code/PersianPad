import sys
from PySide6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QGroupBox, QApplication
from PySide6.QtCore import Qt, Signal
from PersianPad.shared.fonts import Fonts
from PersianPad.widgets.RibbonButton.vertical_button import VerticalButton
from PersianPad.shared.metrics import ClipboardMetrics


class ClipBoardWidget(QFrame):
    request_copy: Signal = Signal()
    request_cut: Signal = Signal()
    request_paste: Signal = Signal()

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setMinimumSize(ClipboardMetrics.width, ClipboardMetrics.height)
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.main_layout: QVBoxLayout = QVBoxLayout()

        self.groupBox: QGroupBox = QGroupBox(self, title="کلیپ بورد")
        self.groupBox.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.group_layout = QHBoxLayout(self.groupBox)
        self.group_layout.setContentsMargins(0,0,0,0)
        self.group_layout.setSpacing(0)

        self.copy_btn: VerticalButton = VerticalButton(text="کپی", icon_name="copy.png", font_name=Fonts.FONT_VAZIR)
        self.cut_btn: VerticalButton = VerticalButton(text="انتقال", icon_name="cut.png", font_name=Fonts.FONT_VAZIR)
        self.paste_btn: VerticalButton = VerticalButton(text="چسپاندن", icon_name="paste.png", font_name=Fonts.FONT_VAZIR)

        btn_list: list = [self.copy_btn, self.cut_btn, self.paste_btn]
        func_list: list = [self.request_copy.emit, self.request_cut.emit, self.request_paste.emit]
        for btn, func in zip(btn_list, func_list):
            btn.setFixedSize(ClipboardMetrics.btn_width, ClipboardMetrics.btn_height)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.clicked.connect(func)

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
