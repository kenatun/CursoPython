
class prueba1(object):
    def __init__(self,radio):
        self.radio = radio

    @classmethod #nos ayuda a usar una funcion
    #sin que anes la clase sea atribuida a un objeto
    def saludo(cls,nombre):
        print("Hola {}".format(nombre))

    @staticmethod
    def saludo_static():
        print("Bienvenido")

    @property
    def area_circulo(self):
        return 3.1416*(self.radio**2)

def main():
    #class methos*****

    #nombre = input("Nombre: ")
    #prueba1.saludo(nombre)

    #static metodo*****

    #c=prueba1()
    #c.saludo_static()

    #otra prueba
    c = prueba1(5)
    area = c.area_circulo
    print(area)


if __name__ == '__main__':
    main()