from PySide6.QtWidgets import QWidget, QHBoxLayout, QTextEdit, QFrame
from shared.metrics import ContainerWidgetMetrics
from UI.edit_widget.FilePage.FileManager.file_manager import FileManager
from UI.edit_widget.FilePage.FileManager.controller import FileController
from UI.edit_widget.FilePage.FilesList.file_list import FilesList
from UI.edit_widget.FilePage.information_lbl.info_label import InfoLabel
from UI.edit_widget.FilePage.FileManager.service import FileService
from UI.edit_widget.FilePage.FileManager.model import FileModel


class FilePage(QWidget):
    def __init__(self, editor: QTextEdit, parent=None):
        super().__init__(parent)
        self.setFixedSize(ContainerWidgetMetrics.SIZE)

        self.model = FileModel()
        self.service = FileService(self.model, editor)
        self.files_list = FilesList(self)

        self.file_manager = FileManager(self)
        self.controller = FileController(self.files_list, editor, self.file_manager, self.service)


        self.info_label = InfoLabel(self.files_list, self)

        main_layout = QHBoxLayout(self)
        main_layout.addStretch(7)
        main_layout.addWidget(self.info_label)
        main_layout.addStretch(2)
        main_layout.addWidget(self.vertical_line(125))
        main_layout.addStretch(2)
        main_layout.addWidget(self.files_list)
        main_layout.addStretch(2)
        main_layout.addWidget(self.vertical_line(125))
        main_layout.addStretch(2)
        main_layout.addWidget(self.file_manager)

    @staticmethod
    def vertical_line(height: int) -> QFrame:
        line = QFrame()
        line.setFrameShape(QFrame.Shape.VLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        line.setFixedHeight(height)
        line.setStyleSheet("background-color: #e8e8e8;"
                           "border: none;")
        line.setFixedWidth(2)
        return line

