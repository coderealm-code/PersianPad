import sys
from PySide6.QtWidgets import QWidget, QLineEdit, QCheckBox, QLabel, QPushButton
from PySide6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QApplication, QDialog
from PySide6.QtCore import Qt, Signal, QSize
from PySide6.QtGui import QPixmap, QMouseEvent
from PersianPad.widgets.dialogs.search_dialog.search_dialog_metrics import SearchDialogMetrics, BodyMetric, Spacer
from PersianPad.core.icon_maker import IconMaker
from PersianPad.core.font_loader import FontLoader
from PersianPad.core.qss_loader import QssLoader
from PersianPad.shared.fonts import Fonts


class SearchDialog(QDialog):
    request_search: Signal = Signal(str)
    request_next: Signal = Signal()
    request_prev: Signal = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.setFixedSize(SearchDialogMetrics.width, SearchDialogMetrics.height)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setObjectName("search_dialog")
        self.setStyleSheet(QssLoader.load_qss("search_dialog.qss"))
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

        pic: QPixmap = IconMaker.icon(name="search.png", size=QSize(24, 24))
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
        self.search_entry.setPlaceholderText("متن مورد نظر...")
        self.search_entry.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        whole_word_chx: QCheckBox = QCheckBox(parent=body_frame, text="فقط کلمه کامل")
        case_sensitivity_chx: QCheckBox = QCheckBox(parent=body_frame, text="حساس به کوچک و بزرگی حروف")
        regex_chx: QCheckBox = QCheckBox(parent=body_frame, text="استفاده از عبارت منظم")
        search_from_start_chx: QCheckBox = QCheckBox(parent=body_frame, text="جستجو از ابتدا")

        chx_list: list = [whole_word_chx, case_sensitivity_chx, regex_chx, search_from_start_chx]
        obj_names:list = ["whole_word_chx", "case_sensitivity", "regex_chx", "search_from_start_chx"]
        for chx, obj in zip(chx_list, obj_names):
            chx.setObjectName(obj)
            chx.setFont(self.font_loader.load_font(Fonts.DEFAULT_FONT_NAME))
            chx.setFixedSize(BodyMetric.check_box_width, BodyMetric.check_box_height)

        main_layout.addStretch(1)
        main_layout.addWidget(self.search_entry)
        main_layout.addStretch(1)
        main_layout.addWidget(whole_word_chx)
        main_layout.addWidget(case_sensitivity_chx)
        main_layout.addWidget(regex_chx)
        main_layout.addWidget(search_from_start_chx)
        main_layout.addStretch(3)
        body_frame.setLayout(main_layout)
        return body_frame

    def buttons_part(self) -> QFrame:
        buttons_frame: QFrame = QFrame(parent=self)
        buttons_frame.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        buttons_frame.setObjectName("buttons_frame")
        buttons_frame.setFixedSize(SearchDialogMetrics.width, 48)

        main_layout: QHBoxLayout = QHBoxLayout(buttons_frame)
        main_layout.setContentsMargins(10, 0, 10, 0)
        main_layout.setSpacing(5)

        next_button: QPushButton = QPushButton(text="بعدی" ,parent=buttons_frame)
        prev_button: QPushButton = QPushButton(parent=buttons_frame, text="قبلی")
        search_btn : QPushButton = QPushButton(parent=buttons_frame,text="جستجو")

        btn_list: list = [next_button, prev_button, search_btn]
        obj_names: list = ["next_button", "prev_button", "search_btn"]
        func_list: list = [self.request_next.emit, self.request_prev.emit, self.search]
        for btn, obj, func in zip(btn_list, obj_names, func_list):
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setObjectName(obj)
            btn.setFixedSize(BodyMetric.button_width, BodyMetric.button_height)
            btn.setFont(self.font_loader.load_font(Fonts.DEFAULT_FONT_NAME))
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.clicked.connect(func)

        main_layout.addWidget(next_button)
        main_layout.addWidget(prev_button)
        main_layout.addStretch()
        main_layout.addWidget(search_btn)
        buttons_frame.setLayout(main_layout)
        return buttons_frame


    def search(self) -> None:
        text = self.search_entry.text()
        if not text:
            return None
        self.request_search.emit(text)
        return None

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
    window = SearchDialog()
    window.show()
    sys.exit(app.exec())