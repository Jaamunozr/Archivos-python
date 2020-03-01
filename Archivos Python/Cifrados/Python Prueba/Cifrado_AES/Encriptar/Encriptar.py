from Crypto.Cipher import AES
from Crypto import Random

#Llamamos el archivo con la llave secreta de 16 bit (Se puede con 16, 24 o 32bits)
key = open('llave.txt', 'rb')
key = key.read()
key = key [:-1]

def encriptar(MensajeE):

    MensajeE = MensajeE
    #Se pasa por parametro al cifrado
    iv = Random.new().read(AES.block_size)
    #Se llama la clase AES y se cre un nuevo cifrado
    cifrado = AES.new(key, AES.MODE_CFB, iv)
    #Aqui se pasa la llave,  luego se cita la libreria MODE
    #Ahora encriptamos el mensaje
    msg = iv + cifrado.encrypt(MensajeE)
    f = open('Texto Encriptado.txt', 'wb')
    #Argumento a escribir debe ser de tipo binario 'wb'
    #Autores aseguran que es para archivos vacios, sin texto
    f.write(msg)
    f.close
#Aquí podemos hacer el llamado de lo que queremos encriptar
#Se debe establecer la opcion de poder llamar un archivo y asi poder encriptar su contenido.

TSE = open ('Texto sin encriptar.txt', 'rb')
TSE = TSE.read()
encriptar(TSE)


'''La librerian basic64 sirve para saber que traduce el texto
 que se acaba de crear, ver para futuras guias '''
