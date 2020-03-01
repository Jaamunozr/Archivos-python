import os #Libreria que permite ejecutar comandos en consola
from AES_Encriptar import Alg_AES

os.system("clear")  #Comando ejecutado en consola

def Seleccion():
	print ('-'*120)
	print ('Usted selecciono el método',Metodo)
	print ('-'*120)
	if Metodo == 'RSA':
		#Alg_RSA()
		print ('Hola mundo')
	elif Metodo =='AES':
		Alg_AES()
		print ('Hola mundo')

def inicio():
	global Metodo #Se debe nombrar ya que para las funciones  esa variable deja de existir
	while Metodo !='RSA' and Metodo != 'AES':
		os.system("clear")
		Metodo = input('Seleccion invalida, digite nuevamente el método a utilizar (RSA o AES):')
	Seleccion()

Metodo = input('Seleccione el método de encriptacion a usar en mayuscula (RSA o AES):')

if Metodo == 'RSA' or Metodo == 'AES':
	Seleccion()
else:
	inicio()
