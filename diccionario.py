#diccionarios

diccionario = dict(nombre="Ken", plataforma="cuack", edad=18)
#print(diccionario["nombre"])

#**********************************

#print(diccionario)
#a = diccionario.items()
#print(a)

#*******************
#****copy

#b=diccionario.copy()
#print(b)

#*******************
#****keys

#keys = diccionario.keys()
#print(keys)

#*******************
#****values

#values = diccionario.values()
#print(values)

#*******************

for n in diccionario.keys():
    print("{} Su valor es: {}".format(n,diccionario[n]))

