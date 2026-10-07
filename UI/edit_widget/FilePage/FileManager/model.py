from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional


@dataclass
class FileModel:
    file_name: Optional[str] = None
    file_path: Optional[Path] = None
    create_date: Optional[datetime] = None
    is_saved: bool = True