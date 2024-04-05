import socket 
import sys

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 7890  # The port used by the server

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: tpudpclient <adress> <port>")
        sys.exit(1)
        
    port = int(sys.argv[2])
    host = sys.argv[1]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    s.sendto(b"", (host, port))
    
    data = s.recv(1024)
    
    # decode the data into a integer
    t = int.from_bytes(data,"big")  



print(f"Received time: {t!r}")