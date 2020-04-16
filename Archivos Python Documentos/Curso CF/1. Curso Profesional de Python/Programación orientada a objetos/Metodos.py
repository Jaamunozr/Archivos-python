import os
os.system('clear')

#TODAS SON CLASES

#Método simple------------------------------------------
print('MÉTODO SIMPLE')
class triangulo: #Creación de clase
    def area(base,altura): #Creación del método, se ponen las variables como parámetro
        return (base*altura) / 2  #Calculamos el área de un triangulo

Area = triangulo.area(10,20)  #INGRESAMOS DATOS PARA EL METODO SIMPLE
print(Area)

#Método de instancia------------------------------------
print('MÉTODO DE INSTANCIA')
class triangulo: #Creación de clase
    def area(self): #La cual tendra un método de instancia
        return (self.base*self.altura) / 2  #Calculamos el área de un triangulo
Triangulo = triangulo()
Triangulo.base = 10
Triangulo.altura = 20

resultado = Triangulo.area()
print(resultado)

#Método estático------------------------------------
print('MÉTODO ESTÁTICO')
class triangulo: #Creación de clase
    numero = 2 #Sí podemos usar variables de clase
    @staticmethod
    def area(base,altura): #Se ponen las variables como parámetro
        return (base*altura) / triangulo.numero  #Calculamos el área de un triangulo con una variable de clase

resultado = triangulo.area(20,10)
print(resultado) #En este método no podemos usar variables de instancia, solo de clase

#Métodos de clase----------------------------------
print ('MÉTODOS DE CLASE')
class Circulo:
    pi = 3.14159265
    @classmethod
    def area(cls, radio): #Parametro para un método de clase
        return cls.pi * radio **2
resultado = Circulo.area(10)
print(resultado) #Usaremos metodos de clase cuando necesitemos usar variables de clase
