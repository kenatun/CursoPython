
def resta(v1,v2):
    print("La resta es: {}".format(v1-v2))

def suma(v1,v2):
    print("La suma es: {}".format(v1+v2))

def multiplicacion(v1,v2):
    print("La multiplicacion es: {}".format(v1*v2))

def division(v1,v2):
    print("La division es: {}".format(v1/v2))

def main():
    while True:
        print("Bienvenida\n")
        print("1.- Suma 2 numeros")
        print("2.- Resta 2 numeros")
        print("3.- Divide 2 numeros")
        print("4.- Multiplica 2 numeros")
        print("5.- GG")
        opcion = int(input("Opcion: "))

        if opcion == 1:
            v1 = int(input("Valor 1: "))
            v2 = int(input("Valor 2: "))
            suma(v1,v2)
        elif opcion == 2:
            v1 = int(input("Valor 1: "))
            v2 = int(input("Valor 2: "))
            resta(v1,v2)
        elif opcion == 3:
            v1 = int(input("Valor 1: "))
            v2 = int(input("Valor 2: "))
            division(v1,v2)
        elif opcion == 4:
            v1 = int(input("Valor 1: "))
            v2 = int(input("Valor 2: "))
            multiplicacion(v1,v2)
        elif opcion == 5:
            exit()
        else:
            print("\n Opcion Invalida prro\n")


if __name__ == '__main__':
    main()