## Ex 3-1. 창 띄우기.

import socket
from _thread import *

import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

HOST = '192.168.0.20'
PORT = 8080
LOGIN = False

class Login(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setFixedSize(QSize(500, 300))
        self.client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

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
        self.lbl1.setFont(QtGui.QFont("normal", 20))
        self.line_edit = QLineEdit()

        self.line_edit.returnPressed.connect(self.on_return_pressed)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.line_edit)
        vbox.addStretch()

        self.setLayout(vbox)

        # 창 크기 및 위치 설정
        self.setWindowTitle('My First Application') # 창 제목
        self.setWindowIcon(QIcon('appImage.png'))
        self.resize(500, 350)
        self.center()
        self.show()

    def open_chatroom(self):
        self.Chatroom = Chatroom()
        self.Chatroom.show()
        print('채팅방으로 이동합니다..')
        self.client_socket.connect((HOST, PORT))
        self.close()
        
    
    def on_return_pressed(self):
        text = self.line_edit.text()
        print(text)
        self.open_chatroom()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class Chatroom(QWidget):
    def __init__(self):
        super().__init__()

        # 버튼 생성
        self.btn = QPushButton('Close Window 2', self)

        # 버튼 클릭 시 실행할 함수 지정
        self.btn.clicked.connect(self.close)

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Window 2'))
        layout.addWidget(self.btn)
        self.setLayout(layout)
           
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    lg = Login()
    lg.show()
    
    sys.exit(app.exec_())
