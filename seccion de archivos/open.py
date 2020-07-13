#w = write

archivo = open("archivo1.txt","w")
nombre = input("Nombre: ")
edad = input("edad: ")
pais = input("pais: ")

archivo.write(nombre)
archivo.write("\n")
archivo.write(edad)
archivo.write("\n")
archivo.write(pais)

print("he escrito los datos gaaaaaaaa")

archivo.close()
