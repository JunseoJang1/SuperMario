## Ex 3-1. 창 띄우기.

import socket
from _thread import *

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

HOST = '192.168.0.20'
PORT = 8080
LOGIN = False

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setFixedSize(QSize(500, 300))

    def initUI(self):
        #self.move(300, 300)
        #self.resize(400, 200)
        #self.setGeometry(300, 300, 300, 300) # move() 와 resize() 을 합쳐놓은 것
        
        """
        label1 = QLabel('Label1', self)
        label1.move(20, 20)
        label2 = QLabel('Label2', self)
        label2.move(20,60)

        btn1 = QPushButton('Button1', self)
        btn1.move(80, 13)
        btn2 = QPushButton('Button2', self)
        btn2.move(80, 53)
        """

        self.lbl1 = QLabel('채팅방에서 사용할 이름을 입력하세요 ')
    
        self.line_edit = QLineEdit()


        self.line_edit.returnPressed.connect(self.on_return_pressed)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.line_edit)
        vbox.addStretch()

        self.setLayout(vbox)
        
        self.setWindowTitle('My First Application') # 창 제목
        self.setWindowIcon(QIcon('appImage.png'))
        self.resize(500, 350)
        self.center()
        self.show()

    def on_return_pressed(self):
        text = self.line_edit.text()
        print(text)
        event = QtGui.QKeyEvent(QtCore.QEvent.KeyPress, QtCore.Qt.Key_Enter, QtCore.Qt.NoModifier)
        event.ignore()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
           
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
