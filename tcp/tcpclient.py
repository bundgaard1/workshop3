import socket 

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 7890  # The port used by the server

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    data = s.recv(1024)
    t = int.from_bytes(data,"big")
    s.close()

print(f"Received time: {t!r}")