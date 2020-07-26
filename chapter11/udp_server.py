import socket
from datetime import datetime

def open_server():
    server_address = ('localhost', 1111)
    max_size = 4096
    print('starting server at', datetime.now())
    
    # 소켓 생성 (AF_INET = IP소켓을 생성 / SOCK_DGRAM UDP 사용)
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 설정한 ip, port 에 도달하는 모든 데이터를 청취
    server.bind(server_address)

    # 서버에 도달하는 데이터그램을 대기
    data, client = server.recvfrom(max_size)

    print('at', datetime.now(), client, 'said', data)
    
    # 클라이언트에게 응답을 보낸 후 종료
    server.sendto(b'status is OK', client)
    server.close()