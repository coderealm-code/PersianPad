from dataclasses import dataclass
from PySide6.QtCore import QSize


@dataclass
class MainWindowMetrics:
    """Metrics for the main window"""
    width: int = 1280
    height: int = 720

    padx: int = 20
    pady: int = 15


@dataclass
class NavigationBarMetrics:
    """Metrics for the navigation bar"""
    height: int = 40
    width: int = MainWindowMetrics.width

    btn_width: int = 100
    btn_height: int = height


@dataclass
class ContainerWidgetMetrics:
    """Metrics for the container widget"""
    width: int = MainWindowMetrics.width
    height: int = 0.2 * MainWindowMetrics.height # 30% OF THE WINDOW = 216 IN HERE


@dataclass
class FileManagerMetrics:
    """Metrics for the file manager"""
    width: int = 576
    height: int = MainWindowMetrics.height

    button_width: int = 80
    button_height: int = 100

    label_height: int = 30
    label_width: int = 576

#==============================================
@dataclass
class TextSettingsMetrics:
    """Metrics for the text setting widget"""
    size: QSize = QSize(MainWindowMetrics.width, int(MainWindowMetrics.height * 0.2))
    height: int = MainWindowMetrics.height * 0.2



class ClipboardMetrics:
    """Metrics for the clipboard widget"""
    height: int = TextSettingsMetrics.height
    width: int = 160
    btn_width: int = 45
    btn_height: int = 75


@dataclass
class FindReplaceMetrics:
    """Metrics for the find replace widget"""
    height: int = TextSettingsMetrics.height
    width: int = 150
    btn_width: int = 45
    btn_height: int = 75


@dataclass
class TextJustifyMetrics:
    """Metrics for the text justify widget"""
    size: QSize = QSize(280, TextSettingsMetrics.height)
    btn_size: QSize = QSize(45, 75)


@dataclass
class FontSettingMetrics:
    """Metrics for the text font setting widget"""
    size: QSize = QSize(280, TextSettingsMetrics.height)
    btn_size: QSize = QSize(45, 75)


@dataclass
class FontShapeMetrics:
    """Metrics for the text font shape widget"""
    size: QSize = QSize(210, TextSettingsMetrics.height)
    combo_box_size: QSize = QSize(200, 40)

#==================================================================
@dataclass
class EditorMetrics:
    """Metrics for the edit widget"""
    A3: QSize = QSize(297, 420)
    A4: QSize = QSize(210, 297)
    A5: QSize = QSize(148, 210)