import socket 
import sys
import time 

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 7890  # Port to listen on (non-privileged ports are > 1023)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        port = int(sys.argv[1])
    else:
        exit()
        
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST, port))
    while True:
        data, addr = s.recvfrom(1024)
        print(f"Connected by {addr}")
        t = time.time()
        s.sendto(int(t).to_bytes(4), addr)


