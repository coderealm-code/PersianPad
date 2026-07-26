from datetime import datetime
from pathlib import Path
from PySide6.QtWidgets import QFileDialog, QTextEdit, QMessageBox
from PersianPad.UI._edit_widget.FilePage.FileManager.model import Model
from PersianPad.core.path_handler import PathHandler
from PySide6.QtPrintSupport import QPrinter


class FileService:
    ALLOWED_EXTENSIONS: set = {".txt", ".pdf"}
    def __init__(self, editor: QTextEdit):
        self.editor = editor
        self.model = Model()

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
                                             QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
                if reply == QMessageBox.Yes:
                    self.save_file()
                elif reply == QMessageBox.No:
                    return None
                elif reply == QMessageBox.Cancel:
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
                                             QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
                if reply == QMessageBox.Yes:
                    self.save_file()
                elif reply == QMessageBox.No:
                    return None
                elif reply == QMessageBox.Cancel:
                    return None

        file_path, _ = QFileDialog.getOpenFileName(None, "انتخاب فایل", "", "Text Files (*.txt)")
        if not file_path:
            return None

        file_path = PathHandler.optimized_path(file_path)
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        editor.setPlainText(text)
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


    def save_as(self):
        file_path, _ = QFileDialog.getSaveFileName(None, "ذخیره فایل", "", "Text Files (*.txt)")
        if not file_path:
            return None
        file_path = PathHandler.optimized_path(file_path)
        if file_path.name.endswith(".txt"):
            new_path = file_path.with_suffix(".txt")
        with open(new_path, "w", encoding="utf-8") as file:
            file.write(self.editor.toPlainText())

        self.model.file_name = new_path.name
        self.model.is_saved = True
        self.model.file_path = new_path
        self.model.create_date = datetime.now()
        return None


    def export_pdf(self) -> None:
        file_path, _ = QFileDialog.getOpenFileName(None, "ذخیره به PDF", "",
                                                   "PDF Files (*.pdf);;All Files (*)")
        if not file_path:
            return None
        new_path = PathHandler.optimized_path(file_path)

        if new_path.suffix != ".pdf":
            new_path = new_path.with_suffix(".pdf")

        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
        printer.setOutputFileName(new_path)
        self.editor.document().print_(printer)
        QMessageBox.information(self, "موفق", f"PDF در مسیر {new_path}ذخیره شد ")
        return None

    def read_file(self):
        pass

    def write_file(self):
        pass