import sys
from PySide6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QGroupBox, QApplication
from PySide6.QtCore import Qt, Signal
from PersianPad.shared.fonts import Fonts
from PersianPad.widgets.RibbonButton.vertical_button import VerticalButton
from PersianPad.widgets.color_button.widget import ColorButton
from PersianPad.shared.metrics import FontSettingMetrics


class FontSetting(QFrame):
    request_highlight: Signal = Signal()
    request_color: Signal = Signal()
    request_bold: Signal = Signal()
    request_italic: Signal = Signal()
    request_underLine: Signal = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.setMinimumWidth(FontSettingMetrics.size.width())
        self.setFixedHeight(FontSettingMetrics.size.height())

        main_layout: QVBoxLayout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        groupBox: QGroupBox = QGroupBox("تنظیمات متن")
        group_layout: QHBoxLayout = QHBoxLayout(groupBox)
        groupBox.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        group_layout.setContentsMargins(5, 0, 5, 0)
        group_layout.setSpacing(10)

        self.highlight: VerticalButton = VerticalButton(parent=groupBox, text="هایلایت",
                                    font_name=Fonts.DEFAULT_FONT_NAME,
                                    icon_name="highlight.png")

        self.text_color: ColorButton  = ColorButton(parent=groupBox, text="رنگ متن",
                                   font_name=Fonts.DEFAULT_FONT_NAME,
                                   icon_name="color.png")

        self.bold: VerticalButton  = VerticalButton(parent=groupBox, text="درشت",
                                     font_name=Fonts.DEFAULT_FONT_NAME,
                                     icon_name="bold.png")
        self.bold.setActive(True)

        self.italic: VerticalButton  = VerticalButton(parent=groupBox, text="کج",
                                      font_name=Fonts.DEFAULT_FONT_NAME,
                                      icon_name="italic.png")
        self.italic.setActive(True)

        self.under_line: VerticalButton  = VerticalButton(parent=groupBox, text="زیر خط",
                                   font_name=Fonts.DEFAULT_FONT_NAME,
                                   icon_name="underline.png")
        self.under_line.setActive(True)


        btn_list: list[VerticalButton] = [self.highlight, self.text_color, self.bold, self.italic, self.under_line]
        func_list: list = [self.request_highlight.emit, self.request_color.emit, self.request_bold.emit,
                           self.request_italic.emit, self.request_underLine.emit]
        for btn, func in zip(btn_list, func_list):
            btn.clicked.connect(func)
            btn.setFixedSize(FontSettingMetrics.btn_size)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)

        group_layout.addWidget(self.highlight)
        group_layout.addWidget(self.text_color)
        group_layout.addWidget(self.bold)
        group_layout.addWidget(self.italic)
        group_layout.addWidget(self.under_line)
        main_layout.addWidget(groupBox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FontSetting()
    window.show()
    sys.exit(app.exec())