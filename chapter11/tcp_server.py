import socket
from datetime import datetime

def open_server():
    server_address = ('localhost', 2222)
    max_size = 1000
    print('starting server at', datetime.now())
    
    # 소켓 생성 (AF_INET = IP소켓을 생성 / SOCK_DGRAM UDP 사용)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 설정한 ip, port 에 연결하려는 커넥션 대기 (최대 5개 )
    server.bind(server_address)
    server.listen(5)

    # 서버에 도달하는 데이터그램을 대기
    client, addr = server.accept()
    data = client.recv(max_size)

    print('at', datetime.now(), client, 'said', data)
    
    # 클라이언트에게 응답을 보낸 후 종료
    client.sendall(b'status is OK')
    client.close()
    server.close()