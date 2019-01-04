import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRubberBand
from PyQt5.QtGui import QPixmap, QGuiApplication, QPalette, QColor, QPainter
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

    def set_geometry(self, top_left, bottom_right):
        rect = QRect(top_left, bottom_right)
        self.rubberBand.setGeometry(rect)

    def set_bottom_right(self, bottom_right):
        top_left = self.origin
        self.set_geometry(top_left, bottom_right)

    def mousePressEvent(self, event):
        self.origin = event.pos()
        self.set_geometry(self.origin, self.origin)
        self.rubberBand.show()

    def mouseMoveEvent(self, event):
        pos = event.pos()
        self.set_bottom_right(pos)

    def mouseReleaseEvent(self, event):
        rect = self.rubberBand.geometry()
        self.close()
        self.signal.emit(rect)


class Qapture(QLabel):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

    def display_ss(self, rect):
        pixmap = screen_shot(rect)
        self.setPixmap(pixmap)
        self.setGeometry(rect)
        self.show()


def screen_shot(rect):
    screen = QGuiApplication.primaryScreen()
    desktop = QApplication.desktop().winId()
    x, y, width, height = rect.getRect()
    img = screen.grabWindow(desktop, x, y, width, height)
    return img


if __name__ == "__main__":
    app = QApplication(sys.argv)
    qapture = Qapture()
    selector = AreaSelector()
    selector.exec(callback = qapture.display_ss)
    sys.exit(app.exec_())
