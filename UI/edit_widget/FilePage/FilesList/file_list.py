from PySide6.QtWidgets import QWidget, QGroupBox, QVBoxLayout
from PySide6.QtCore import Qt
from UI.edit_widget.FilePage.FileManager.model import FileModel
from shared.metrics import FileListMetrics
from widgets.list_widget.list_widget import ListWidget


class FilesList(QWidget):
    def __init__(self, parent:QWidget | None=None):
        super().__init__(parent)
        self.setObjectName("FilesList")
        self.setFixedSize(FileListMetrics.SIZE)

        main_layout: QVBoxLayout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        group_box: QGroupBox = QGroupBox("فایل های اخیر")
        group_layout: QVBoxLayout = QVBoxLayout(group_box)
        group_box.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        group_layout.setContentsMargins(0, 0, 0, 0)
        group_layout.setSpacing(0)

        self.list_widget: ListWidget = ListWidget(group_box)

        group_layout.addWidget(self.list_widget)
        main_layout.addWidget(group_box)
        self.setLayout(main_layout)

    def add_file(self, model: FileModel) -> None:
        self.list_widget.set_data(model)





