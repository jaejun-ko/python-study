import socket
from datetime import datetime

def connect_server():
    server_address = ('localhost', 2222)
    max_size = 1000
    print('starting client at', datetime.now())
    
    # 소켓 생성
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 서버에서 커넥션 얻어오기
    client.connect(server_address)
    client.sendall(b'hello server')
    
    # 서버의 응답을 전송 받아 출력한뒤 종료
    data = client.recv(max_size)
    print('at', datetime.now(), 'replied', data)
    client.close()