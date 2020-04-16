import os
os.system('clear')


#Existen dos tipos de variables a usar, las de INSTANCIA y las de CLASE

class Circulo:
    pi = 3.1416 #pi es una variable de clase, pueden ser utilizadas por instancias
    def __init__(self, radio):
        self.radio = radio  #radio es una variable de instancia y su valor no se comparten entre instancias
        

#creamos dos objetos
Circulo_A = Circulo(10)
Circulo_B = Circulo(20)

Circulo_A.radio = 100

print(Circulo_A.radio) #Imprime variables de instancia
print(Circulo_B.radio) 

print(Circulo_A.pi) #Imprime variables de clase desde los objetos creados
print(Circulo.pi) #Imprime variables de clase desde la clase