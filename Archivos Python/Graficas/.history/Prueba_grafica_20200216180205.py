from matplotlib import pyplot
import time
import os

valores=(100,12,23)
colores=('red','green','blue')

pyplot.pie(valores, colors=colores) 
pyplot.pause(3) 
#Imprime la torta por un tiempo no mayor a 2 segundos

#pyplot.savefig('Prueba torta.png') 
# #Guarda la imagen en formato .png en la misma direccion donde se encuentra el programa
os.system("clear")