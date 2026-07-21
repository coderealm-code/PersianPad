from dataclasses import dataclass
from pathlib import Path

@dataclass
class FontItem:
    title: str 
    path : Path
    family: str = ""