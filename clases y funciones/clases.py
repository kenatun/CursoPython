
class Carro(object):
    def __init__(self,m):
        self.color = "Rojo"
        self.puertas = 5
        self.tipo = "antiguito"
        self.m = m

    def movilidad(self):
        if self.m==True:
            print("Acelerar")
        else:
            print("Frenar")

def main():
    while True:
        print("1. Acelerar")
        print("2. Frenar")
        valor = int(input("> "))
        if valor == 1:       
            c = Carro(True)
        else:
            c= Carro(False)
            c.movilidad()
    #print(c.color)
    #print(c.puertas)
    #print(c.tipo)

if __name__ == '__main__':
    main()