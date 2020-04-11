import os
os.system('clear')

class Usuario: #Creamos una clase
    pass

codi = Usuario()  #Creamos un objeto a partir de esa clase, tambien conocida como ínstancia 
facilito= Usuario() #Creamos otro objeto o instancia

print(type(codi)) #Vemos a que clase pertenece ese objeto

#METODOS---------------------------------------
#Cremos un método, el cual es una función dentro de una clase:

class Usuario: #Creamos una clase
    pass
    def saluda(self, nombre): 
        #Agregamos la función en la clase y todos deben resivir un parametro, por defecto self, se puede agregar otra cosa
        print("Hola, soy un usuario " + nombre + " y esto es un método")


codi = Usuario()  #Creamos un objeto a partir de esa clase, tambien conocida como ínstancia 
facilito= Usuario() #Creamos otro objeto o instancia

codi.saluda("codi")
facilito.saluda("Facilito")

#ATRIBUTOS---------------------------------------
#Generamos atributos dentro y fuera de la clase

class Usuario:
    def saluda(self, nombre):
        return "Hola, soy un usuario " + nombre
    
    def mostrar_username(self): #Self hace referencia al objeto
        print(self.username)

    def mostrar_nombre(self): #Con este método muestro el atributo creado en consola
        print(self.nombre)

    def crear_nombre(self, nombre): #Con este método creo un atributo, dentro de la clase, dentro de un método
        self.nombre = nombre

codi = Usuario()
codi.username = "codi"  #Estos son lo atributos fuera de la clase
codi.correo = "codi@correo.com"#Esto es otro atributo fuera de la clase

facilito = Usuario()
facilito.username = 'Facilito'
facilito.correo = 'Facilito@correo.com'

codi.mostrar_username()
facilito.mostrar_username()
    
codi.crear_nombre("Codigo")
codi.mostrar_nombre()



#METODO __init__-----------------------------------------------------------
#Se pueden inicializar atributos dentro de __init__
class Usuario:
    def __init__(self,username="**", correo="**", nombre="**"): #El método __init__ recibe cierta cantidad de parametros
        self.username = username #Estos string poseen un valor de "**"
        self.corre = correo
        self.nombre = nombre
    
    def saluda(self):
        return "Hola, soy un usuario " + self.nombre
    
    def mostrar_username(self): #Self hace referencia al objeto
        print(self.username)

    def mostrar_nombre(self): #Con este método muestro el atributo creado en consola
        print(self.nombre)

 
codi = Usuario("Codi","codi@correo.com","Código") #Aqui ponemos argumentos para cada parametro
facilito = Usuario()

resultado = codi.saluda()
print(resultado)