from Crypto.PublicKey import RSA

#Creamos la llave de 2048 (16, 24 o 32bits)
llave = RSA.generate(2048)
#-----------------------------------------------
#Generamos un archivo y escribimos
f = open("llaveprivada.pem", "wb")
#.PEM es un archivo certificado de correo mejorado
f.write(llave.exportKey('PEM'))
f.close
#-----------------------------------------------
f = open("llavepublica.pem", "wb")
#.PEM es un archivo certificado de correo mejorado
f.write(llave.publickey().exportKey('PEM'))
f.close


