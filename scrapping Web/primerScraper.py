#extraemos el contenido web

from urllib.request import urlopen


def main():
    file_web = open('web.html','wb')
    consulta = urlopen('https://uncp.edu.pe/')
    consulta = consulta.read()
    file_web.write(consulta)
    file_web.close()

if __name__ == '__main__':
    main()