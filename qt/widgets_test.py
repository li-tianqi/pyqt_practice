#!/usr/bin/env python3
# coding=utf-8

import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QPushButton, QFrame, QSlider, QLabel, QProgressBar, QCalendarWidget
from PyQt5.QtCore import Qt, QBasicTimer, QDate
from PyQt5.QtGui import QColor, QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb = QCheckBox('Show title', self)
        cb.move(20,20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)
        
        self.col = QColor(0,0,0)
        
        redb = QPushButton('red', self)
        redb.setCheckable(True)
        redb.move(20, 60)
        
        redb.clicked[bool].connect(self.setColor)
        
        greenb = QPushButton('green', self)
        greenb.setCheckable(True)
        greenb.move(20, 110)
        
        greenb.clicked[bool].connect(self.setColor)
        
        blueb = QPushButton('blue', self)
        blueb.setCheckable(True)
        blueb.move(20, 160)
        
        blueb.clicked[bool].connect(self.setColor)
        
        self.square = QFrame(self)
        self.square.setGeometry(150, 60, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" % self.col.name())
        
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(20, 250, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)
        
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('mute.gif'))
        self.label.setGeometry(150, 200, 150, 150)
        
        
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(20, 380, 200, 25)
        
        self.pbtn = QPushButton('start', self)
        self.pbtn.move(30, 420)
        self.pbtn.clicked.connect(self.doAction)
        
        self.timer = QBasicTimer()
        self.step = 0
        
        
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 510)
        cal.clicked[QDate].connect(self.showDate)
        
        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(230, 510)
        
        
        
        
        
        self.setGeometry(300, 30, 580, 670)
        self.setWindowTitle('QCheckBox')
        self.show()
        
    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')
            
            
    def setColor(self, pressed):
        source = self.sender()
        
        if pressed:
            val = 255
        else:
            val = 0
            
        if source.text() == "red":
            self.col.setRed(val)
        elif source.text() == "green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)
            
        self.square.setStyleSheet("QFrame { background-color: %s }" % self.col.name())
        
        
    def changeValue(self, value):
        if value == 0:
            self.label.setPixmap(QPixmap('mute.gif'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap('min.gif'))
        elif value > 30 and value <= 80:
            self.label.setPixmap(QPixmap('med.gif'))
        else:
            self.label.setPixmap(QPixmap('max.gif'))
            
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.pbtn.setText("finished")
            return
            
        self.step = self.step + 1
        self.pbar.setValue(self.step)
        
        
    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.pbtn.setText('start')
        else:
            self.timer.start(100, self)
            self.pbtn.setText('stop')
            
            
    def showDate(self, date):
        self.lbl.setText(date.toString())
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

