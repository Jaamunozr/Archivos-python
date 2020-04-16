import os
os.system('clear')
"""
#Primer ciclo a trabajar WHILE
numero = 12345
contador = 0
while numero >= 1:
    contador+=1
    numero=numero/10
else: #Se ejecuta cuando la condición termine 
    print(contador)

#Segundo ciclo a trabjar FOR
numeros=[1,2,3,4,5,6,7,8,9]
for numero in numeros:
    print (numero)

valores=((12,23),["hola mundo","hola"], (True,False))
for valor1, valor2 in valores:
    print(valor1, valor2)
"""
#Variables condicionadas
nota=int(input("digite la nota: "))
color = "rojo" if nota >= 5 else "verde"
print(color)