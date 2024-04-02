import socket 
import sys

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 7890  # The port used by the server

if __name__ == "__main__":
    if len(sys.argv) == 3:
        host = sys.argv[1]
        port = int(sys.argv[2])
    else:
        exit()
        
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    s.sendto("".encode(), (host, port))
    data = s.recv(1024)
    t = int.from_bytes(data,"big")

print(f"Received time: {t!r}")