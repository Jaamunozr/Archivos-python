from matplotlib import pyplot
import time
import os
valores=(100,12,23)
colores=('red','green','blue')
pyplot.ion()
pyplot.pie(valores, colors=colores) 
pyplot.ion()
#pyplot.show() #Imprime la torta pero se omite para poder guardar el formato en .png
#pyplot.savefig('Prueba torta.png')
#time.sleep(5)
os.system("clear")
#os.system("^Z")
iprint ('hola mundo')