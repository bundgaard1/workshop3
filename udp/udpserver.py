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
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST, port))
    
    while True:
        data, addr = s.recvfrom(1024)
        t = time.time() + 2208988800
        print(f"Recieved datagram from {addr}, send time: {t!r}")
        # encode the data into integer
        data = int(t).to_bytes(4)
        s.sendto(data, addr)


