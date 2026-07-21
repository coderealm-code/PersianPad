from PySide6.QtGui import QFontDatabase
from app.models.font_Item import FontItem


class FontLoader:

    def load_font(self, font_item: FontItem) -> FontItem:
        font_id = QFontDatabase.addApplicationFont(str(font_item.path))

        if font_id == -1:
            return font_item
        
        families = QFontDatabase.applicationFontFamilies(font_id)
        if families:
            font_item.family = families[0]

        return font_item