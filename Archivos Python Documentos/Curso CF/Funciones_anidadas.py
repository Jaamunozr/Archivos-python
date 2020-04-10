import os
os.system('clear')
"""

#Función dentro de otra función
def  comenzar_play__list(list):
    print(list)
    def reproducir():
        nonlocal list
        list = [1,2,3,4]  #Modifica la variable local
        for val in list:
            print (val)
    reproducir()
    print (list) #Observamos la modificación d ela variable local
list = ["tema 1", "tema 2", "tema 3", "tema 4"]
comenzar_play__list(list)
print (list)

"""


#Generadores
#1
def tabla_multiplicar(numero, maximo=10):
    for posicion in range(1,maximo+1):
        yield numero * posicion   #"yield" me permite no declarar variables a imprimir despues
for resultado in tabla_multiplicar(9):
    print (resultado)
#2
def tabla_multiplicar(numero, maximo=10):
    """este es un comentario para documentar la función"""
    for posicion in range(1,maximo+1):
        yield numero * posicion, numero, posicion   #"yield" me permite no declarar variables a imprimir despues
for resultado, numero, posicion in tabla_multiplicar(9,20):
    print (numero,"*", posicion, "=", resultado)

#Podemos trabajar con la documentación a través de su atributo ____doc____, donde miraremos los comentarios de esa función
print(tabla_multiplicar.__doc__)  #Información de la función

