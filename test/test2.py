from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QGroupBox,
    QVBoxLayout,
    QPushButton
)
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        group = QGroupBox("تنظیمات فایل")
        group.setLayoutDirection(Qt.RightToLeft)

        button1 = QPushButton("باز کردن")
        button2 = QPushButton("ذخیره")

        layout = QVBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)
        group.setLayout(layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(group)

        self.setLayout(main_layout)
        self.setStyleSheet("""QGroupBox {
    border: 1px solid #555;
    border-radius: 8px;
    margin-top: 12px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 15px;
    padding: 0 5px;
}""")



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())