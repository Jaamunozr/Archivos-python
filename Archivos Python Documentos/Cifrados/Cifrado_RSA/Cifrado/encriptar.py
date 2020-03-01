from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

MensajeE = b"Hola mundo cruel"

#MensajeE = Mensaje.read()

key = RSA.importKey(open("llavepublica.pem", "r").read())
cifrado = PKCS1_OAEP.new(key)
Cifrar_Mensaje= cifrado.encrypt(MensajeE)

f= open("Texto_Cifrado.txt", "wb")
f.write(Cifrar_Mensaje)
f.close
