from dataclasses import dataclass
from PySide6.QtGui import QColor


@dataclass
class MainWindowColors:
    pass


@dataclass
class NavigationBarColors:
    BACKGROUND_COLOR: QColor = QColor("#F8FAFC")
    BORDER: QColor = QColor("transparent")

    BACKGROUND_COLOR_BTN: QColor = BACKGROUND_COLOR
    TEXT_COLOR_PRIMARY: QColor = QColor("#000000")
    TEXT_COLOR_SECONDARY: QColor = QColor("#FFFFFF")
    SELECTED_BTN: QColor = QColor("#DBEAFE")
    HOVER: QColor = QColor("#F3F4F6")

    # SETTING BUTTON
    SETTING_BACKGROUND: QColor = QColor("transparent")
    SETTING_BORDER: QColor = QColor("transparent")
    SETTING_HOVER: QColor = QColor("#F3F4F6")
    SETTING_PRESSED: QColor = QColor("#E5E7E8")