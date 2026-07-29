import sys
from PySide6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QGroupBox, QApplication
from PySide6.QtCore import Qt, Signal
from PersianPad.shared.fonts import Fonts
from PersianPad.widgets.RibbonButton.vertical_button import VerticalButton
from PersianPad.shared.metrics import FindReplaceMetrics


class FindReplaceText(QFrame):
    request_search: Signal = Signal()
    request_replace: Signal = Signal()

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.setMinimumHeight(FindReplaceMetrics.height)

        main_layout: QVBoxLayout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        groupBox: QGroupBox = QGroupBox("جستجو و جایگزین")
        group_layout: QHBoxLayout = QHBoxLayout(groupBox)
        groupBox.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        group_layout.setContentsMargins(0, 0, 0, 0)
        group_layout.setSpacing(10)

        self.search_btn: VerticalButton = VerticalButton(text="جستجو", icon_name="search.png", font_name=Fonts.DEFAULT_FONT_NAME)
        self.replace_btn: VerticalButton = VerticalButton(text="جایگزین", icon_name="replace.png", font_name=Fonts.DEFAULT_FONT_NAME)
        btn_list: list = [self.search_btn, self.replace_btn]
        func_list: list = [self.request_search.emit, self.request_replace.emit]
        for btn, func in zip(btn_list, func_list):
            btn.setFixedSize(FindReplaceMetrics.btn_width, FindReplaceMetrics.btn_height)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.clicked.connect(func)

        group_layout.addWidget(self.search_btn)
        group_layout.addWidget(self.replace_btn)

        main_layout.addWidget(groupBox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FindReplaceText()
    window.show()
    sys.exit(app.exec())