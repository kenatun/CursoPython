
""" 
try:
    while True:
        print("Hola")
#except NameError:
  #  print("L no está definido gaaa")
except KeyboardInterrupt:
    print("Salida Forzosa")
finally:
    print("Termino la ejecucuion")
 """
#***************************
try:
    raise IOError
except IOError:
    print("Ocurrio un error")