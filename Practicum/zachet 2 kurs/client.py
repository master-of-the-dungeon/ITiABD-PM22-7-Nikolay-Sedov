import socket

def start_client(host='127.0.0.1', port=65432, message='Sedov Nikolay PM22-7'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(message.encode())
        data = s.recv(1024)
        print(f'Received echo: {data.decode()}')

if __name__ == '__main__':
    start_client()
