from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass
class FileModel:
    file_name: str = None
    file_path: Path = None
    create_date: datetime = None
    is_saved: bool = True