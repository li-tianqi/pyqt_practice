#!/usr/bin/env python3
# coding=utf-8


import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QFrame, QColorDialog, QVBoxLayout, QSizePolicy, QLabel, QFontDialog
from PyQt5.QtGui import QColor



class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI2()


    def initUI(self):

        col = QColor(0, 0, 0)

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }"% col.name())
        self.frm.setGeometry(130, 22, 100, 100)



        #self.le = QLineEdit(self)
        #self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle("Dialog")
        self.show()


    def initUI2(self):
        vbox = QVBoxLayout()

        btn = QPushButton('dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn.move(20, 20)

        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog2)

        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font dialog')
        self.show()


    def showDialog(self):
        #text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name: ')

        #if ok:
        #    self.le.setText(str(text))

        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"% col.name())


    def showDialog2(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



