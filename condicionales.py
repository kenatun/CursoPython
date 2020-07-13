edad = int(input("Digita tu edad: "))
nombre = input("Digita tu nombre: ")
if edad == 18 and nombre == "chupetin":
    print("Hola", format(nombre))
    print("Eres mayor de edad")
    
elif edad < 18 and nombre == "chupetin":
    print("Hola", format(nombre))
    print("No eres mayor de edad")
else:
    print("Hola", format(nombre))
    print("No se tu edad")
        