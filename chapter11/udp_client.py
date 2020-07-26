import socket
from datetime import datetime

def connect_server():
    server_address = ('localhost', 1111)
    max_size = 4096
    print('starting client at', datetime.now())
    
    # 소켓 생성
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 서버로 데이터 전송
    client.sendto(b'hello server', server_address)
    
    # 서버의 응답을 전송 받아 출력한뒤 종료
    data, server = client.recvfrom(max_size)
    print('at', datetime.now(), server, 'said', data)
    client.close()