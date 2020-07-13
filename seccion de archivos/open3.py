#a=append
#si usas w chanca los datos
archivo = open('archivo1.txt','a')
dedicacion = input("Dedicacion: ")
empresa = input("Empresa: ")
idioma = input("Idioma: ")

archivo.write("\n")
archivo.write(dedicacion)
archivo.write("\n")
archivo.write(empresa)
archivo.write("\n")
archivo.write(idioma)

archivo.close()