from PyQt5.QtWidgets import QWidget, QRubberBand
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtCore import Qt, QRect, pyqtSignal

class AreaSelector(QWidget):
    areaSelected = pyqtSignal(['QRect'])

    def __init__(self):
        super().__init__()
        self.rubberBand = QRubberBand(QRubberBand.Rectangle, parent = self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowState(Qt.WindowFullScreen)
        self.setCursor(Qt.CrossCursor)

    def exec(self, callback):
        self.areaSelected.connect(callback)
        self.show()

    def paintEvent(self, event):
        p = QPainter(self)
        p.fillRect(self.rect(), QColor(0, 0, 0, 1))

    def mousePressEvent(self, event):
        self.origin = event.pos()
        self.rubberBand.show()

    def mouseMoveEvent(self, event):
        rect = QRect(self.origin, event.pos())
        self.rubberBand.setGeometry(rect)

    def mouseReleaseEvent(self, event):
        rect = self.rubberBand.geometry()
        self.close()
        self.areaSelected.emit(rect)