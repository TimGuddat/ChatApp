import asyncio
import socket


async def handle(conn):
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


async def start(server):
    server.listen()
    while True:
        conn, addr = server.accept()
        conns.append(conn)
        await handle(conn)
        # thread = Thread(target=handle, args=(conn,))
        # thread.start()


async def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(ADDR)
        await start(server)


if __name__ == '__main__':
    SERVER = '192.168.0.115'
    PORT = 5050
    ADDR = (SERVER, PORT)
    MAX = 1024
    FORMAT = 'utf-8'
    conns = []

    asyncio.run(main())
