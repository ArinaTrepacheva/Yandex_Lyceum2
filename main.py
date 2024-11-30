import sys
from random import randrange
import io

from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>767</width>
    <height>644</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>230</x>
      <y>20</y>
      <width>251</width>
      <height>61</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font-size: 25px;
background-color: rgb(255, 252, 228);
border-radius:20px;</string>
    </property>
    <property name="text">
     <string>Нажать </string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>767</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

class Design(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.init_ui(parent)

    def init_ui(self, parent):
        f = io.StringIO(template)
        uic.loadUi(f, parent)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        design = Design(self)
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