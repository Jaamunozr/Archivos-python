from matplotlib import pyplot
import time
import os

hola=(100,12,23)
colores=('red','green','blue')
pyplot.pie(hola, colors=colores)
pyplot.show()
time.sleep(10)
os.system("^Z")