import socket
from _thread import *

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel, QPushButton, QTextEdit, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

# 서버 IP 및 열어줄 포트
HOST = '192.168.0.20'
PORT = 8080

client_sockets = [] # 서버에 접속한 클라이언트 목록
ID_LIST = [] # 서버에 접속한 ID 목록

# 서버 소켓 생성
print('>> Server Start')
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

def SendMessageToAll(message):
    for client_socket in client_sockets:
        client_socket.send(message.encode())

def threaded(client_socket, addr):
    data = client_socket.recv(1024)
    print('\n>> Connected by :', addr[0], ':', addr[1])
    ID_LIST.append(data.decode())
    SendMessageToAll(ID_LIST[len(client_sockets) - 1] + "님이 입장하셨습니다.")

        
    # 클라이언트가 접속을 끊을 때 까지 반복합니다.
    while True:
        try:
            # 데이터가 수신되면 클라이언트에 다시 전송합니다.(에코)
            data = client_socket.recv(1024)
            
            if not data:
                print('>> Disconnected by ' + addr[0], ':', addr[1])
                break

            print('>> Received from ' + addr[0], ':', addr[1], data.decode())
            # 서버에 접속한 클라이언트들에게 채팅 보내기
            # 메세지를 보낸 본인을 제외한 서버에 접속한 클라이언트에게 메세지 보내기
            for client in client_sockets:
                if client != client_socket:
                    client.send(data)

        except ConnectionResetError as e:
            print('>> Disconnected by ' + addr[0], ':', addr[1])
            break

    if client_socket in client_sockets:
        client_sockets.remove(client_socket)
        print('remove client list : ', len(client_sockets))

    client_socket.close()

try:
    while True:
        print('>> Wait')

        client_socket, addr = server_socket.accept()
        client_sockets.append(client_socket)
        start_new_thread(threaded, (client_socket, addr))
        
except Exception as e:
    print ('에러는? : ', e)

finally:
    server_socket.close()