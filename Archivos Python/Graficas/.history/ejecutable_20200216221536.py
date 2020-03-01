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
#AGREGAR LINEAS DE EJES Y QUITAR EL RECUADRO:

ax = pl.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# Guardar la figura usando 72 puntos por pulgada
# savefig("exercice_2.png", dpi=72)

#Indicamos los espacios entre los bordes de grafica y las graficas
#pl.xlim(X.min() * 1.1, X.max() * 1.1)
pl.ylim(C.min() * 1.1, C.max() * 1.1)

#AGREGRA UNA LEYENDA
pl.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="Coseno")
pl.plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="Seno")
pl.legend(loc='upper left')

#AGREGRA UNA ANOTACION EN UN PUNTO CONOCIDO
t = 2 * np.pi / 3
#Para coseno------------------------------------------------------------------------------------
pl.plot([t, 0], [np.cos(t), np.cos(t)], color='blue', linewidth=2.5, linestyle="--")
#pl.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle="--")
pl.scatter([t, ], [np.cos(t), ], 50, color='blue') #DEFINE LAS CARACTERISTICAS DEN PUNTO (CIRCULO)
pl.annotate(r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',#DATOS A IMPRIMIR DEL TEXTO
            xy=(t, np.sin(t)), xycoords='data', #COORDENADAS DE REFERENCIA PARA LA FLECHA Y EL TEXTO
            xytext=(+10, +30), textcoords='offset points', fontsize=16,#INDICAN POSICION DEL TEXTO 
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2")) #DIRECCION DE LA FLECHA
#Para seno--------------------------------------------------------------------------------------
pl.plot([t, t],[0, np.sin(t)], color='red', linewidth=2.5, linestyle="--")
pl.scatter([t, ],[np.sin(t), ], 50, color='red')
pl.annotate(r'$cos(\frac{2\pi}{3})=-\frac{1}{2}$',
            xy=(t, np.cos(t)), xycoords='data',
            xytext=(-90, -50), textcoords='offset points', fontsize=16,
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))#DIRECCION DE LA FLECHA




# Mostrar resultado en pantalla (Con 2 segundos de muestreo)
pl.pause(100)
