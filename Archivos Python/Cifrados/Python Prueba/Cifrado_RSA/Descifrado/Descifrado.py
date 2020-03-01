from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

f = open("Texto_Cifrado.txt", "rb")

MensajeE = f.read()
key = RSA.importKey(open("llaveprivada.pem", "r").read())
cifrado = PKCS1_OAEP.new(key)
DM = cifrado.decrypt(MensajeE)
print (DM)
