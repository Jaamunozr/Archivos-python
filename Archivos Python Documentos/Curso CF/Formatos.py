#Formatos en la impresión del texto
import os
os.system("clear")

#Primera letra en mayuscula
palabra = "hola mundo python3, python3 es libre"
Palabra = palabra.capitalize()
print(Palabra)

#Invertir mayusculas y minusculas
Cambio = Palabra.swapcase()
print(Cambio)

#Todo a mayuscula
Cambio = Palabra.upper()
print(Cambio)

#Todo a minuscula
Cambio = Palabra.lower()
print(Cambio)

#Primera letra mayuscula de cada palabra
Cambio = palabra.title()
print(Cambio)

#Reemplazo de palabras, incluyendo las repetidas
Cambio = palabra.replace("python3","cruel")
print(Cambio)
Cambio = palabra.replace("python3","cruel", 1) 
#Este uno (1) me indica, desde la primera palabra, cunatas quiero reemplazar
print(Cambio)

#Borrar espacion al inicio y al final del texto
Cambio = palabra.strip()

#Modificar cadenas de texto con variables string
texto_uno="python"
texto_dos = "casa"
texto = "hola mundo {a}. Te invito a pasar a {b}".format(b=texto_dos, a=texto_uno)
print(texto)

#Concatenar (Unir varios string y otros)
primer_texto = "Hola"
segundo_texto = "mundo"
tercer_texto = "python"
cuarto_texto = 3
concatenar = "Señores, "+primer_texto+" "+segundo_texto+" "+tercer_texto+str(cuarto_texto)
print (concatenar)