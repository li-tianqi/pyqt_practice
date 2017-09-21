#!/usr/bin/env python3
# coding=utf-8


import sys
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from PyQt5.QtWidgets import QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication, QMainWindow, QPushButton

class Communicate(QObject):
    closeApp = pyqtSignal()
    lcd_display = pyqtSignal()


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.i = 1
        self.initUI2()


    def initUI(self):

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("event")
        self.show()


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def plusone(self):
        self.i = self.i + 1
        self.lcd.display(self.i)


    def initUI2(self):

        self.lcd = QLCDNumber(self)
        #vbox = QVBoxLayout()
        #vbox.addWidget(lcd)

        #self.setLayout(vbox)
        self.lcd.move(0,0)

        btn1 = QPushButton("Button1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.c = Communicate()
        self.c.closeApp.connect(self.close)
        #self.i = 0
        self.c.lcd_display.connect(self.plusone)
        
        #lcd.display(self.i)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle("sender")
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')


    def mousePressEvent(self, event):
        #self.c.closeApp.emit()
        self.c.lcd_display.emit()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


