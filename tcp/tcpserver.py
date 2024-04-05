import socket 
import sys
import time 

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 7890  # Port to listen on (non-privileged ports are > 1023)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: tpudpclient <port>")
        sys.exit(1)
        
    port = int(sys.argv[1])
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, port))
    s.listen()
    while True:
        conn, addr = s.accept()
        t = time.time() + 2208988800
        print(f"Connected by {addr}")
        
        data = int(t).to_bytes(4,"big")
        conn.send(data)
        conn.detach()



