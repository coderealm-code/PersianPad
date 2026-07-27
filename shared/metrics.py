from dataclasses import dataclass


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
    height: int = (30 / 100) * MainWindowMetrics.height # 30% OF THE WINDOW = 216 IN HERE


@dataclass
class FileManagerMetrics:
    """Metrics for the file manager"""
    width: int = 576
    height: int = MainWindowMetrics.height

    button_width: int = 80
    button_height: int = 100

    label_height: int = 30
    label_width: int = 576


@dataclass
class TextSettingsMetrics:
    """Metrics for the text setting widget"""
    width: int = MainWindowMetrics.width
    height: int = MainWindowMetrics.height * (30 // 100)


class ClipboardMetrics:
    """Metrics for the clipboard widget"""
    height: int = TextSettingsMetrics.height
    width: int = 200
    btn_width: int = 50
    btn_height: int = 80