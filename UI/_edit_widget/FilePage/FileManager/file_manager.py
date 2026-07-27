import sys
from PersianPad.shared.metrics import FileManagerMetrics
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QVBoxLayout, QFrame
from PySide6.QtCore import Qt, Signal
from PersianPad.widgets.RibbonButton.vertical_button import VerticalButton


class FileManager(QWidget):

    request_new_file: Signal = Signal()
    request_open_file: Signal = Signal()
    request_save_file: Signal = Signal()
    request_save_as_file: Signal = Signal()
    request_export_pdf: Signal = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setLayoutDirection(Qt.RightToLeft)
        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color: #ffffff;")

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        lbl_layout = QHBoxLayout()
        lbl_layout.setContentsMargins(0, 0, 0, 0)
        lbl_layout.setSpacing(0)
        lbl_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label = QLabel("مدیریت فایل", self)
        self.title_label.setFixedHeight(FileManagerMetrics.label_height)
        self.title_label.setStyleSheet("font_name-weight: bold;")
        lbl_layout.addWidget(self.title_label)

        self.btn_layout = QHBoxLayout()
        self.btn_layout.setContentsMargins(0 ,0 , 0, 0)
        self.btn_layout.setSpacing(10)

        self.new_file = VerticalButton(text="جدید", icon="new.png")
        self.open_file = VerticalButton(text="بازکردن", icon="open.png")
        self.save_file = VerticalButton(text="ذخیره", icon="save.png")
        self.save_as_file = VerticalButton(text="ذخیره با نام", icon="save_as.png")
        self.export_pdf = VerticalButton(text="خروجی PDF", icon="pdf.png")

        btn_list = [self.new_file, self.open_file, self.save_file, self.save_as_file, self.export_pdf]
        func_list = [self.request_new_file.emit, self.request_open_file.emit,
                     self.request_save_file.emit, self.request_save_as_file.emit,
                     self.request_export_pdf.emit]
        btn_object_name_list = ["new_file", "open_file", "save_file", "save_as_file", "export_pdf"]
        for btn, func, object in zip(btn_list, func_list, btn_object_name_list):
            btn.clicked.connect(func)
            btn.setObjectName(object)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setFixedSize(FileManagerMetrics.button_width, FileManagerMetrics.button_height)

            if btn == btn_list[-1]:
                self.btn_layout.addWidget(btn)
                self.btn_layout.addStretch()
                break
            if btn == btn_list[0]:
                self.btn_layout.addStretch()
            self.btn_layout.addWidget(btn)
            self.btn_layout.addStretch()
            self.btn_layout.addWidget(self.verical_line(120))
            self.btn_layout.addStretch()

        self.main_layout.addLayout(self.btn_layout)
        self.main_layout.addStretch()
        self.main_layout.addLayout(lbl_layout)
        self.setLayout(self.main_layout)

    def verical_line(self, height: int) -> QFrame:
        line = QFrame()
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setFixedHeight(height)
        line.setStyleSheet("background-color: #e8e8e8;"
                           "border: none;")
        line.setFixedWidth(2)
        return line


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileManager()
    window.show()
    sys.exit(app.exec())