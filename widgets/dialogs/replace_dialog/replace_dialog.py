import sys
from PySide6.QtWidgets import QWidget, QLineEdit, QCheckBox, QLabel, QPushButton
from PySide6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QApplication, QDialog
from PySide6.QtCore import Qt, Signal, QSize
from PySide6.QtGui import QPixmap, QMouseEvent
from PersianPad.widgets.dialogs.replace_dialog.replace_metrics import ReplaceDialogMetrics, Spacer, BodyMetric
from PersianPad.core.icon_maker import IconMaker
from PersianPad.core.font_loader import FontLoader
from PersianPad.core.qss_loader import QssLoader
from PersianPad.shared.fonts import Fonts


class ReplaceDialog(QWidget):
    request_replace_all: Signal = Signal(dict)
    request_replace: Signal = Signal(dict)
    request_search: Signal = Signal(dict)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.setFixedSize(ReplaceDialogMetrics.width, ReplaceDialogMetrics.height)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setObjectName("replace_dialog")
        self.setStyleSheet(QssLoader.load_qss("replace_dialog.qss"))
        self.setAutoFillBackground(True)

        self.font_loader = FontLoader()
        self._drag_pos = None

        self.main_layout: QVBoxLayout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.main_layout.addWidget(self.title_bar())
        self.main_layout.addWidget(self.body_part())
        self.main_layout.addWidget(self.buttons_part())
        self.setLayout(self.main_layout)


    def title_bar(self) -> QFrame:
        title_bar_frame: QFrame = QFrame(parent=self)
        title_bar_frame.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        title_bar_frame.setFixedSize(QSize(BodyMetric.width, BodyMetric.height))
        title_bar_frame.setObjectName("title_bar")

        main_layout: QHBoxLayout = QHBoxLayout(title_bar_frame)
        main_layout.setContentsMargins(0, 0, 10, 0)
        main_layout.setSpacing(10)

        pic: QPixmap = IconMaker.icon(name="replace.png", size=QSize(24, 24))
        pic_label: QLabel = QLabel(parent=title_bar_frame)
        pic_label.setObjectName("pic_label")
        pic_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pic_label.setPixmap(pic)

        title_label: QLabel = QLabel(text="جستجو", parent=title_bar_frame)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setObjectName("title_label")
        title_label.setFont(self.font_loader.load_font(Fonts.DEFAULT_FONT_NAME))

        close_button: QPushButton = QPushButton(parent=title_bar_frame)
        close_button.setObjectName("close_button")
        close_button.setFixedSize(QSize(48, 48))
        close_button.clicked.connect(self.close)
        btn_icon: QPixmap = IconMaker.icon(name="close.png", size=QSize(32, 32))
        close_button.setIcon(btn_icon)

        main_layout.addWidget(pic_label)
        main_layout.addWidget(title_label)
        main_layout.addStretch()
        main_layout.addWidget(close_button)
        title_bar_frame.setLayout(main_layout)
        return title_bar_frame


    def body_part(self) -> QFrame:
        body_frame: QFrame = QFrame(parent=self)
        body_frame.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        body_frame.setObjectName("body_frame")

        main_layout: QVBoxLayout = QVBoxLayout(body_frame)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        self.search_entry: QLineEdit = QLineEdit(parent=body_frame)
        self.search_entry.setFixedSize(BodyMetric.line_edit_width, BodyMetric.line_edit_height)
        self.search_entry.setObjectName("search_entry")
        self.search_entry.setPlaceholderText("متن جستجو...")
        self.search_entry.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.replace_entry: QLineEdit = QLineEdit(parent=body_frame)
        self.replace_entry.setFixedSize(BodyMetric.line_edit_width, BodyMetric.line_edit_height)
        self.replace_entry.setObjectName("replace_entry")
        self.replace_entry.setPlaceholderText("متن جایگزین...")
        self.replace_entry.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.whole_word_chx: QCheckBox = QCheckBox(parent=body_frame, text="فقط کلمه کامل")
        self.case_sensitivity_chx: QCheckBox = QCheckBox(parent=body_frame, text="حساس به کوچک و بزرگی حروف")
        self.regex_chx: QCheckBox = QCheckBox(parent=body_frame, text="استفاده از عبارت منظم")
        self.search_from_start_chx: QCheckBox = QCheckBox(parent=body_frame, text="جستجو از ابتدا")

        chx_list: list = [self.whole_word_chx, self.case_sensitivity_chx, self.regex_chx, self.search_from_start_chx]
        obj_names: list = ["whole_word_chx", "case_sensitivity", "regex_chx", "search_from_start_chx"]
        for chx, obj in zip(chx_list, obj_names):
            chx.setObjectName(obj)
            chx.setFont(self.font_loader.load_font(Fonts.DEFAULT_FONT_NAME))
            chx.setFixedSize(BodyMetric.check_box_width, BodyMetric.check_box_height)

        main_layout.addStretch(1)
        main_layout.addWidget(self.search_entry)
        main_layout.addStretch(1)
        main_layout.addWidget(self.replace_entry)
        main_layout.addStretch(1)
        main_layout.addWidget(self.whole_word_chx)
        main_layout.addWidget(self.case_sensitivity_chx)
        main_layout.addWidget(self.regex_chx)
        main_layout.addWidget(self.search_from_start_chx)
        main_layout.addStretch(3)
        body_frame.setLayout(main_layout)
        return body_frame


    def buttons_part(self) -> QFrame:
        buttons_frame: QFrame = QFrame(parent=self)
        buttons_frame.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        buttons_frame.setObjectName("buttons_frame")
        buttons_frame.setFixedSize(ReplaceDialogMetrics.width, 48)

        main_layout: QHBoxLayout = QHBoxLayout(buttons_frame)
        main_layout.setContentsMargins(10, 0, 10, 0)
        main_layout.setSpacing(5)

        replace_all_button: QPushButton = QPushButton(text="جایگزین همه" ,parent=buttons_frame)
        replace_button: QPushButton = QPushButton(parent=buttons_frame, text="جایگزینی")
        search_btn : QPushButton = QPushButton(parent=buttons_frame,text="جستجو")

        btn_list: list = [replace_all_button, replace_button, search_btn]
        obj_names: list = ["replace_all_button", "replace_button", "search_btn"]
        func_list: list = [lambda: self.request_replace_all.emit(self.get_search_data()),
                           lambda: self.request_replace.emit(self.get_search_data()),
                           lambda: self.request_search.emit(self.get_search_data())]
        for btn, obj, func in zip(btn_list, obj_names, func_list):
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setObjectName(obj)
            btn.setFixedSize(BodyMetric.button_width, BodyMetric.button_height)
            btn.setFont(self.font_loader.load_font(Fonts.DEFAULT_FONT_NAME))
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.clicked.connect(func)

        main_layout.addWidget(replace_all_button)
        main_layout.addWidget(replace_button)
        main_layout.addStretch()
        main_layout.addWidget(search_btn)
        buttons_frame.setLayout(main_layout)
        return buttons_frame

    def get_search_data(self) -> dict:
        return {"search_text": self.search_entry.text(),
                "replace_text": self.replace_entry.text(),
                "whole_word": self.whole_word_chx.isChecked(),
                "match_case": self.case_sensitivity_chx.isChecked(),
                "wrap_search": self.search_from_start_chx.isChecked(),
                "regex": self.regex_chx.isChecked()}



    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self._drag_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self._drag_pos and event.buttons() & Qt.MouseButton.LeftButton:
            self.move(event.globalPosition().toPoint() - self._drag_pos)
            event.accept()

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self._drag_pos = None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReplaceDialog()
    window.show()
    sys.exit(app.exec())