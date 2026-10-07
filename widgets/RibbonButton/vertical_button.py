import sys
from PySide6.QtWidgets import QWidget, QApplication, QStyle
from PySide6.QtCore import Qt, QSize, QRect, Signal
from PySide6.QtGui import QPixmap, QPainter, QFont, QColor, QMouseEvent
from core.font_loader import FontLoader
from shared.fonts import Fonts
from core.path_handler import PathHandler
from widgets.RibbonButton.metrics import RibbonButtonMetrics

class VerticalButton(QWidget):
    clicked = Signal()
    def __init__(self, text: str, icon_name: str, font_name: str, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.setMinimumSize(RibbonButtonMetrics.width, RibbonButtonMetrics.height)

        self.font_loader: FontLoader = FontLoader()
        self.text: str = text
        self.font: QFont = self.font_loader.load_font(font_name)
        self.pixmap: QPixmap = QPixmap(PathHandler.icon(icon_name))
        self.scaled_pixmap: QPixmap = self.pixmap.scaled(QSize(32, 32),
                                                         Qt.AspectRatioMode.KeepAspectRatio,
                                                         Qt.TransformationMode.SmoothTransformation)

        #-------- states -------------
        self._hover: bool = False
        self._pressed: bool = False
        self._active: bool = False
        self._setActivation: bool = False

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform, True)
        painter.setRenderHint(QPainter.RenderHint.TextAntialiasing, True)
        #----------- BackGround ----------------
        button_area = QRect(0, 10, self.width(), self.height() - 10)
        if self._pressed:
            color = QColor("#ebebeb")
        elif self._hover:
            color = QColor("#e0e0e0")
        else:
            color = QColor("transparent")
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(color)
        painter.drawRoundedRect(button_area, RibbonButtonMetrics.size_10, RibbonButtonMetrics.size_10)

        #----------- set Icon --------------
        painter.setPen(QColor("#ffcccc"))
        painter.setBrush(Qt.BrushStyle.NoBrush)
        pixmap_rect = QStyle.alignedRect(Qt.LayoutDirection.LeftToRight,
                                         Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop,
                                         self.scaled_pixmap.size(), button_area)
        painter.drawPixmap(pixmap_rect.topLeft(), self.scaled_pixmap)

        #------------- set Text ------------------
        text_area = QRect(0, pixmap_rect.bottom() + 10, self.width(), RibbonButtonMetrics.size_24)
        painter.setFont(self.font)
        painter.setPen(QColor("black"))
        painter.drawText(text_area, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter, self.text)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            if self._setActivation:
                self._active = not self._active
                self._pressed = True
            else:
                self._pressed = True
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if self.rect().contains(event.pos()):
                self.clicked.emit()
            if self._active:
                self._pressed = True
            else:
                self._pressed = False
            self.update()


    def enterEvent(self, event: QMouseEvent):
        self._hover = True
        self.update()

    def leaveEvent(self, event: QMouseEvent):
        self._hover = False
        if self._active:
            self._pressed = True
        else:
            self._pressed = False
        self.update()

    def setActive(self, active: bool=False) -> None:
        if not isinstance(active, bool):
            raise TypeError("active must be bool")
        self._setActivation = active
        return None



if __name__ == '__main__':
    app = QApplication(sys.argv)
    font = Fonts.FONT_VAZIR
    window = VerticalButton(icon_name="copy.png", text="copy", font_name=Fonts.FONT_VAZIR)
    window.show()
    sys.exit(app.exec())