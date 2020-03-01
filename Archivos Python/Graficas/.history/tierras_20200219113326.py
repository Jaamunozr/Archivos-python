import os
import pylab as pl
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
os.system("clear")

fig = pl.figure()
axx = Axes3D(fig)
X = np.arange(-10, 10, 0.25)
Y = np.arange(-10, 10, 0.25)
X, Y = np.meshgrid(X, Y)
ax, ay = 0.5 , 0.5

print(ax)
print(ay)
Z = np.sqrt(abs(X ** 3 + Y ** 3))

axx.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=pl.cm.hot)
axx.contourf(X, Y, Z, zdir='z', offset=-2, cmap=pl.cm.hot)
axx.set_zlim(-2, 2)

pl.show()