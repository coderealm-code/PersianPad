from dataclasses import dataclass

#-----------------------------
# General Metrics / Constants
#-----------------------------

@dataclass
class MainWindowMetrics:
    """Metrics for the main window"""

    width: int = 1280
    height: int = 720

    padx: int = 20
    pady: int = 15


@dataclass
class NavigationPanelMetrics:
    """Metrics for the navigation bar"""

    height: int = 50
    width: int = MainWindowMetrics.width

    btn_width: int = 50
    btn_height: int = 50


@dataclass
class HomeWidgetMetrics:
    """Metrics for the home widget"""

    width: int = MainWindowMetrics.width
    height: int = 150

    btn_width: int = 100
    btn_height: int = 100

    lbl_height: int = height
    lbl_width: int = 50


@dataclass
class EditWidgetMetrics:
    """Metrics for the edit widget"""

    width: int = MainWindowMetrics.width
    height: int = 150

    lbl_height: int = height
    lbl_width: int = 50

    # first part
    f_btn_width: int = 65
    f_btn_height: int = 100

    # second part
    s_cbx_width : int = 180
    s_cbx_height: int = 35

    s_btn_width : int = 60
    s_btn_height: int = 50

    # third part
    t_btn_width : int = 100
    t_btn_height: int = 30

    t_entry_width : int = 120
    t_entry_height: int = 35

    # fourth part
    fo_btn_width : int = 60
    fo_btn_height: int = 50

@dataclass
class ShowWidgetMetrics:
    """Metrics for the edit widget"""

    width: int = MainWindowMetrics.width
    height: int = 150

    lbl_height: int = height
    lbl_width: int = 50

    btn_width : int = 40
    btn_height: int = 40

@dataclass
class HelpWidgetMetrics:
    """Metrics for the edit widget"""

    width: int = MainWindowMetrics.width
    height: int = 150

    lbl_height: int = height
    lbl_width: int = 50
    

@dataclass
class TextPlaceMetrics:
    width : int = MainWindowMetrics.width - 2*MainWindowMetrics.padx
    height: int = 500

    