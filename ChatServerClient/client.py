import socket

PORT = 5050
FORMAT = 'utf-8'
SERVER = '127.0.0.1'
ADDR = (SERVER, PORT)
MAX = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def receive():
    return client.recv(MAX).decode(FORMAT)


def send(msg):
    client.send(msg.encode(FORMAT))


def close_con():
    client.close()
