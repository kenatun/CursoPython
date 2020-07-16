import sys
from shodan import Shodan
from importlib import reload

if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding("utf8")

def main():
    api = Shodan('zGToTmCJQ8QICf7NYkDEcoFkKI3t0QEi')
    h = api.host('72.167.226.7')
    
    print('''
        Direccion: {}
        Ciudad: {}
        Isp: {}
        Org: {}
        Ports: {}
        '''.format(h['ip_str'],h['city'],h['isp'],h['org'],h['ports']))
    file = open('escaneo.txt','a+')


    for elemento in h['data']:
        lista = elemento.keys()
        for l in lista:
            file.write(str(elemento[l]))
    file.close()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Saliend")
        exit()

   