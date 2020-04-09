import os
os.system("clear")

def saludo(nombre='', apellido='', edad=10, dias=0):
    return print("Hola {} {}, felices {}, {} de cuarentena".format(nombre,apellido,edad,dias))

saludo("javier","muñoz",10)


#funciones con N datos a ingresar
def suma(*args):
    total = 0 
    for valor in args:
        total+=valor
    return total

ecuacion =suma  #Aquí declaramos una funcion en una variable
print(ecuacion(1,2,3,4,5))


#Otra opción de declarar una función en un variables es con LAMBDA

funcion = lambda grados=0,ajuste=90: grados*1.8+32 + ajuste
print(funcion(32,100))

#Estas son algunas formas en las cuales podemos crear funciones lambdas más complejas.
"""
sin_parametros = lambda : True

con_valores = lambda val, val1=10, val2=10 : val + val1 + val2

con_asterisco = lambda *args : args[0]

con_doble_asterisco = lambda **kwargs : args[0]

con_asteriscos = lambda *args , **kwargs : kwargs.get('key', False)

"""