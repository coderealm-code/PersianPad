import sys

from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout
from PersianPad.widgets.RibbonButton.vertical_button import VerticalButton


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Persian Pad")

        self.button1 = VerticalButton(text="فایل", icon="document.png")
        self.button2 = VerticalButton(text="ذخیره", icon="save.png")
        self.button3 = VerticalButton(text="ذخیره با نام", icon="save_as.png")
        self.button4 = VerticalButton(text="فایل جدید", icon="new_file.png")
        self.button5 = VerticalButton(text="بازکردن", icon="open.png")

        btn_list = [self.button1, self.button2, self.button3, self.button4, self.button5]
        for btn in btn_list:
            btn.setFixedSize(80, 100)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(10)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())