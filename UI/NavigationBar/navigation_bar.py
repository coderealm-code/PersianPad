import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QButtonGroup, QHBoxLayout
from PySide6.QtCore import Qt
from PersianPad.metrics.metrics import NavigationBarMetrics

class NavigationBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayoutDirection(Qt.RightToLeft)
        self.setFixedSize(NavigationBarMetrics.width, NavigationBarMetrics.height)

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)

        self.file_btn = QPushButton("فایل")
        self.edit_btn = QPushButton("ویرایش")
        self.page_setup_btn = QPushButton("صفحه")
        self.view_btn = QPushButton("نمایش")
        self.help_btn = QPushButton("راهنما")

        self.setting_btn = QPushButton("تنظیمات")
        self.setting_btn.setObjectName("setting_button")
        self.setting_btn.setFixedSize(NavigationBarMetrics.btn_width, NavigationBarMetrics.btn_height)

        self.btn_group = QButtonGroup(self)
        self.btn_group.setExclusive(True)
        self.btn_group.buttonClicked.connect(self.button_clicked)
        btn_id = 1

        btn_list = [self.file_btn, self.edit_btn, self.page_setup_btn, self.view_btn, self.help_btn]
        object_name_list = ["file_button", "edit_button", "page_setup_button", "view_button", "help_button"]

        for btn, object_name in zip(btn_list, object_name_list):
            self.layout.addWidget(btn)
            self.btn_group.addButton(btn, btn_id)

            btn.setObjectName(object_name)
            btn.setCheckable(True)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setFixedSize(NavigationBarMetrics.btn_width, NavigationBarMetrics.btn_height)
            btn_id += 1
        self.file_btn.setChecked(True)

        self.layout.addStretch()
        self.layout.addWidget(self.setting_btn)

        self.setLayout(self.layout)


    def button_clicked(self, id):
        print(f"button clicked {id}\n button text: {id.text()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NavigationBar()
    window.show()
    sys.exit(app.exec_())