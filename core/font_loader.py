from pathlib import Path
from PySide6.QtGui import QFont, QFontDatabase
from PersianPad.shared.fonts import Fonts

class FontLoader:
    def __init__(self):
        pass

    def get_font_path(self, font_name: str) -> Path:
        """
        this method is used to get the font_name path from specific folder and return its path
        :param font_name:
        """
        if not (font_name.endswith('.ttf') or not font_name.endswith('.otf')):
            raise Exception(f'Font name {font_name} not supported it must end with .ttf or .otf')

        DIR_PATH = Path(__file__).resolve().parent.parent / "resources" / "fonts"
        path = DIR_PATH / font_name

        if not path.exists():
            raise Exception(f'{font_name} not exist please add it to resources\fonts folder')
        return path

    def load_font(self, font_name: str, size: int = 8) -> QFont:
        """
        this method will use for returning the fonts as QFont object
        :param font_name:
        :param size:
        """
        font_path = self.get_font_path(font_name)
        font_id = QFontDatabase.addApplicationFont(str(font_path))
        if font_id == -1:
            raise Exception(f"Font loading failed")

        families = QFontDatabase.applicationFontFamilies(font_id)
        font_family = families[0]

        font = QFont(font_family, size)
        return font

