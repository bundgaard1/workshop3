import socket 
import time 

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 7890  # Port to listen on (non-privileged ports are > 1023)

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        t = time.time()
        conn.send(int(t).to_bytes(4,"big"))
        conn.detach()



