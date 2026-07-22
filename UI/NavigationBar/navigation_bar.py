import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QButtonGroup, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QIcon
from PersianPad.shared.metrics import NavigationBarMetrics
from PersianPad.shared.colors import NavigationBarColors
from PersianPad.core.font_loader import FontLoader
from PersianPad.shared.fonts import Fonts

class NavigationBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAutoFillBackground(True)
        self.setObjectName("NavigationBar")
        self.setLayoutDirection(Qt.RightToLeft)
        self.setFixedSize(NavigationBarMetrics.width, NavigationBarMetrics.height)
        self.fontLoader = FontLoader()
        self.font = self.fontLoader.load_font(font_name=Fonts.DEFAULT_FONT_NAME)
        self.setFont(self.font)

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)

        self.file_btn = QPushButton("فایل")
        self.edit_btn = QPushButton("ویرایش")
        self.page_setup_btn = QPushButton("صفحه")
        self.view_btn = QPushButton("نمایش")
        self.help_btn = QPushButton("راهنما")

        pixmap = QPixmap("UI/NavigationBar/icons/setting.png")
        pixmap.scaled(24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.setting_btn = QPushButton()
        self.setting_btn.setIcon(QIcon(pixmap))
        self.setting_btn.setObjectName("setting_button")
        self.setting_btn.setFixedSize(NavigationBarMetrics.btn_width / 2, NavigationBarMetrics.btn_height)

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

        self.setStyleSheet(f"""
                        QWidget#NavigationBar  {{
                            background-color: {NavigationBarColors.BACKGROUND_COLOR.name()};
                            border-radius: 0px;
                            margin: 0px;
                            border: none;
                            padding: 0px;
                        }}
                        QPushButton {{
                            background-color: {NavigationBarColors.BACKGROUND_COLOR_BTN.name()};
                            color: {NavigationBarColors.TEXT_COLOR_PRIMARY.name()};
                            border: none;
                            margin: 0px;
                            padding: 0px;
                        }}
                        
                        QPushButton:hover {{
                            background-color: {NavigationBarColors.HOVER.name()};
                        }}
                        
                        QPushButton:checked {{
                            background-color: {NavigationBarColors.SELECTED_BTN.name()};
                        }}
                    """)


    def button_clicked(self, btn) -> None:
        print(f"button clicked {btn}\n button text: {btn.text()}")

        return None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NavigationBar()
    window.show()
    sys.exit(app.exec_())