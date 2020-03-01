from matplotlib import pyplot
import time
import os

valores=(100,12,23)
colores=('red','green','blue')

pyplot.pie(valores, colors=colores) 

pyplot.draw()
time.sleep(2)
pyplot.pause(3) #Imprime la torta pero se omite para poder guardar el formato en .png
#pyplot.savefig('Prueba torta.png')

#os.system("exit")
#os.system("^Z")