from PySide6.QtWidgets import QHBoxLayout, QLabel, QWidget, QApplication, QPushButton, QFrame, QVBoxLayout, QListWidget
from PySide6.QtCore import Qt, Signal
from app.sizes.metrics import HomeWidgetMetrics
import sys
import os 
from datetime import datetime
import json


class HomeWidget(QWidget):

    request_open_file = Signal()
    request_save_file = Signal()
    request_new_file  = Signal()
    request_save_as   = Signal()


    def __init__(self, parent=None):
        super().__init__(parent)

        self.setLayoutDirection(Qt.RightToLeft)
        self.setFixedSize(HomeWidgetMetrics.width, HomeWidgetMetrics.height)

        self.recent_files_list = QListWidget()
        self.recent_files_list.itemClicked.connect(self.show_file_information)

        self.information_lbl = QLabel("اطلاعات")
        self.information_lbl.setAlignment(Qt.AlignTop)
        self.information_lbl.setWordWrap(True)
        self.information_lbl.setFixedWidth(300)
        self.load_recent_files()

        layout = QHBoxLayout()
        layout.setContentsMargins(10, 0, 0, 10)
        

        # add the layout parts you made to the main layout
        layout.addLayout(self.first_part_layout())
        layout.addStretch()
        layout.addLayout(self.frameVLine())
        layout.addStretch()
        layout.addLayout(self.third_part_layout())

        self.setLayout(layout)

    def first_part_layout(self) -> QHBoxLayout:
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)

        # Add your widgets for the second part here
        # For example:
        # some_widget = SomeWidget()
        # layout.addWidget(some_widget)

        title_lbl = QLabel("خانه")
        title_lbl.setAlignment(Qt.AlignCenter)
        title_lbl.setFixedSize(HomeWidgetMetrics.lbl_width, HomeWidgetMetrics.lbl_height)
        title_lbl.setStyleSheet("font-size: 20px; font-weight: bold; background-color: #1a4471; color: white;")
        layout.addWidget(title_lbl)

        new_file_btn = QPushButton("فایل جدید")
        open_file_btn = QPushButton("باز کردن فایل")
        save_file_btn = QPushButton("ذخیره فایل")
        save_as_file_btn = QPushButton("ذخیره با نام")

        btn_list = [new_file_btn, open_file_btn, save_file_btn, save_as_file_btn]
        func_list = [self.request_new_file.emit, self.request_open_file.emit,
                     self.request_save_file.emit, self.request_save_as.emit]

        for btn, func in zip(btn_list, func_list):
            btn.setFixedSize(HomeWidgetMetrics.btn_width, HomeWidgetMetrics.btn_height)
            layout.addWidget(btn)
            btn.clicked.connect(func)
        layout.addStretch()
        
        return layout
    
    def frameVLine(self) -> QHBoxLayout:
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)

        # Add your widgets for the second part here
        # For example:
        # some_widget = SomeWidget()
        # layout.addWidget(some_widget)

        line_frame = QFrame()
        line_frame.setFrameShape(QFrame.VLine)
        line_frame.setFrameShadow(QFrame.Sunken)
        line_frame.setStyleSheet("background-color: lightgray;")
        line_frame.setFixedHeight(HomeWidgetMetrics.height - 40)  # Adjust the height as needed
        layout.addWidget(line_frame)

        return layout
    
    def third_part_layout(self) -> QVBoxLayout:
        main_layout = QVBoxLayout()

        upper_layout = QHBoxLayout()
        upper_layout.setContentsMargins(0, 0, 0, 0)
        upper_layout.setSpacing(0)

        lower_layout = QHBoxLayout()
        lower_layout.setContentsMargins(0, 0, 0, 0)
        lower_layout.setSpacing(0)

        # Add your widgets for the second part here
        # For example:
        # some_widget = SomeWidget()
        # layout.addWidget(some_widget)
        recent_files_lbl = QLabel("فایل های اخیر")
        recent_files_lbl.setAlignment(Qt.AlignCenter)
        upper_layout.addWidget(recent_files_lbl)

        
        lower_layout.addWidget(self.recent_files_list)
        lower_layout.addStretch()
        lower_layout.addWidget(self.information_lbl)


        main_layout.addLayout(upper_layout)
        main_layout.addLayout(lower_layout)

        return main_layout

    def add_to_recent_files(self, file_path: str):
        if not file_path:
            return

        items = [
            self.recent_files_list.item(i).text()
            for i in range(self.recent_files_list.count())
        ]

        if file_path not in items:
            self.recent_files_list.insertItem(0, file_path)

        self.save_recent_files()

    def show_file_information(self, item):

        file_path = item.text()

        if not os.path.exists(file_path):
            self.information_lbl.setText("فایل پیدا نشد")
            return

        size = os.path.getsize(file_path)
        modified = datetime.fromtimestamp(
            os.path.getmtime(file_path)
        )

        info = f"""
 نام فایل: {os.path.basename(file_path)}
مسیر: {file_path}
حجم: {size} Byte
آخرین تغییر: {modified}
"""

        self.information_lbl.setText(info)


    def save_recent_files(self):
        files = [
            self.recent_files_list.item(i).text()
            for i in range(self.recent_files_list.count())
        ]

        with open("recent_files.json", "w", encoding="utf-8") as f:
            json.dump(files, f, ensure_ascii=False)
    

    def load_recent_files(self):
        try:
            with open("recent_files.json", "r", encoding="utf-8") as f:
                files = json.load(f)

            self.recent_files_list.addItems(files)

        except FileNotFoundError:
            pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HomeWidget()
    window.show()
    sys.exit(app.exec())