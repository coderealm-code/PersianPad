from datetime import datetime
from pathlib import Path
from PySide6.QtWidgets import QFileDialog, QTextEdit, QMessageBox
from UI.edit_widget.FilePage.FileManager.model import FileModel
from core.path_handler import PathHandler
from PySide6.QtPrintSupport import QPrinter


class FileService:
    ALLOWED_EXTENSIONS: set = {".txt", ".pdf"}

    def __init__(self, model: FileModel, editor: QTextEdit) -> None:
        self.editor = editor
        self.model = model
        self.models_list: list[FileModel] = []

        self.editor.textChanged.connect(self.mark_unsaved)

    def check_file_allowed(self, path: str) -> bool:
        ext = Path(path).suffix.lower().strip()
        if ext not in self.ALLOWED_EXTENSIONS:
            return False
        return True

    def mark_unsaved(self) -> None:
        """if editor changes the file will mark unsave"""
        self.model.is_saved = False
        return None

    def new_file(self) -> None:
        """this makes a new file"""
        if not (self.editor.document().isEmpty()):
            if not self.model.is_saved:
                reply = QMessageBox.question(None, "هشدار", "تغییرات ذخیره نشده‌اند. آیا می‌خواهید ذخیره کنید؟",
                                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                if reply == QMessageBox.StandardButton.Yes:
                    self.save_file()
                elif reply == QMessageBox.StandardButton.No:
                    return None

        self.editor.clear()
        self.model.file_name = None
        self.model.is_saved = True
        self.model.file_path = None
        self.model.create_date = None
        return None


    def open_file(self) -> None:
        """this open a file from your computer"""
        if not (self.editor.document().isEmpty()):
            if not self.model.is_saved:
                reply = QMessageBox.question(None, "هشدار", "تغییرات ذخیره نشده‌اند. آیا می‌خواهید ذخیره کنید؟",
                                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                if reply == QMessageBox.StandardButton.Yes:
                    self.save_file()
                elif reply == QMessageBox.StandardButton.No:
                    return None

        file_path, _ = QFileDialog.getOpenFileName(None, "انتخاب فایل", "", "Text Files (*.txt)")
        if not file_path:
            return None

        file_path = PathHandler.optimized_path(file_path)
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        self.editor.setPlainText(text)
        self.model.file_name = file_path.name
        self.model.is_saved = True
        self.model.file_path = file_path
        self.model.create_date = datetime.now()
        return None


    def save_file(self):
        if self.model.file_path is None:
            self.save_as()
            return None
        with open(self.model.file_path, "w", encoding="utf-8") as file:
            file.write(self.editor.toPlainText())

        self.model.is_saved = True
        return None


    def save_as(self) -> bool:
        file_path, _ = QFileDialog.getSaveFileName(None, "ذخیره فایل", "", "Text Files (*.txt)")
        if not file_path:
            return False
        file_path = PathHandler.optimized_path(file_path)
        if not file_path.name.endswith(".txt"):
            new_path = file_path.with_suffix(".txt")
        else:
            new_path = file_path
        self.write_file(new_path, self.editor.toPlainText())

        self.model.file_name = new_path.name
        self.model.is_saved = True
        self.model.file_path = new_path
        self.model.create_date = datetime.now()
        self.append_list(self.model)
        return True


    def export_pdf(self) -> bool:
        file_path, _ = QFileDialog.getSaveFileName(None, "ذخیره به PDF", "",
                                                   "PDF Files (*.pdf);;All Files (*)")
        if not file_path:
            return False
        new_path = PathHandler.optimized_path(file_path)

        if new_path.suffix != ".pdf":
            new_path = new_path.with_suffix(".pdf")

        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
        printer.setOutputFileName(str(new_path))
        self.editor.document().print_(printer)
        QMessageBox.information(self.editor, "موفق", f"PDF در مسیر {new_path}ذخیره شد ")
        self.model.file_name = new_path.name
        self.model.is_saved = True
        self.model.file_path = new_path
        self.model.create_date = datetime.now()
        self.append_list(self.model)
        return True


    @staticmethod
    def read_file(path: Path) -> str:
        with open(path, "r", encoding="utf-8") as file:
            text = file.read()
        return text


    @staticmethod
    def write_file(path: Path, text: str) -> None:
        with open(path, "w", encoding="utf-8") as file:
            file.write(text)
        return None


    def append_list(self, model: FileModel) -> None:
        the_model = model
        self.models_list.append(the_model)
        return None