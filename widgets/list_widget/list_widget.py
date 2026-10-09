import sys
from PySide6.QtWidgets import QApplication, QListWidget, QListWidgetItem
from PySide6.QtCore import Qt

from core.icon_maker import IconMaker
from core.qss_loader import QssLoader
from widgets.list_widget.Style import CustomDelegate
from shared.metrics import ListWidgetMetrics
from UI.edit_widget.FilePage.FileManager.model import FileModel


class ListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("ListWidget")
        self.setFixedSize(ListWidgetMetrics.SIZE)

        self.setStyleSheet(self.load_stylesheet("list_widget.qss"))
        self.setup_ui()

    def setup_ui(self):
        self.setItemDelegate(CustomDelegate())


    @staticmethod
    def load_stylesheet(name):
        QssLoader.load_qss(name)
        return name

    def set_data(self, data_model: FileModel) -> None:
        item = QListWidgetItem(self)
        item.setData(Qt.ItemDataRole.UserRole, data_model.file_name)
        item.setData(Qt.ItemDataRole.UserRole + 1, data_model.file_path)
        if data_model.file_name:
            icon_name = ("pdf.png" if data_model.file_name.lower().endswith(".pdf") else "doc.png")
            item.setData(Qt.ItemDataRole.UserRole + 2, IconMaker.icon(icon_name))

        item.setData(Qt.ItemDataRole.UserRole + 3, data_model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ListWidget()
    window.show()
    sys.exit(app.exec())