import socket
import threading

def handle_client(conn, addr):
    print(f"{addr} connected")

    connection = True

    while connection:
        try:
            msg = conn.recv(1024).decode('utf-8')

            if msg == "DISCONNECT":
                connection = False
                print(f"{addr} disconnected")
            # In TCP empty msg means connection failed
            elif not msg:
                connection = False
                print(f"{addr} disconnected")
            else:
                if msg[0] == 'A':
                    new_msg = "".join(sorted(msg[1:], reverse=True))
                elif msg[0] == 'C':
                    new_msg = "".join(sorted(msg[1:]))
                elif msg[0] == 'D':
                    new_msg = msg[1:].upper()
                else:
                    new_msg = msg
    
                conn.send(new_msg.encode('utf-8'))
        except ConnectionResetError:
            connection = False
            print(f"{addr} disconnected")

    conn.close()


IP_address = "127.0.0.1"
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP_address, port))
s.listen()

print(f"TCP Server listening on {IP_address}:{port}")

while True:
    conn, addr = s.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print(f"Active Connections: {threading.active_count() - 1}")

