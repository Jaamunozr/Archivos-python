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
 
Xa = np.arange(0, 14, 0.1)
Ya = np.arange(0, 14, 0.1)
#X, Y = np.meshgrid(X, Y)
print (np.count_nonzero(Xa))
l = 2
rho= 100
ik=25
Electrodos=8
E=Electrodos-1

P=np.array([
    [0, 0],   #Posicion electrodo A
    [4, 0],   #Posicion electrodo B
    [8, 0],   #Posicion electrodo C
    [0, 4],   #Posicion electrodo D
    [8, 4],   #Posicion electrodo E
    [0, 8],   #Posicion electrodo F
    [4, 8],   #Posicion electrodo G
    [8, 8]    #Posicion electrodo H
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
            m[i][0] =raiz(((X-(P[i][0]))**2)+((Y-(P[i][1]))**2))
            """o,u=(X-(P[i][0])),(Y-(P[i][1]))
            if (o ==0) or (u==0):
                print ("hola mundo")   """          
            if k==0 and t==0:
                print(m[i][0])
                #print(P[i][1])
            V[i][0] =ln((l+raiz((m[i][0])**2+l**2))/(m[i][0]))
            i += 1
        Vt[k][t]=np.sum(V)
        t +=1
    k +=1
Vtt=(Vt*(rho*ik))/(2*np.pi)
#print (Vt)


print("Vt max")
print (Vtt[::].max())
print (np.count_nonzero(Xa))
#Xa, Ya = np.meshgrid(Xa, Ya, sparse = False)
X=np.zeros((np.count_nonzero(Xa),1))
Y=np.zeros((np.count_nonzero(Ya),1))
pos=1
print (P)
while pos<np.count_nonzero(Xa):
    np.concatenate(X, axis=0)
    
    #X[pos][0]=Xa
    #Y[pos][0]=Ya
    pos +=1

#print(Vt)
x = X.flatten()
y = Y.flatten()
z = Vtt.flatten()
print("Ya")
print((Y))
print("Xa")
#print(np.count_nonzero(X))
print("Vt")
print(np.count_nonzero(Vtt))


#colors = cmap(a / b)

surf = axx.plot_surface(X, Y, Vtt, cmap = cm.get_cmap("Spectral"), linewidth=0, antialiased=False)

# Customize the z axis.
axx.set_zlim(300, 3000)
axx.zaxis.set_major_locator(LinearLocator(10))
axx.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
