from dataclasses import dataclass

@dataclass
class RibbonButtonMetrics:
    width: int = 50
    height: int = 75

    padx: int = 10
    pady: int = 7

    size_4: int = 4
    size_6: int = 6
    size_8: int = 8
    size_10: int = 10
    size_12: int = 12
    size_14: int = 14
    size_16: int = 16
    size_20: int = 20
    size_24: int = 24
    size_32: int = 32
    size_48: int = 48