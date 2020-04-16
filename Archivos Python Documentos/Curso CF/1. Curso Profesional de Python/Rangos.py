import os
os.system('clear')

#Rango de números
for valor in range(-10,10): #No toma el ultimo número 
    print (valor)


#Saber la posicion y el valor de la msima en una lista 
lista = [1,2,3,4,5,6,7,8,9]
for indice, valor in enumerate(lista):
    print("indice:", indice, "valor:", valor)

#Palabras Reservadas
Titulo = "Javier Muñoz"
for caracter in Titulo:
    if caracter == "M":
        break #Finaliza el ciclo de manera forzada
    print (caracter)

for caracter in Titulo:
    if caracter == "M":
        continue #continua el ciclo pero elimina la condición anterior, salta a la siguiente interacción
    print (caracter)