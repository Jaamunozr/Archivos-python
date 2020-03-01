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

#------------------------------------------------------------------------------ 

Xa = np.arange(-10, 10, 0.1)   #Rango de coordenadas de X 
Ya = np.arange(-10, 10, 0.1)   #Rango de coordenadas de Y
l = 2                          #Longitud del electrodo [m]
rho= 100                       #Resistividad de terrreno [Ohm/m]
Ik=200                         #Corriente de falla [A] (Total)
Rad=0.01                       #Radio del electrodo [m]
Electrodos=8                   #Número de electrodos

#Posición de los electrodos 

P=np.array([
    [-4,-4],   #Electrodo A
    [0,-4],   #Electrodo B
    [4,-4],   #Electrodo C
    [-4,0],   #Electrodo D
    [4,0],   #Electrodo E
    [-4,4],   #Electrodo F
    [0,4],   #Electrodo G
    [4,4]    #Electrodo H
])
#------------------------------------------------------------------------------ 


E=Electrodos-1
ik=Ik/Electrodos
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
                m[i][0]=Rad
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
print(np.where(max.all(Vtt) == Vtt))


print ("Elementos de Xa al cuadrado: ", np.count_nonzero(Xa)**2)
X, Y = np.meshgrid(Xa, Ya)
print ("Nuevo número de elementos de X y Y:", np.count_nonzero(Xa))

surf = axx.plot_surface(X, Y, Vtt, cmap = cm.get_cmap("Spectral"), linewidth=0, antialiased=False)

# Customize the z axis.
axx.set_zlim(300, 1800)
axx.zaxis.set_major_locator(LinearLocator(10))
axx.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()