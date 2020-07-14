
def saludo(nombre1,edad1):
    print("Hola {} tienes {} años".format(nombre1,edad1))


def main():
    nombre = input("Nombre: ")
    edad = int(input("Edad prro: "))
    saludo(nombre,edad)

if __name__ == '__main__':
    main()