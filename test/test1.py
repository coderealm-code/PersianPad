import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QStackedWidget, QFrame
from UI.edit_widget.editor_tools.widget import EditorTools
from UI.NavigationBar.navigation_bar import NavigationBar
from UI.edit_widget.FilePage.file_page import FilePage


class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.editor = QTextEdit()
        self.editor_tools = EditorTools(self.editor)
        self.file_page = FilePage(editor=self.editor)
        self.navigation_bar = NavigationBar(self)
        self.switch_widget = QStackedWidget(self)

        self.switch_widget.addWidget(self.file_page)
        self.switch_widget.addWidget(self.editor_tools)

        self.navigation_bar.btn_group.idClicked.connect(self.switch_widget_bar)

        layout = QVBoxLayout(self)
        layout.addWidget(self.navigation_bar)
        layout.addWidget(self.HF())
        layout.addWidget(self.switch_widget)
        layout.addWidget(self.editor)

    def switch_widget_bar(self, btn: int) -> None:
        if 0 <= btn < self.switch_widget.count():
            self.switch_widget.setCurrentIndex(btn)

    def HF(self):
        frame = QFrame(self)
        frame.setFrameShape(QFrame.Shape.HLine)
        frame.setFrameShadow(QFrame.Shadow.Sunken)
        frame.setMinimumWidth(self.width())
        return frame

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec())