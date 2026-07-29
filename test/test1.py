import sys

from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout
from PersianPad.widgets.RibbonButton.vertical_button import VerticalButton
from PersianPad.shared.fonts import Fonts
from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QPainter, QTextOption
from PySide6.QtCore import Qt

class RTLLineEdit(QLineEdit):
    def paintEvent(self, event):
        painter = QPainter(self)
        option = QTextOption()
        option.setTextDirection(Qt.RightToLeft)   # جهت نوشتن RTL
        option.setAlignment(Qt.AlignRight)        # اشاره‌گر از راست شروع بشه

        # متن فعلی
        text = self.text()

        # رسم متن با تنظیمات جدید
        rect = self.rect()
        painter.drawText(rect, text, option)




class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Persian Pad")

        self.button1 = VerticalButton(text="فایل", icon_name="document.png", font_name=Fonts.DEFAULT_FONT_NAME)
        self.button2 = VerticalButton(text="ذخیره", icon_name="save.png", font_name=Fonts.DEFAULT_FONT_NAME)
        self.button3 = VerticalButton(text="ذخیره با نام", icon_name="save_as.png", font_name=Fonts.DEFAULT_FONT_NAME)
        self.button4 = VerticalButton(text="فایل جدید", icon_name="new_file.png", font_name=Fonts.DEFAULT_FONT_NAME)
        self.button5 = VerticalButton(text="بازکردن", icon_name="open.png", font_name=Fonts.DEFAULT_FONT_NAME)

        btn_list = [self.button1, self.button2, self.button3, self.button4, self.button5]
        for btn in btn_list:
            btn.setFixedSize(80, 100)

        search_entry: QLineEdit = RTLLineEdit(parent=self)


        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(10)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        layout.addWidget(search_entry)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())