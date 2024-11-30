import sys
from random import randrange

from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow
from UI import Ui_MainWindow

class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw(self, qp):
        for i in range(randrange(1, 10)):
            qp.setBrush(QColor(randrange(0, 255), randrange(0, 255), randrange(0, 255)))
            diametr = randrange(1, 100)
            cor = (randrange(1, 700), randrange(1, 600), diametr, diametr)
            qp.drawEllipse(*cor)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())