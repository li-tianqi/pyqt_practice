#!/usr/bin/env python3
# coding=utf-8


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QTextEdit
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):
    
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)
        
    
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        
        
        self.statusBar()
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        
        
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle("Menubar")
        self.show()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())