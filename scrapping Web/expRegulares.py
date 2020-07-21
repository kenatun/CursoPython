import re
import urllib

def parser3():
    cadena = "esta es una cadena que tomara ejemplo"
    #funcion sub()
    cadena1 = re.sub('funcion', 'sub', cadena)
    print(cadena1)


def parser2():
    #ejemplo2 , funcion findall() nos permite encontrar multiples resultados en cadenas de textos enornmes
    pagina = open('web.html',encoding="utf8")
    for l in pagina.readlines():
        b= re.findall('^<html>',l) #^
        if b:
            print(b)
        b = re.findall('</html>$',l)
        if b:
            print(b)
        b = re.findall('<div>.*<div>',l)
        if b:
            for c in b:
                d = re.split('<div>',c) #la funcion split() no permite cortal elementop

def parser1():
    pagina = open('web.html',encoding="utf8")
    for l in pagina.readlines():
        #Ejemplo 1. funcion search(), se utiliza para verificar existencia de caracteres
        #nos devuelve un objeto para verificar si la bsqueda es encontrada
        b = re.search('uncp',l)
        if b:
            print(l)
        else:
            pass



def main():
    parser1()
    parser2()
    parser3()


if __name__ == '__main__':
    main()