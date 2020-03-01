print ('-'*120)
print ('\n ALGORITMO DE ENCRIPTACION AES \n ')
def Alg_AES():

	while True:
		try:
			llave= input ('Indique el archivo en que se encuentra alojada la llave (ejm: "llave.txt"): \n \n')
			key = open(llave, 'rb')
			key = key.read()
			key = key [:-1]
			break
		except FileNotFoundError:
			print ('''\n Archivo ""''' + llave+ '''"" no encontrado\n''')

	from Crypto.Cipher import AES
	from Crypto import Random
	#Llamamos el archivo con la llave secreta de 16 bit (Se puede con 16, 24 o 32bits)

	def encriptar(MensajeE):
	    MensajeE = MensajeE
	    #Se pasa por parametro al cifrado
	    iv = Random.new().read(AES.block_size)
	    #Se llama la clase AES y se cre un nuevo cifrado
	    cifrado = AES.new(key, AES.MODE_CFB, iv)
	    #Aqui se pasa la llave,  luego se cita la libreria MODE
	    #Ahora encriptamos el mensaje
	    msg = iv + cifrado.encrypt(MensajeE)
	    while True:
                       try:
                                Encriptado = input ('\n Indique el nombre del nuevo archivo encriptado (ejm: " encriptado.txt"): \n \n')
                                f = open(Encriptado, 'wb')
                                #Argumento a escribir debe ser de tipo binario 'wb'
                                #Autores aseguran que es para archivos vacios, sin texto
                                f.write(msg)
                                f.close
                                break
                       except FileNotFoundError:
                                print ('''\n Archivo ""''' + Sin_Encriptar + '''"" no valido\n''')

	#Aquí podemos hacer el llamado de lo que queremos encriptar
	while True:
		try:
			Encriptado = input ('\n Indique el nombre del archivo a encriptar (ejm: "AES encriptar.txt"): \n \n')
			TSE = open (Encriptado, 'rb')
			TSE = TSE.read()
			encriptar(TSE)
			break
		except FileNotFoundError:
			print ('''\n Archivo ""''' + Encriptado + '''"" no valido\n''')
#Alg_AES()
