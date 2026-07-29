from dataclasses import dataclass


@dataclass
class SearchDialogMetrics:
    """Metrics for the search dialog"""
    width: int = 420
    height: int = 460
    radius: int = 10


@dataclass
class BodyMetric:
    """Metrics for the title bar"""
    width: int = SearchDialogMetrics.width
    height: int = 48

    line_edit_width: int = 380
    line_edit_height: int = 40

    check_box_height: int = 32
    check_box_width: int = 380

    button_width: int = 100
    button_height: int = 38
    button_radius: int = 8


@dataclass
class Spacer:
    """Metrics for the spacer"""
    space_4: int = 4
    space_6: int = 6
    space_8: int = 8
    space_10: int = 10
    space_12: int = 12
    space_14: int = 14
    space_16: int = 16
    space_18: int = 18
    space_20: int = 20
    space_24: int = 24
    space_26: int = 26
    space_28: int = 28
    space_30: int = 30
    space_32: int = 32
    space_36: int = 36
    space_40: int = 40
    space_48: int = 48