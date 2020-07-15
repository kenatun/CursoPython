
import requests
import argparse  
from os import path

parser = argparse.ArgumentParser()
parser.add_argument('-f','--file',help="Indica el archivo a subir")
parser = parser.parse_args()

def main():
    if parser.file:
        if path.exists(parser.file):
            archivo= open(parser.file,'rb')
            headers = {'User-Agent':'Firefox'}
            peticion = requests.post(url="https://curso--python-0-prueba-pentest1.000webhostapp.com/",files={'uploaded_file':archivo},headers=headers)
            if parser.file in peticion.text:
                print(peticion.text)
                print("Arhivos subido cuaack")
            else:
                print("Fallo subida de archivo")

        else:
            print("No existe el archivo")

    else:
        print("Nesecito un archivo para subir")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo....")