from PySide6.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QWidget, QApplication, QPushButton, QFrame, QComboBox, QLineEdit
from PySide6.QtCore import Qt, Signal
import sys
from app.sizes.metrics import ShowWidgetMetrics


class ShowWidget(QWidget):

    request_zoomIn = Signal()
    request_zoomOut = Signal()
    request_reset_zoom = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setLayoutDirection(Qt.RightToLeft)
        self.setFixedSize(ShowWidgetMetrics.width, ShowWidgetMetrics.height)

        layout = QHBoxLayout()
        layout.setContentsMargins(10, 0, 0, 10)
        layout.setSpacing(10)

        layout.addLayout(self.title_label())
        layout.addLayout(self.part_one())
        layout.addStretch()

        self.setLayout(layout)


    def title_label(self) -> QHBoxLayout:
        #------------- لایوت لیبل سبز ویرایش -------------------
        title_layout = QHBoxLayout()
        title_layout.setContentsMargins(0, 0, 0, 0)

        title_lbl = QLabel("نمایش")
        title_lbl.setAlignment(Qt.AlignCenter)
        title_lbl.setFixedSize(ShowWidgetMetrics.lbl_width, ShowWidgetMetrics.lbl_height)
        title_lbl.setStyleSheet("""font-size: 16px; font-weight: bold; background-color: #5B3491; color: white;""")

        title_layout.addWidget(title_lbl)
        return title_layout
    
    def part_one(self):
        main_lay = QHBoxLayout()
        main_lay.setAlignment(Qt.AlignCenter)
        main_lay.setContentsMargins(0, 0, 0, 0)
        main_lay.setSpacing(10)

        btn_lay = QVBoxLayout()

        zoom_in_btn = QPushButton("+")
        zoom_out_btn = QPushButton("-")
        reset_zoom_btn = QPushButton("↺")

        btn_list = [zoom_in_btn, zoom_out_btn, reset_zoom_btn]
        func_list = [self.request_zoomIn.emit, self.request_zoomOut.emit, self.request_reset_zoom.emit]
        btn_lay.addStretch()
        for btn, func in zip(btn_list, func_list):
            btn.clicked.connect(lambda: print("this buttons will fixed in next version."))
            btn.setFixedSize(ShowWidgetMetrics.btn_width, ShowWidgetMetrics.btn_height)
            btn_lay.addWidget(btn)
        btn_lay.addStretch()
        
        main_lay.addLayout(btn_lay)
        main_lay.addStretch()
        return main_lay
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShowWidget()
    window.show()
    sys.exit(app.exec())