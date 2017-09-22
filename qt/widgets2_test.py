#!/usr/bin/env python3
# coding=utf-8


import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QApplication, QHBoxLayout, QFrame, QSplitter, QStyleFactory, QComboBox
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.lbl = QLabel(self)
        qle = QLineEdit(self)

        qle.move(60, 100)
        self.lbl.move(60, 40)

        qle.textChanged[str].connect(self.onChanged)

        self.lbl2 = QLabel("Ubuntu", self)
        combo = QComboBox(self)

        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("Victor")

        combo.move(50, 150)
        self.lbl2.move(50, 250)

        combo.activated[str].connect(self.onActivated)



        self.setGeometry(300, 300, 300, 370)
        self.setWindowTitle("LineEdit")
        self.show()

    def onActivated(self, text):
        self.lbl2.setText(text)
        self.lbl2.adjustSize()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


    def initUI2(self):
        hbox = QHBoxLayout(self)

        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("splitter")
        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

