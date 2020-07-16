
import socket


s = socket.socket()
try:
    s.connect(("uncp.edu.pe",80))
    banner = s.recv(1024)
    print(banner)
except:
    print("Ocurrio un error")