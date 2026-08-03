import sys
from PySide6.QtWidgets import QFrame, QVBoxLayout, QGroupBox, QApplication, QComboBox
from PySide6.QtCore import Qt, Signal
from PersianPad.shared.fonts import Fonts
from PersianPad.shared.metrics import FontShapeMetrics


class FontShape(QFrame):
    request_font_family: Signal = Signal(str)
    request_font_size: Signal = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.setMinimumWidth(FontShapeMetrics.size.width())
        self.setFixedHeight(FontShapeMetrics.size.height())

        main_layout: QVBoxLayout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        groupBox: QGroupBox = QGroupBox("فونت")
        group_layout: QVBoxLayout = QVBoxLayout(groupBox)
        groupBox.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        group_layout.setContentsMargins(5, 0, 5, 0)
        group_layout.setSpacing(10)

        self.font_cbx: QComboBox = QComboBox()
        self.font_cbx.setFixedSize(FontShapeMetrics.combo_box_size)
        for item in range(len(self._font_list())):
            self.font_cbx.addItem(self._font_list()[item][0], self._font_list()[item][1])
        self.font_cbx.currentIndexChanged.connect(self._emit_font_family)

        self.size_cbx: QComboBox = QComboBox()
        self.size_cbx.setFixedSize(int(FontShapeMetrics.combo_box_size.width()*0.4), FontShapeMetrics.combo_box_size.height())
        for item in self._font_size():
            self.size_cbx.addItem(str(item), item)
        self.size_cbx.setCurrentText("12")
        self.size_cbx.currentIndexChanged.connect(self._emit_font_size)

        group_layout.addStretch()
        group_layout.addWidget(self.font_cbx)
        group_layout.addWidget(self.size_cbx)
        group_layout.addStretch()

        main_layout.addWidget(groupBox)


    @staticmethod
    def _font_list() -> list[tuple]:
        return [("وزیر", Fonts.FONT_VAZIR),
                ("نازنین", Fonts.FONT_NAZANIN),
                ("میترا", Fonts.FONT_MITRA),
                ("کلاسیک", Fonts.FONT_CLASSIC),
                ("رویا", Fonts.FONT_ROYA),
                ("رضوان", Fonts.FONT_REZVAN),
                ("لالزار", Fonts.FONT_LALEZR),
                ("بسم الله", Fonts.FONT_BESMELLAH),
                ("فرخودکر", Fonts.FONT_FARKHODKAR),
                ("ایران نستعلیق", Fonts.FONT_IRANNASTALIQ),
                ("خط خطی", Fonts.FONT_KHAT_KHATI),
                ("بچه دزد", Fonts.FONT_KIDNAP),
                ("اردیبهشت", Fonts.FONT_ORDIBEHESHT),
                ("کرشمه", Fonts.FONT_KARESHME),
                ("یاقوت", Fonts.FONT_YAGUT),
                ("یکان", Fonts.FONT_YEKAN),
                ("حدیث", Fonts.FONT_HADITH),
                ]


    @staticmethod
    def _font_size() -> list[int]:
        return [4, 6, 8, 9, 10, 11, 12, 14, 16, 18, 20, 24, 28, 32, 36, 48, 72]


    def _emit_font_family(self) -> None:
        font_family: str = self.font_cbx.currentData()
        if font_family:
            self.request_font_family.emit(font_family)
        return None


    def _emit_font_size(self) -> None:
        font_size: int = self.size_cbx.currentData()
        if font_size:
            self.request_font_size.emit(font_size)
        return None




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FontShape()
    window.show()
    sys.exit(app.exec())