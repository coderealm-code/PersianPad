from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication, QStackedWidget, QHBoxLayout
from PySide6.QtCore import Qt
import sys

from app.widgets.navigation_panel import NavigationPanel
from app.sizes.metrics import MainWindowMetrics
from app.widgets.pages.home_widget import HomeWidget
from app.widgets.pages.help_widget import HelpWidget
from app.widgets.pages.edit_widget import EditWidget
from app.widgets.pages.show_widget import ShowWidget
from app.widgets.text_place_widget import TextEdit
from app.models.font_format import TextFormatModel
from app.services.file_controler import FileController, FileModel



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setLayoutDirection(Qt.RightToLeft)
        self.setWindowTitle("PersianPad")
        self.setGeometry(120, 60, MainWindowMetrics.width, MainWindowMetrics.height)
        self.stack = QStackedWidget()


        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # لایه اصلی روی central widget
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)

        main_layout.addLayout(self.part_one())
        self.stack.setCurrentIndex(0)

    def part_one(self) -> QVBoxLayout:
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)

        text_edit_lay = QHBoxLayout()
        text_edit_lay.setAlignment(Qt.AlignCenter)

        font_model = TextFormatModel()
        home = HomeWidget(self)
        show = ShowWidget(self)
        help = HelpWidget(self)
        self.edit = EditWidget(self)

        file_model = FileModel()

        self.file_controller = FileController(model=file_model, editor=self.edit.editor, widget=home)
        text_edit_lay.addLayout(self.editor_lay_main())
        
        

        self.edit.request_bold.connect(lambda: font_model.toggle_bold(self.edit.editor))
        self.edit.request_italic.connect(lambda: font_model.toggle_italic(self.edit.editor))
        self.edit.request_underLine.connect(lambda: font_model.toggle_underLine(self.edit.editor))

        self.stack.addWidget(home) # index = 0
        self.stack.addWidget(self.edit) # index = 1
        self.stack.addWidget(show) # index = 2
        self.stack.addWidget(help) # index = 3

        nav_panel = NavigationPanel(self)

        nav_panel.request_home_page.connect(lambda: self.switch_widget(0))
        nav_panel.request_edit_page.connect(lambda: self.switch_widget(1))
        nav_panel.request_show_page.connect(lambda: self.switch_widget(2))
        nav_panel.request_help_page.connect(lambda: self.switch_widget(3))

        layout.addWidget(nav_panel)
        layout.addWidget(self.stack)
        layout.addLayout(text_edit_lay)
        
        return layout


    def switch_widget(self, index):
        self.stack.setCurrentIndex(index)

    def editor_lay_main(self) -> QVBoxLayout:
        editor_lay = QVBoxLayout()
        editor_lay.setAlignment(Qt.AlignCenter)
        editor_lay.addWidget(self.edit.editor)
        return editor_lay

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())