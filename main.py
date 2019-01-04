import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRubberBand
from PyQt5.QtGui import QPixmap, QGuiApplication
from PyQt5 import QtCore

class App(QWidget):
    def __init__(self):
        super().__init__()
        shape = QRubberBand.Rectangle
        parent = self
        self.rubberBand = QRubberBand(shape, parent)
        self.setWindowOpacity(0.01)
        self.showFullScreen()

    def get_geometry(self):
        return self.rubberBand.geometry()

    def set_geometry(self, top_left, bottom_right):
        rect = QtCore.QRect(top_left, bottom_right)
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
        rect = self.get_geometry()
        self.rubberBand.hide()
        self.close()
        self.window = ss(rect)
        self.window.show()


def take_ss(rect):
    screen = QGuiApplication.primaryScreen()
    desktop = QApplication.desktop().winId()
    x, y, width, height = rect.getRect()
    img = screen.grabWindow(desktop, x, y, width, height)
    return img

def ss_window(pixmap):
    label = QLabel()
    label.setPixmap(pixmap)
    label.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    return label

def ss(rect):
    pixmap = take_ss(rect)
    label = ss_window(pixmap)
    label.move(rect.topLeft())
    return label

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
