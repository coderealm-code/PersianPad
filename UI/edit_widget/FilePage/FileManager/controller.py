from PySide6.QtWidgets import QTextEdit
from UI.edit_widget.FilePage.FileManager.service import FileService
from UI.edit_widget.FilePage.FileManager.file_manager import FileManager
from UI.edit_widget.FilePage.FilesList.file_list import FilesList


class FileController:
    def __init__(self, file_list: FilesList, editor: QTextEdit, widget: FileManager, service: FileService) -> None:
        self.widget: FileManager = widget
        self.editor: QTextEdit = editor
        self.service: FileService = service
        self.file_list: FilesList = file_list
        self._connect_signals()


    def _connect_signals(self) -> None:
        self.widget.request_new_file.connect(self.new_file)
        self.widget.request_export_pdf.connect(self.export_pdf)
        self.widget.request_open_file.connect(self.open_file)
        self.widget.request_save_file.connect(self.save_file)
        self.widget.request_save_as_file.connect(self.save_as)



    def open_file(self) -> None:
        self.service.open_file()


    def save_file(self) -> None:
        self.service.save_file()

    def save_as(self) -> None:
        if self.service.save_as():
            self.file_list.add_file(self.service.model)


    def new_file(self) -> None:
        self.service.new_file()


    def export_pdf(self) -> None:
        if self.service.export_pdf():
            self.file_list.add_file(self.service.model)



