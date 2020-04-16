import os
os.system("clear")
"""
listas=["uno","dos","tres","cuatro","hola mundo"]
dato = listas[3] #Indice de la lista
print (dato)
dato_dos=listas[-1]
print(dato_dos)

#En este caso no toma la posicion numero 2
sublista=listas[0:2] 
print(sublista)

#Datos tomados parcialmente
datos_tres=listas[2:]
datos_cuatro=listas[:3]
print(datos_tres)
print (datos_cuatro)

#Datos con saltos de 2
datos_cinco=listas[::2]
print(datos_cinco)

#Inverso de una lista
inverso=listas[::-1]
print(inverso)
"""
#orden de una lista 
lista=[1,43,453645.56,456,23,234,7,98,3]
print(lista)
lista.sort() #Forma ascendente
print(lista)
lista.sort(reverse=True) #Forma descendente
print(lista)
#Valores mayores y menores
print(max(lista))
print(min(lista))
#Longitud de lista
print(len(lista))
#Saber si un valor esta en nuestra lista
valor = 8 in lista
print(valor) #True o False
#Saber en que indice se encuentra un valor definido 
indice = lista.index(43)
print(indice)
#Saber cuantas veces está un mismo valor en la lista
conteo = lista.count(1)
print(conteo)