from PySide6.QtWidgets import QWidget, QGroupBox, QVBoxLayout, QApplication
from PySide6.QtCore import Qt
from shared.metrics import FileListMetrics
from widgets.list_widget.list_widget import ListWidget
from UI.edit_widget.FilePage.FileManager.service import FileService


class FilesList(QWidget):
    def __init__(self, service: FileService, parent=None):
        super().__init__(parent)
        self.service: FileService = service
        self.setObjectName("FilesList")
        self.setFixedSize(FileListMetrics.SIZE)

        main_layout: QVBoxLayout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        group_box: QGroupBox = QGroupBox("فایل های اخیر")
        group_layout: QVBoxLayout = QVBoxLayout(group_box)
        group_box.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        group_layout.setContentsMargins(5, 0, 5, 0)
        group_layout.setSpacing(10)

        self.list_widget: ListWidget = ListWidget(group_box)
        for model in self.service.models_list:
            self.list_widget.set_data(model)

        group_layout.addWidget(self.list_widget)
        main_layout.addWidget(group_box)
        self.setLayout(main_layout)





if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = FilesList()
    window.show()
    sys.exit(app.exec())
