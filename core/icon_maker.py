from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize, Qt
from PersianPad.core.path_handler import PathHandler


class IconMaker:
    DEFAULT_SIZE: QSize = QSize(24, 24)

    @classmethod
    def icon(cls, name: str, size: QSize | None = None) -> QPixmap:
        if not name:
            raise ValueError("No icon name provided")

        valid_ext = (".png", ".svg", ".ico", ".jpg", ".jpeg")
        if not name.lower().endswith(valid_ext):
            raise ValueError(f"Invalid icon format: {name}")

        pixmap = QPixmap(PathHandler.icon(name))
        if pixmap.isNull():
            raise FileNotFoundError(f"Icon file not found: {name}")

        if size is None:
            size = cls.DEFAULT_SIZE

        scaled_pixmap = pixmap.scaled(size,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation)
        return scaled_pixmap
