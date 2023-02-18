import socket
from _thread import *

HOST = '192.168.0.20'
PORT = 8080
LOGIN = False

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# 서버로부터 메세지를 받는 메소드
# 스레드로 구동 시켜, 메세지를 보내는 코드와 별개로 작동하도록 처리
def recv_data(client_socket) :
    while True :
        data = client_socket.recv(1024)

        print(repr(data.decode()))
start_new_thread(recv_data, (client_socket,))

if LOGIN == False:
    ID = input("채팅에서 사용할 아이디를 입력해주세요 : ")
    LOGIN = True
    
while True:
    message = '[ ' + ID + ' ] : ' + input('')
    if message == 'quit':
        close_data = message
        break

    client_socket.send(message.encode())


client_socket.close()
