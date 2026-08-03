import sys
from PySide6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QGroupBox, QApplication
from PySide6.QtCore import Qt, Signal
from PersianPad.shared.fonts import Fonts
from PersianPad.widgets.RibbonButton.vertical_button import VerticalButton
from PersianPad.shared.metrics import TextJustifyMetrics


class TextJustify(QFrame):
    request_right: Signal = Signal()
    request_left: Signal = Signal()
    request_center: Signal = Signal()
    request_justify: Signal = Signal()
    request_list: Signal = Signal()
    request_num_lines: Signal = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.setMinimumWidth(TextJustifyMetrics.size.width())
        self.setFixedHeight(TextJustifyMetrics.size.height())

        main_layout: QVBoxLayout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        groupBox: QGroupBox = QGroupBox("چینش پاراگراف")
        group_layout: QHBoxLayout = QHBoxLayout(groupBox)
        groupBox.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        group_layout.setContentsMargins(5, 0, 5, 0)
        group_layout.setSpacing(10)

        self.right = VerticalButton(parent=groupBox, text="راست چین",
                                    font_name=Fonts.DEFAULT_FONT_NAME,
                                    icon_name="right-align.png")

        self.left = VerticalButton(parent=groupBox, text="چپ چین",
                                   font_name=Fonts.DEFAULT_FONT_NAME,
                                   icon_name="left-align.png")

        self.center = VerticalButton(parent=groupBox, text="وسط چین",
                                     font_name=Fonts.DEFAULT_FONT_NAME,
                                     icon_name="center-alignment.png")

        self.justify = VerticalButton(parent=groupBox, text="منظم",
                                      font_name=Fonts.DEFAULT_FONT_NAME,
                                      icon_name="justify-align.png")

        self.list = VerticalButton(parent=groupBox, text="لیست",
                                   font_name=Fonts.DEFAULT_FONT_NAME,
                                   icon_name="list.png")

        self.num_list = VerticalButton(parent=groupBox, text="لیست شماره",
                                       font_name=Fonts.DEFAULT_FONT_NAME,
                                       icon_name="list(1).png")

        btn_list: list[VerticalButton] = [self.right, self.left, self.center, self.justify, self.list, self.num_list]
        func_list: list = [self.request_right.emit, self.request_left.emit, self.request_center.emit,
                           self.request_justify.emit, self.request_list.emit, self.request_num_lines.emit]
        for btn, func in zip(btn_list, func_list):
            btn.clicked.connect(func)
            btn.setFixedSize(TextJustifyMetrics.btn_size)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)

        group_layout.addWidget(self.right)
        group_layout.addWidget(self.left)
        group_layout.addWidget(self.center)
        group_layout.addWidget(self.justify)
        group_layout.addWidget(self.list)
        group_layout.addWidget(self.num_list)

        main_layout.addWidget(groupBox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextJustify()
    window.show()
    sys.exit(app.exec())