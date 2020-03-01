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
 
Xa = np.arange(-2, 12, 1)
Ya = np.arange(-2, 12, 1)
#X, Y = np.meshgrid(X, Y)
print (np.count_nonzero(Xa))
l = 2
rho= 100
ik=25
Electrodos=8
E=Electrodos-1

P=np.array([
    [0.5, 0.5],   #Posicion electrodo A
    [4.5, 0.5],   #Posicion electrodo B
    [8.5, 0.5],   #Posicion electrodo C
    [0.5, 4.5],   #Posicion electrodo D
    [8.5, 4.5],   #Posicion electrodo E
    [0.5, 8.5],   #Posicion electrodo F
    [4.5, 8.5],   #Posicion electrodo G
    [8.5, 8.5]    #Posicion electrodo H
])

Vt=np.zeros((np.count_nonzero(Xa),np.count_nonzero(Ya)))
m=np.zeros((Electrodos,1))
V=np.zeros((Electrodos,1))
t=0
while t<np.count_nonzero(Xa):
    X=Xa[t]
    Y=Ya[t]
    i=0
    while i<=E:

        m[i][0] =raiz((X-(P[i][0]))**2+(Y-(P[i][1]))**2)
        LL=X-(P[i][0]
        if LL== 0:
            print(m[i][0])
        else:
            pass
        V[i][0] =ln((l+raiz((m[i][0])**2+l**2))/(m[i][0]))
        i += 1
    Vt[t][t]=np.sum(V)
    t +=1

Vt=Vt*(rho*ik)/(2*np.pi)
print (V)
print (Vt)
print (Vt[::].max())
"""
Vt=((rho*ik)/(2*np.pi))*(va+vb+vc+vd+ve+vf+vg+vh)
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