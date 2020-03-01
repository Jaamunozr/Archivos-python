from matplotlib import pyplot
import time
import os

valores=(100,12,23)
colores=('red','green','blue')

pyplot.pie(valores, colors=colores) 

pyplot.show(block=False) #Imprime la torta pero se omite para poder guardar el formato en .png
#pyplot.savefig('Prueba torta.png')
#time.sleep(5)
#os.system("exit")
#os.system("^Z")