import os
os.system('clear')

#Los diccionarios siempre tengras una llave asociada a cada valor
diccionario = {}
diccionario["llave"]="valor"
print (diccionario)

#Para agregar un nuevo valor:
diccionario["llave_dos"]="valor_dos"
diccionario["llave_tres"]=90
print (diccionario)
#Las llaves no pueden repetirse 

#Para imprimir el valor de una llave
resultado = diccionario["llave_tres"]
print(resultado)

#Saber si una llave esta en un diccionario 
resultado = "llave_tres" in diccionario
print(resultado)
#Tambien podemos usar el siguiente comando:
resultado = diccionario.get("llave_tres","no se encuentra la llave") #Forma recomendada
#si existe, imprime el valor, si no, imprime None o lo que tengas en texto
print(resultado)
#Tambien podemos agregar un nuevo valor si la llave que buscamos no esta
resultado = diccionario.setdefault("llave_cuatro","valor 4") #Forma recomendada
print(resultado)
print(diccionario)

#Para visualizar las laves de nuestro diccionario
print(diccionario.keys())
#Para visualizar los valores de nuestro diccionario
print(diccionario.values())

#Borrar un valor a partir de su llave:
#Método uno
del diccionario["llave"]
print(diccionario)
#Método dos
valor = diccionario.pop("llave_dos")
print(diccionario)
print(valor)