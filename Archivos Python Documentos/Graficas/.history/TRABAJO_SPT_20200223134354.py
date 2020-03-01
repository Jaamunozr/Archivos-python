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
 
Xa = np.arange(-10, 10, 0.1)
Ya = np.arange(-10, 10, 0.1)
l = 2
rho= 100
ik=25
Electrodos=8
E=Electrodos-1

P=np.array([
    [-4, -4],   #Posicion electrodo A
    [0, -4],   #Posicion electrodo B
    [4, -4],   #Posicion electrodo C
    [-4, 0],   #Posicion electrodo D
    [4, 0],   #Posicion electrodo E
    [-4, 4],   #Posicion electrodo F
    [0, 4],   #Posicion electrodo G
    [4, 4]    #Posicion electrodo H
])

Vt=np.zeros((np.count_nonzero(Xa),np.count_nonzero(Ya)))
m=np.zeros((Electrodos,1))
V=np.zeros((Electrodos,1))
k=0

while k<np.count_nonzero(Ya):
    Y=Ya[k]
    t=0
    while t<np.count_nonzero(Xa):
        X=Xa[t]
        i=0
        while i<=E:
            m[i][0] =round(raiz((((P[i][0])-X)**2)+(((P[i][1])-Y)**2)),4)
            o,u=((P[i][0])-X),((P[i][1])-Y)
            if ((o ==0) and (u==0)) or (m[i][0]==0):
                #print("Elementos de matriz",k,t, "x,y",P[i][0],P[i][1],"punto de eje",X,Y )
                m[i][0]=0.01
            V[i][0] =ln((l+raiz((m[i][0])**2+l**2))/(m[i][0]))
            i += 1
        Vt[k][t]=np.sum(V)
        t +=1
    k +=1
Vtt=(Vt*(rho*ik))/(2*np.pi*l)
print ("Número de elementos por eje:" , np.count_nonzero(Xa))
print ("Valor máximo de tensión: ", round(Vtt[::].max(),3), "[V]")
print ("Valor mínimo de tensión: ", round(Vtt[::].min(),3), "[V]")
print ("Número de elemmentos de Vt: ", np.count_nonzero(Vtt))
print ("Elementos de Xa al cuadrado: ", np.count_nonzero(Xa)**2)
Xa, Ya = np.meshgrid(Xa, Ya)
print ("Nuevo número de elemmentos de Xa y Ya:", np.count_nonzero(Xa))
#x = X.flatten()
#y = Y.flatten()
#z = Vtt.flatten()

#colors = cmap(a / b)

surf = axx.plot_surface(Xa, Ya, Vtt, cmap = cm.get_cmap("Spectral"), linewidth=0, antialiased=False)

# Customize the z axis.
axx.set_zlim(300, 1800)
axx.zaxis.set_major_locator(LinearLocator(10))
axx.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()