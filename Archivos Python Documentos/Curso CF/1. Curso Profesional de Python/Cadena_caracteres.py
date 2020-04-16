import os
os.system("clear")
#Pilas, no podemos modificar un string que ya fue declarado
Palabra = "Hola mundo"
Resulatado = len (Palabra)
print (Resulatado)
Resulatado_1=Palabra[1]
print(Resulatado_1)

#Pasar de un string a una lista e indicar como se divide cada elemento
ABC= "a; b; c; d; e; f"
separador = "; "  
resultado = ABC.split(separador)
#Con el comando split, indicamos la separación, ademas podemos indicar con que caracter separa 
print(resultado)

#Pasar de una lista a un string
nuevo_string= "_*_".join(resultado) #Entre comilla sponemos el simbolo de separación 
print(nuevo_string)

#Texto con saltos de linea
Texto = """Texto con 
saltos 
de un par de lineas"""
resultado = Texto.splitlines()
print(resultado)