#Permite crear clases a partir de clases existentes en el mismo código
#Esto evita que se escriba el mismo código dos veces
#Las clases que se piensan llamar o heredar deben estár nombradas antes, lo ideal es que sea al inicio del programa

import os 
os.system('clear')

class Animal: #Clase "padre" que se puede heredar
    def comer(self):
        return print('comiendo')
    
    def dormir(self):
        return print('duermiendo')
    def comun(self):
        return print ("Método común Animal")

class Mascota: #Clase "padre" que se puede heredar
    def fecha(self, fecha): 
        Mascota.fecha = fecha
        return print ("Fecha de nacimiento",fecha)
    def comun(self):
        return print ("Método común Mascota")

class Perro (Animal, Mascota): #Herencia multiple
    #Hereda de la clase "Animal", puede "dormir" y "comer", además hereda las cacarteristicas de clase "Mascota"
    def __init__(self,nombre):
        self.nombre = nombre
        return print(nombre)

    def ladrar(self):
        return print('ladrando') 
    
    def comun(self):
        return print ("Método común Perro")

    def dormir(self):  #Modificación del metodo "dormir" de la clase "Animal" (SOBRE ESCRIBIR)  
        #Basicamente es agregar un nuevo método con otras caracteristicas
        print(self.nombre, "esta duermiendo")
        print ("Esto se imprime de Animal: ") 
        Animal.dormir(self) #Podemos llamar a  otros métodos de la clase "padre", en este caso, clase "Animal"

class Gato (Animal):#Hereda de clase Animal
    def ronronear(self):
        return print("ronroneo")
        
lukas = Perro("lukas")
lukas.ladrar()
lukas.comer() 
lukas.dormir()
lukas.fecha(12345)
lukas.comun() #Los métodos comunes se pueden presentar tanto en las clases padres, como en las que heredan
#Python busca primero en su clase heredada y luego en el orden citado (Animal, mascota) de sus clases padre

print("\nmishi") #Imprimiremos el nombre del gato, ya que nuestra clase "Gato" no lo muestra 
mishi = Gato()
mishi.ronronear()
mishi.comer()
mishi.dormir()