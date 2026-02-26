import socket

IP_address = "127.0.0.1"
port = 12345
msg = "Ahello from the other side"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"UDP client sending to {IP_address}:{port}")

s.sendto(msg.encode('utf-8'), (IP_address, port))

data, server_addr = s.recvfrom(1024)

print(f"Received from server: {data.decode('utf-8')}")

s.close()