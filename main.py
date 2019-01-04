import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtCore import Qt
from area_selector import AreaSelector

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
