from dataclasses import dataclass

@dataclass
class Fonts:
    DEFAULT_FONT_NAME: str = "Vazir.ttf"
    FONT_VAZIR: str = "Vazir.ttf"
    FONT_CLASSIC: str = "classic.ttf"
    FONT_BESMELLAH: str = "Besmellah.ttf"
    FONT_IRANNASTALIQ: str = "IranNastaliq.ttf"
    FONT_FARKHODKAR: str = "Far_khodkar.ttf"
    FONT_KHAT_KHATI: str = "khat-khati.ttf"
    FONT_KIDNAP: str = "kidnapp.ttf"
    FONT_LALEZR: str = "lalezar.ttf"
    FONT_MITRA: str = "mitra.ttf"
    FONT_NAZANIN: str = "nazanin.ttf"
    FONT_ORDIBEHESHT: str = "ordibehesht.ttf"
    FONT_KARESHME: str = "persian-kereshmeh.ttf"
    FONT_REZVAN: str = "rezvan.ttf"
    FONT_ROYA: str = "roya.ttf"
    FONT_YAGUT: str = "yagut.ttf"
    FONT_YEKAN: str = "Yekan.ttf"
    FONT_HADITH: str = "ZARGHAN HADITH.ttf"

    def __iter__(self):
        yield self.DEFAULT_FONT_NAME
        yield self.FONT_VAZIR
        yield self.FONT_CLASSIC
        yield self.FONT_BESMELLAH
        yield self.FONT_IRANNASTALIQ
        yield self.FONT_FARKHODKAR
        yield self.FONT_KHAT_KHATI
        yield self.FONT_KIDNAP
        yield self.FONT_LALEZR
        yield self.FONT_MITRA
        yield self.FONT_NAZANIN
        yield self.FONT_ORDIBEHESHT
        yield self.FONT_KARESHME
        yield self.FONT_REZVAN
        yield self.FONT_YAGUT
        yield self.FONT_YEKAN
        yield self.FONT_HADITH