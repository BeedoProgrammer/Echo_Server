import socket

IP_address = "127.0.0.1"
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP_address, port))
print(f"Client connected to {IP_address}:{port}")

connection = True

while connection:
    msg = input()

    if not msg:
        print("Cannot send an empty message. Try again.")
        continue

    s.send(msg.encode('utf-8'))

    if msg == "DISCONNECT":
        connection = False
        print(f"Client disconnected from {IP_address}:{port}")
    else:
        data = s.recv(1024)
        print(f"Received from server: {data.decode('utf-8')}")

s.close()