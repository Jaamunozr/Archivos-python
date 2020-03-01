import pylab as pl
import numpy as np

# Crear una figura de 8x6 puntos de tamaño, 80 puntos por pulgada (Se modifica a 16x8)
pl.figure(figsize=(16, 8), dpi=100)

# Crear una nueva subgráfica en una rejilla de 1x1 (se podrian crean una de dos graficas en una reijlla)
pl.subplot(1, 1, 1)
# Obtencion de datos para seno y coseno (Desde -2pi hasta 2pi)
X = np.linspace(-2.1*np.pi, 2.1*np.pi, 256, endpoint=True) #el numero 256 es la cantidad de datos en ese intervalo
C, S = np.cos(X), np.sin(X)

# Graficar la función coseno con una línea continua azul de 1 pixel de grosor
pl.plot(X, C, color="blue", linewidth=1.0, linestyle="-")

# Graficar la función seno con una línea continua verde de 1 pixel de grosor
pl.plot(X, S, color="green", linewidth=1.0, linestyle="-")

# Establecer límites del eje x (Divisiones en X)
pl.xlim(-8.0, 8.0)

# Ticks en x(Impresión de intervalos, cantidad de datos mostrados en el eje)
pl.xticks(np.linspace(-8, 8, 17, endpoint=True))

# Establecer límites del eje y (Divisiones en Y)
pl.ylim(-1.0, 1.0)

# Ticks en y (Impresión de intervalos, cantidad de datos mostrados en el eje)
pl.yticks(np.linspace(-1, 1, 5, endpoint=True))

'''Otra opcion de determinar los limites a imprimir
pl.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
pl.yticks([-1, 0, +1]) '''

pl.gca()  # gca stands for 'get current axis'
#ax.spines['right'].set_color('none')
#ax.spines['top'].set_color('none')
#ax.xaxis.set_ticks_position('bottom')
#ax.spines['bottom'].set_position(('data',0))
#ax.yaxis.set_ticks_position('left')
#ax.spines['left'].set_position(('data',0))

# Guardar la figura usando 72 puntos por pulgada
# savefig("exercice_2.png", dpi=72)

#Indicamos los espacios entre los bordes de grafica y las graficas
#pl.xlim(X.min() * 1.1, X.max() * 1.1)
pl.ylim(C.min() * 1.1, C.max() * 1.1)

# Mostrar resultado en pantalla (Con 2 segundos de muestreo)
pl.pause(10)
