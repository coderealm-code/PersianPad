from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QFrame, QGroupBox, QVBoxLayout, QWidget, QApplication
from UI.edit_widget.FilePage.FileManager.model import FileModel
from shared.metrics import LabelInfoMetrics
from UI.edit_widget.FilePage.FilesList.file_list import FilesList


class InfoLabel(QFrame):
    def __init__(self, file_list: FilesList, parent: QWidget | None = None):
        super().__init__(parent)
        self.file_list: QWidget = file_list
        self.setObjectName("InfoLabel")
        self.setFixedSize(LabelInfoMetrics.SIZE)

        main_layout: QVBoxLayout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        group_box: QGroupBox = QGroupBox("اطلاعات سند")
        group_layout: QVBoxLayout = QVBoxLayout(group_box)
        group_box.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        group_layout.setContentsMargins(5, 0, 5, 0)
        group_layout.setSpacing(10)

        self.info_lbl = QLabel()
        self.info_lbl.setStyleSheet("QLabel { padding: 5px; font-size: 14px; }")
        group_layout.addWidget(self.info_lbl)

        main_layout.addWidget(group_box)
        self.setLayout(main_layout)
        self.file_list.list_widget.itemClicked.connect(self.model_info)
        self.set_text(None)


    def set_text(self, model: FileModel | None) -> None:
        if model is None:
            name = "---"
            path = "---"
            created_date = "---"
        else:
            name = model.file_name
            path = model.file_path
            created_date = model.create_date

        self.info_lbl.setText(
            f"""
اسم فایل : {name}

مسیر فایل : {path}

تاریخ ایجاد : {created_date}
""")

    def model_info(self, item) -> None:
        model = item.data(Qt.ItemDataRole.UserRole + 3)
        if isinstance(model, FileModel):
            self.set_text(model)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    editor = InfoLabel()
    editor.show()
    sys.exit(app.exec())