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
class FileManagerMetrics:
    """Metrics for the file manager"""
    width: int = 500
    height: int = 30 / MainWindowMetrics.height*100
    button_width: int = 80
    button_height: int = 100

    label_height: int = 30
