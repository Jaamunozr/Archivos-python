import os
os.system("clear")

#Para tipo string:
nombre=input("¿Cuál es tu nombre?\n") 
print("Hola", nombre)

#Para enteros:

edad=int(input("¿Cuál es tu edad?\n"))
print("Edad", edad)

#Para flotante:
peso=float(input("¿Cuál es tu peso?\n"))
print("Peso",peso)

#Para Booleano
autorizado = input("¿Estas autorizado? (si/no)\n") == "si"
print("Autorizado", autorizado)