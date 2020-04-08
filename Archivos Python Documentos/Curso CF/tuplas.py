#No se pueden modificar una vez se define en el programa 

import os 
os.system("clear")
Tupla = (1,2,3,4,"Hola mundo")
print(Tupla) #Son más rápidas que las listas

#Podemos generar una subtupla
sub=Tupla[1:3] #Recordar que así no se toma la última posición
print(sub)

#Podemos generar valores de acuerdo a las posiciones de la tupla en un solo renglon
a,b,c,*d=Tupla #El asterisco guarda el resto en esa última variable
print(a,b,c,d)
a,b,*c,d=Tupla #El asterisco reorganiza las variables a ser guardadas
print(a,b,c,d)
a,_,b,c,d=Tupla # No toma el valor de la posicion 1 
print(a,b,c,d)

#Generar arreglos entre tuplas y listas
tupla=(1,2,3,4,5,6,7)
lista=[10,20,30,40]
hola=[1,1,1,1,1,1,1,1,1]
resultado=zip(tupla, lista, hola) #Objeto zip al que se le pueden agregar N cantidad de listas y/o tuplas
resultado=list(resultado) # Tambien se puede representar como tuple(resultado)
print(resultado)


#De listas a tuplas 
tupla=(1,2,3,4,5,6,7)
lista=[10,20,30,40]
Ntupla=tuple(lista)
Nlista=list(tupla)
