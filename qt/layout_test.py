#!/usr/bin/env python3
# coding=utf-8


import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QTextEdit

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI3()
        
        
    def initUI(self):
        okButton = QPushButton("ok")
        cancelButton = QPushButton("cancel")
        
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addStretch(1)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)
        
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)
        
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('layout')
        self.show()
        
    def initUI2(self):
        grid = QGridLayout()
        self.setLayout(grid)
        
        names = ['Cls', 'Bck', '', 'Close', '7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '=', '+']
        
        positions = [(i,j) for i in range(5) for j in range(4)]
        
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)
            
        self.move(300, 150)
        self.setWindowTitle("grid layout")
        self.show()
        
        
    def initUI3(self):
        title = QLabel('title')
        author = QLabel('author')
        review = QLabel('review')
        
        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()
        
        grid = QGridLayout()
        grid.setSpacing(10)
        
        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)
        
        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)
        
        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)
        
        self.setLayout(grid)
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('review')
        self.show()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())