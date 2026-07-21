
from PySide6.QtGui import QTextCharFormat, QFont
from pathlib import Path
from app.models.font_Item import FontItem
from app.services.font_loader import FontLoader



class TextFormatModel:

    def toggle_bold(self, editor):
        format = editor.currentCharFormat()

        if format.fontWeight() == 700:
            format.setFontWeight(400)
        else:
            format.setFontWeight(700)

        editor.mergeCurrentCharFormat(format)

    def toggle_italic(self, editor):
        format = editor.currentCharFormat()

        format.setFontItalic(not format.fontItalic())

        editor.mergeCurrentCharFormat(format)

    def toggle_underLine(self, editor):
        format = editor.currentCharFormat()

        format.setFontUnderline(not format.fontUnderline())

        editor.mergeCurrentCharFormat(format)


class FontFormatModel:
    def __init__(self):
        
        self.font_loader = FontLoader()
        BASE_DIR = Path(__file__).resolve().parents[2]
        base_path = BASE_DIR / "app" / "resources" / "fonts"

        self.fonts = [FontItem(title="نازنین"  , path=base_path / "nazanin.ttf"),
                      FontItem(title="وزیر"    , path=base_path / "Vazir.ttf"),
                      FontItem(title="میترا"   , path=base_path / "mitra.ttf"),
                      FontItem(title="لالزار"   , path=base_path / "lalezar.ttf"),
                      FontItem(title="اردیبهشت", path=base_path / "ordibehesht.ttf"),
                      FontItem(title="رضوان"   , path=base_path / "rezvan.ttf"),
                      FontItem(title="رویا"    , path=base_path / "roya.ttf"),
                      FontItem(title="یاقوت"   , path=base_path / "yagut.ttf"),
                      FontItem(title="یکان"    , path=base_path / "Yekan.ttf"),
                      FontItem(title="بسم الله", path=base_path / "Besmellah.ttf"),
                      FontItem(title="بچه دزد" , path=base_path / "kidnap.ttf"),
                      FontItem(title="کلاسیک"   , path=base_path / "classic.ttf"),
                      FontItem(title="حدیث"    , path=base_path / "ZARGHAN HADITH.ttf"),
                      FontItem(title="خط خطی"  , path=base_path / "khat-khati.ttf"),
                      FontItem(title="نستعلق"  , path=base_path / "IranNastaliq.ttf"),
                      FontItem(title="کرشمه"   , path=base_path / "persian-kereshmeh.ttf"),]
        
        self._load_fonts()
        
    def _load_fonts(self):
        loaded_fonts = []
        for font in self.fonts:
            loaded_font = self.font_loader.load_font(font_item=font)
            if loaded_font.family:
                loaded_fonts.append(loaded_font)

        self.fonts = loaded_fonts

    def get_fonts(self):
        return self.fonts
    
    
    def built_font(self, family: str | None = None, size: int | None = None, base_font: QFont | None = None) -> QFont:
        if base_font is not None:
            font = QFont(base_font)
        else:
            font = QFont()

        if family:
            font.setFamily(family)
        if size:
            font.setPointSize(size)
        return font


    def change_font_family(self, editor, family):
        format = editor.currentCharFormat()
        format.setFontFamily(family)
        editor.mergeCurrentCharFormat(format)

    def change_font_size(self, editor, size):
        format = editor.currentCharFormat()
        format.setFontPointSize(size)
        editor.mergeCurrentCharFormat(format)

    
