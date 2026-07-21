from PySide6.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QWidget, QApplication, QPushButton, QFrame, QComboBox, QLineEdit
from PySide6.QtCore import Qt
from app.sizes.metrics import HelpWidgetMetrics
import sys


class HelpWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setLayoutDirection(Qt.RightToLeft)
        self.setFixedSize(HelpWidgetMetrics.width, HelpWidgetMetrics.height)

        layout = QHBoxLayout()
        layout.setContentsMargins(10, 0, 0, 10)
        layout.setSpacing(10)

        layout.addLayout(self.title_label())

        layout.addStretch()

        self.setLayout(layout)


    def title_label(self) -> QHBoxLayout:
        #------------- لایوت لیبل سبز ویرایش -------------------
        title_layout = QHBoxLayout()
        title_layout.setContentsMargins(0, 0, 0, 0)

        title_lbl = QLabel("کمک")
        title_lbl.setAlignment(Qt.AlignCenter)
        title_lbl.setFixedSize(HelpWidgetMetrics.lbl_width, HelpWidgetMetrics.lbl_height)
        title_lbl.setStyleSheet("""font-size: 16px; font-weight: bold; background-color: #7E5F42; color: white;""")

        title_layout.addWidget(title_lbl)
        return title_layout
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HelpWidget()
    window.show()
    sys.exit(app.exec())