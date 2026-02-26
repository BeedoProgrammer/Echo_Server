import socket

IP_address = "127.0.0.1"
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((IP_address, port))

print(f"UDP Server listening on {IP_address}:{port}")

while True:
    data, addr = s.recvfrom(1024)

    msg = data.decode('utf-8').strip()

    if not msg:
        continue    # Skip empty messages to prevent crashes on msg[0]

    # Used "".join() to convert the sorted list back into a string
    if msg[0] == 'A':
        new_msg = "".join(sorted(msg[1:], reverse=True))
    elif msg[0] == 'C':
        new_msg = "".join(sorted(msg[1:]))
    elif msg[0] == 'D':
        new_msg = msg[1:].upper()
    else:
        new_msg = msg
    
    s.sendto(new_msg.encode('utf-8'), addr)
