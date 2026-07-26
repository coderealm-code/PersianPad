import sys
from pathlib import Path
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication, QHBoxLayout, QFrame, QGroupBox
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap, QIcon, QMouseEvent


class RecentFileItem(QFrame):
    request_open_file = Signal(str)
    def __init__(self, path: Path, name: str, icon: QPixmap | None = None,  parent=None) -> None:
        super().__init__(parent)
        self.name = name
        self.path = path
        self.setStyleSheet("""QFrame#recentFileItem {
                                                        background-color: transparent;
                                                        border: none;
                                                        border-radius: 10px;
                                                        padding: 20 5px;
                                                    }""")
        self.setMinimumSize(250, 30)

        self.setObjectName("recentFileItem")
        self.setLayoutDirection(Qt.RightToLeft)
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(10)

        path_lbl: QLabel = QLabel(str(self.path))
        name_lbl: QLabel = QLabel(self.name)
        icon_lbl: QLabel = QLabel()
        if icon:
            icon_lbl.setPixmap(icon)

        main_layout.addWidget(name_lbl)
        main_layout.addWidget(icon_lbl)
        main_layout.addStretch()
        main_layout.addWidget(path_lbl)
        self.setLayout(main_layout)


    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        pos = event.position().toPoint()
        if event.button() == Qt.MouseButton.LeftButton:
            print(f"left click in {pos.x()}, {pos.y()}")
            self.request_open_file.emit(str(self.path))
        super().mousePressEvent(event)
        return None


    def enterEvent(self, event: QMouseEvent) -> None:
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setStyleSheet("""QFrame#recentFileItem {
                                                    background-color: #b8b8b8;
                                                    border: none;
                                                    border-radius: 10px;
                                                    padding: 20 5px;
                                                     }""")
        super().enterEvent(event)
        return None

    def leaveEvent(self, event: QMouseEvent) -> None:
        self.setCursor(Qt.CursorShape.ArrowCursor)
        self.setStyleSheet("""QFrame#recentFileItem {
                                                            background-color: transparent;
                                                            border: none;
                                                            border-radius: 10px;
                                                            padding: 20 5px;
                                                             }""")
        super().leaveEvent(event)
        return None



class RecentFilesContainer(QFrame):
    request_clear_json = Signal()
    def __init__(self, parent=None, *list_item: RecentFileItem):
        super().__init__(parent)
        self.setLayoutDirection(Qt.RightToLeft)
        self.setStyleSheet("""QFrame {border: 1px solid #bdbdbd; border-radius: 10px;}
                               QLabel {border: none;}""")
        self.setMinimumSize(300, 150)

        self.list_item = list(list_item)
        self.container_layout = QVBoxLayout()
        self.container_layout.setContentsMargins(10, 5, 10, 5)
        self.container_layout.setSpacing(5)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)

        for i, item in enumerate(self.list_item):
            self.container_layout.addWidget(item)

            if i != len(self.list_item) - 1:
                line = QFrame()
                line.setFrameShape(QFrame.HLine)
                self.container_layout.addWidget(line)

        self.setLayout(self.container_layout)

    def clear_item(self) -> None:
        while self.container_layout.count():
            child = self.container_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.list_item = []
        self.request_clear_json.emit()
        return None


class RecentFilesWidget(QWidget):
    def __init__(self, list_container: RecentFilesContainer, parent=None):
        super().__init__(parent)
        self.setLayoutDirection(Qt.RightToLeft)
        self.setAutoFillBackground(True)

        main_layout = QVBoxLayout()

        self.group = QGroupBox("فایل های اخیر")
        self.group.setLayoutDirection(Qt.RightToLeft)
        self.group.setStyleSheet("""QGroupBox {
                                                    border: 1px solid #bdbdbd;
                                                    color: #000000;
                                                    border-radius: 8px;
                                                    margin-top: 12px;
                                                }
                                                
                                                QGroupBox::title {
                                                    subcontrol-origin: margin;
                                                    left: 15px;
                                                    padding: 0 5px;
                                                }""")
        group_layout = QVBoxLayout()
        group_layout.setContentsMargins(15, 10, 15, 10)
        group_layout.addWidget(list_container)
        self.group.setLayout(group_layout)

        main_layout.addWidget(self.group)
        self.setLayout(main_layout)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    item1 = RecentFileItem(
        "C:/Users/Asus/Documents",
        "یادداشت.txt"
    )
    item2 = RecentFileItem(
        "C:/Users/Asus/Documents",
        "یادداشت.txt"
    )
    item3 = RecentFileItem(
        "C:/Users/Asus/Documents",
        "یادداشت.txt"
    )
    container = RecentFilesContainer(None, item1, item2, item3)
    window = RecentFilesWidget(container)
    window.show()
    sys.exit(app.exec())