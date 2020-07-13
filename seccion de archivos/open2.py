#r = read
archivo = open('archivo1.txt','r')

#split quita el salto de linea pero usando read

#for l in archivo.read().split('\n'):
#   print(l)

#***************************************
#otra forma de leer

lista = archivo.read().split('\n')
for n in lista:
    print(n)
