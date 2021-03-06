import pylab as pl
import numpy as np

# Crear una figura de 8x6 puntos de tamaño, 80 puntos por pulgada (Se modifica a 16x8)
pl.figure(figsize=(16, 8), dpi=100)

# Crear una nueva subgráfica en una rejilla de 1x1 (se podrian crean una de dos graficas en una reijlla)
pl.subplot(1, 1, 1)
# Obtencion de datos para seno y coseno (Desde -2pi hasta 2pi)
X = np.linspace(-2*np.pi, 2*np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

# Graficar la función coseno con una línea continua azul de 1 pixel de grosor
pl.plot(X, C, color="blue", linewidth=1.0, linestyle="-")

# Graficar la función seno con una línea continua verde de 1 pixel de grosor
pl.plot(X, S, color="green", linewidth=1.0, linestyle="-")

# Establecer límites del eje x
pl.xlim(-8.0, 8.0)

# Ticks en x
pl.xticks(np.linspace(-4, 4, 9, endpoint=True))

# Establecer límites del eje y (Divisiones en Y)
pl.ylim(-1.0, 1.0)

# Ticks en y (Impresión de intervalos)
pl.yticks(np.linspace(-1, 1, 4, endpoint=True))

# Guardar la figura usando 72 puntos por pulgada
# savefig("exercice_2.png", dpi=72)

# Mostrar resultado en pantalla
pl.show()