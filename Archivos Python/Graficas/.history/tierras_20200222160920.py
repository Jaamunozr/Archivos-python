import os
import pylab as pl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

os.system("clear")


fig = pl.figure()
axx = Axes3D(fig)
raiz=np.sqrt
ln=np.log
 
X = np.arange(-2, 12, 1)
Y = np.arange(-2, 12, 1)
#X, Y = np.meshgrid(X, Y)
print (np.count_nonzero(X))
l = 2
rho= 100
ik=25
Electrodos=8
E=Electrodos-1

P=np.array([
    [0.55, 0.55],   #Posicion electrodo A
    [4.55, 0.55],   #Posicion electrodo B
    [8.55, 0.55],   #Posicion electrodo C
    [0.55, 4.55],   #Posicion electrodo D
    [8.55, 4.55],   #Posicion electrodo E
    [0.55, 8.55],   #Posicion electrodo F
    [4.55, 8.55],   #Posicion electrodo G
    [8.55, 8.55],   #Posicion electrodo H
])


m=np.zeros((1,Electrodos))
V=np.zeros((1,Electrodos))
i=0
t=0
while t<=np.count_nonzero(X):
    while i<=E:

        m[i][0]=raiz((X-(P[i][0]))**2+(Y-(P[i][1]))**2)
        V[i][0]=ln((l+raiz(m[i][0]**2+l**2))/m[i][0])
        i += 1

print (V)
print (E)
"""

ma=raiz((X-ax)**2+(Y-ay)**2)
mb=raiz((X-bx)**2+(Y-by)**2)
mc=raiz((X-cx)**2+(Y-cy)**2)
md=raiz((X-dx)**2+(Y-dy)**2)
me=raiz((X-ex)**2+(Y-ey)**2)
mf=raiz((X-fx)**2+(Y-fy)**2)
mg=raiz((X-gx)**2+(Y-gy)**2)
mh=raiz((X-hx)**2+(Y-hy)**2)

va=ln((l+raiz(ma**2+l**2))/ma)
vb=ln((l+raiz(mb**2+l**2))/mb)
vc=ln((l+raiz(mc**2+l**2))/mc)
vd=ln((l+raiz(md**2+l**2))/md)
ve=ln((l+raiz(me**2+l**2))/me)
vf=ln((l+raiz(mf**2+l**2))/mf)
vg=ln((l+raiz(mg**2+l**2))/mg)
vh=ln((l+raiz(mh**2+l**2))/mh)

Vt=((rho*ik)/(2*np.pi))*(va+vb+vc+vd+ve+vf+vg+vh)
print (Vt[::].max())
#print(Vt)
x = X.flatten()
y = Y.flatten()
z = Vt.flatten()

surf = axx.plot_surface(X, Y, Vt, cmap = cm.coolwarm, linewidth=0, antialiased=False)

# Customize the z axis.
axx.set_zlim(300, 3000)
axx.zaxis.set_major_locator(LinearLocator(10))
axx.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
"""