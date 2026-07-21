from PySide6.QtWidgets import QHBoxLayout, QWidget, QApplication, QPushButton
from PySide6.QtCore import Qt, Signal
import sys
from app.sizes.metrics import NavigationPanelMetrics


class NavigationPanel(QWidget):
    request_home_page = Signal()
    request_edit_page = Signal()
    request_show_page = Signal()
    request_help_page = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedSize(NavigationPanelMetrics.width, NavigationPanelMetrics.height)
        self.setLayoutDirection(Qt.RightToLeft)
        
        self.setLayout(self.ui_part())

    def ui_part(self) -> QHBoxLayout:
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        

        self.home_btn = QPushButton("خانه")
        self.edit_btn = QPushButton("ویرایش")
        self.show_btn = QPushButton("نمایش")
        self.help_btn = QPushButton("راهنما")

        btn_list = [self.home_btn, self.edit_btn, self.show_btn, self.help_btn]
        func_list = [self.request_home_page.emit, self.request_edit_page.emit, self.request_show_page.emit, self.request_help_page.emit]

        # اتصال هر دکمه به تابع خودش
        for btn, func in zip(btn_list, func_list):
            btn.setFixedSize(NavigationPanelMetrics.btn_width, NavigationPanelMetrics.btn_height)
            layout.addWidget(btn)
            btn.clicked.connect(func)

        layout.addStretch()
        return layout

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NavigationPanel()
    window.show()
    sys.exit(app.exec())