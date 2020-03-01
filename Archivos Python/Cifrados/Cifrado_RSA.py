import Crypto 
import binascii

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
random_generator = Crypto.Random.new().read

private_key = RSA.generate(1024, random_generator)
public_key=private_key.publickey()


private_key = private_key.exportKey(format='DER')
public_key = public_key.exportKey(format='DER')

private_key = binascii.hexlify(private_key).decode('utf8')
public_key = binascii.hexlify(public_key).decode('utf8')

#print (public_key)
#print (private_key)

#Proceso inverso
private_key = RSA.importKey(binascii.unhexlify(private_key))
public_key = RSA.importKey(binascii.unhexlify(public_key))

Mensaje = 'Hola mundo'
Mensaje = Mensaje.encode()

cipher = PKCS1_OAEP.new(public_key)
Mensaje_encriptado = cipher.encrypt(Mensaje)

print (Mensaje_encriptado)

cipher = PKCS1_OAEP.new(private_key)
Mensaje = cipher.decrypt(Mensaje_encriptado)

print (Mensaje)
