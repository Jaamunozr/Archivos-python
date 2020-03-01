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
 
Xa = np.arange(-10, 10, 1)
Ya = np.arange(-10, 10, 1)
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
            m[i][0] =raiz((((P[i][0])-X)**2)+(((P[i][1])-Y)**2))
            o,u=((P[i][0])-X),((P[i][1])-Y)
            if (o ==0) and (u==0):
                #print ("hola mundo")
                print("matriz",k,t, "x,y",P[i][0],P[i][1],"punto de eje",X,Y )
                #m[i][0]=0.01
            V[i][0] =ln((l+raiz((m[i][0])**2+l**2))/(m[i][0]))
            i += 1
        Vt[k][t]=np.sum(V)
        t +=1
    k +=1
Vtt=(Vt*(rho*ik))/(2*np.pi*l)
print("Numero de elementos por eje:")
print (np.count_nonzero(Xa))
print ("Valor máximo")
print (Vtt[::].max())
print ("Numero de elemmentos de Vt")
print (np.count_nonzero(Vtt))
print ("lementos de Xa al cuadrado")
print (np.count_nonzero(Xa)**2)

