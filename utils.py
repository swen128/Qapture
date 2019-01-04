from PyQt5.QtCore import QRect, QPoint

def point_min(point1, point2):
    x = min(point1.x(), point2.x())
    y = min(point1.y(), point2.y())
    return QPoint(x, y)

def point_max(point1, point2):
    x = max(point1.x(), point2.x())
    y = max(point1.y(), point2.y())
    return QPoint(x, y)

def q_rect(point1, point2):
    top_left = point_min(point1, point2)
    bottom_right = point_max(point1, point2)
    return QRect(top_left, bottom_right)    