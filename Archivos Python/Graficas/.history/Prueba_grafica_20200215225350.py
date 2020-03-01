from matplotlib import pyplot
import time
import os
valores=(100,12,23)
colores=('red','green','blue')

pyplot.pie(valores, colors=colores) 
pyplot.ion()

#pyplot.show() #Imprime la torta pero se omite para poder guardar el formato en .png
time.sleep(5)
#pyplot.savefig('Prueba torta.png')
#time.sleep(5)
#os.system("clear")
#os.system("^Z")