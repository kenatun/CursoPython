

import wget
from xml.etree.ElementTree import parse

def main():
    download = wget.download(url="https://curso-python-0-pruebas-pentest-dvwa1.000webhostapp.com/administrator/manifests/files/joomla.xml")
    archivo = parse("joomla.xml")
    for element in archivo.find_all('version'):
        ver = element.text
    
    print(ver)
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliend")
        exit()