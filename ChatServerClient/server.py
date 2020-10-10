import socket
from threading import Thread


def handle(conn, addr):
    connected = True
    while connected:
        msg = conn.recv(MAX).decode(FORMAT)
        if msg == 'exit':
            connected = False
            conn.send('exit'.encode(FORMAT))
            i = conns.index(conn)
            conns.pop(i)
        else:
            message = msg.encode(FORMAT)
            send_all(message)

    conn.close()


def send_all(message):
    for con in conns:
        con.send(message)


def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        conns.append(conn)
        thread = Thread(target=handle, args=(conn, addr))
        thread.start()


if __name__ == '__main__':
    SERVER = '127.0.0.1'
    PORT = 5050
    ADDR = (SERVER, PORT)
    MAX = 1024
    FORMAT = 'utf-8'
    conns = []

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    start()
