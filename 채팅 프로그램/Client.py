import socket
from _thread import *

HOST = '192.168.0.20'
PORT = 8080
LOGIN = False

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

## 로그인
if LOGIN == False:
    ID = input("채팅에서 사용할 아이디를 입력해주세요 : ")
    LOGIN = True
    client_socket.connect((HOST, PORT))
    client_socket.send(ID.encode())

## 채팅 받기
def recv_data(client_socket) :
    while True :
        data = client_socket.recv(1024)

        print(repr(data.decode()))
start_new_thread(recv_data, (client_socket,))

## 채팅 보내기
while True:
    message = input('')
    sender = '[ ' + ID + ' ] : '
    msg = sender + message
    if message == 'quit':
        close_data = msg
        break

    client_socket.send(msg.encode())

client_socket.close()
