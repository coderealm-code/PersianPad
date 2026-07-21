import os 
from dataclasses import dataclass
from PySide6.QtWidgets import QFileDialog, QMessageBox
from app.widgets.text_place_widget import TextEdit
from app.widgets.pages.home_widget import HomeWidget


@dataclass
class FileModel:    
    file_path: str = None
    is_saved: bool = False 


class FileController:
    def __init__(self, model: FileModel, editor: TextEdit, widget: HomeWidget):
        self.model = model
        self.editor = editor
        self.widget = widget

        self.widget.request_new_file.connect(self.new_file)
        self.widget.request_open_file.connect(self.open_file)
        self.widget.request_save_as.connect(self.save_as)
        self.widget.request_save_file.connect(self.save_file)

        self.editor.textChanged.connect(self.mark_unsave)

    def mark_unsave(self):
        self.model.is_saved = False

    def open_file(self):
        if not self.model.is_saved:
            reply = QMessageBox.question(None, "هشدار", "تغییرات ذخیره نشده‌اند. آیا می‌خواهید ذخیره کنید؟",
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            
            if reply == QMessageBox.Yes:
                self.save_file()
            elif reply == QMessageBox.No:
                pass
            elif reply == QMessageBox.Cancel:
                return None
            
        file_path, _ = QFileDialog.getOpenFileName(None, "انتخاب فایل", "", "Text Files (*.txt)")
        if not file_path:
            return None
            
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        self.editor.setPlainText(text)

        self.widget.add_to_recent_files(file_path)

        self.model.file_path = file_path
        self.model.is_saved = True
        return None



    def save_file(self) -> None:
        if self.model.file_path is None:
            self.save_as()
            return None
        
        with open(self.model.file_path, "w", encoding="utf-8") as file:
            file.write(self.editor.toPlainText())

        self.model.is_saved = True
        return None


    def save_as(self) -> None:
        file_path, _ = QFileDialog.getSaveFileName(None, "ذخیره فایل", "", "Text Files (*.txt)")
        if not file_path:
            return None
        
        if not file_path.lower().endswith(".txt"):
            file_path += ".txt"
        
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(self.editor.toPlainText())

        self.widget.add_to_recent_files(file_path)

        self.model.file_path = file_path
        self.model.is_saved = True
        return None


    def new_file(self):
        if not self.model.is_saved:
            reply = QMessageBox.question(None, "هشدار", "تغییرات ذخیره نشده‌اند. آیا می‌خواهید ذخیره کنید؟",
                 QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            
            if reply == QMessageBox.Yes:
                self.save_file()
                
            if reply == QMessageBox.Cancel:
                return None
            
        self.editor.clear()

        self.model.file_path = None
        self.model.is_saved = True
            
