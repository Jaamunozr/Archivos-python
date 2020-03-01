from Crypto.Cipher import AES
from Crypto import Random
#Aqui asumimos que la llaven la conocen por defecto, asi pueden desencripatr
#Se debe implementar a futuro el llamo de un archivo con su respectiva llave

f = open("Texto Encriptado.txt", "rb")
MensajeD = f.read()

keys = open("llave.txt","rb")
key = keys.read()
key = key[:-1]
print (MensajeD)
print (key)
def desencriptar(MensajeD):
	MensajeD = MensajeD
	#La llave solo se puede crear con 16, 24 o 32 bots
	#Al cambiar la clave 
#	key = "la llave secreta"
	iv = Random.new().read(AES.block_size)
	cifrado = AES.new(key, AES.MODE_CFB, iv)
        #Ahora desencriptamos en esta parte
	msg = cifrado.decrypt(MensajeD)
	print (msg)
	TD=open ('Texto desencriptado.txt', 'wb')
	TD.write(msg)
	TD.close
desencriptar(MensajeD)
