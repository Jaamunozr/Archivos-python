import os
import pylab as pl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
#------------------------------------------------------------------------------ 
os.system("clear")
fig = pl.figure()
axx = Axes3D(fig)
raiz=np.sqrt
ln=np.log
puntoX=float(0)
puntoY=float(0)
#puntoX=float(input("Seleccione la coordenada en X donde desea calcular el potencial: "))
#puntoY=float(input("Seleccione la coordenada en Y donde desea calcular el potencial: "))
print("Calculando ...")

#------------------------------------------------------------------------------ 

Xa = np.arange(-10, 10, 0.1)   #Rango de coordenadas de X 
Ya = np.arange(-10, 10, 0.1)   #Rango de coordenadas de Y
l = 2                          #Longitud del electrodo [m]
rho= 100                       #Resistividad de terrreno [Ohm/m]
Ik=200                         #Corriente de falla [A] (Total)
Rad=0.01                       #Radio del electrodo [m]
Electrodos=8                   #Número de electrodos
Pos1=4                         #Posición 1 en Y para analisis de grafica 2D
Pos2=0                         #Posición 2 en Y para analisis de grafica 2D

#------------------------------------------------------------------------------ 
#Posición de los electrodos 
#------------------------------------------------------------------------------ 
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
m2=np.zeros((Electrodos,1))
V2=np.zeros((Electrodos,1))

#------------------------------------------------------------------------------ 
#Cálculo del punto ingresado
#------------------------------------------------------------------------------ 

i=0
while i<=E:
    m2[i][0] =round(raiz((((P[i][0])-puntoX)**2)+(((P[i][1])-puntoY)**2)),4)
    o,u=((P[i][0])-puntoX),((P[i][1])-puntoY)
    if ((o ==0) and (u==0)) or (m2[i][0]==0):
    #print("Elementos de matriz",k,t, "x,y",P[i][0],P[i][1],"punto de eje",X,Y )
        m2[i][0]=Rad
    V2[i][0] =ln((l+raiz((m2[i][0])**2+l**2))/(m2[i][0]))
    i += 1
Vt2=(np.sum(V2)*(rho*ik))/(2*np.pi*l)

print("El potencial en el punto (",puntoX,",",puntoY,"), es de",round(Vt2,3),"[V]")
#------------------------------------------------------------------------------ 
#Cálculo de la malla
#------------------------------------------------------------------------------ 

Vxy = [1] * (np.count_nonzero(Ya))

while k<np.count_nonzero(Ya):
    Y=round(Ya[k],3)
    t=0
    while t<np.count_nonzero(Xa):
        X=round(Xa[t],3)
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
        if Y==Pos1:
            Vxa=Vt[k]
        if Y==Pos2:
            Vxb=Vt[k]
        if (Y==X) and ((X-Y)==0):
            Vxy[k]=Vt[k][t]*(rho*ik)/(2*np.pi*l)
        t +=1
    k +=1

Vtt=(Vt*(rho*ik))/(2*np.pi*l)
Vxa=(Vxa*(rho*ik))/(2*np.pi*l)
Vxb=(Vxb*(rho*ik))/(2*np.pi*l)
aa=np.where(np.amax(Vtt) == Vtt)
print ("Valor máximo de tensión (GPR):",round(Vtt[::].max(),3),"[V], en posición: (",round(Xa[aa[0][0]],2),",",round(Ya[aa[1][0]],2),")")
bb=np.where(np.amin(Vtt) == Vtt)
print("Valor de Resistencia de puesta a tierra:", (round(Vtt[::].max(),3)/Ik), "[Ohm]")
#print ("Valor mínimo de tensión:",round(Vtt[::].min(),3),"[V], en posición: (",round(Xa[bb[0][0]],2),",",round(Ya[bb[1][0]],2),")")
print ("Número de elementos de Vt:",np.count_nonzero(Vtt))
X, Y = np.meshgrid(Xa, Ya)

#------------------------------------------------------------------------------ 
# GRAFICAS 3D
#------------------------------------------------------------------------------ 
# Configurar una figura dos veces más alta que ancha
#fig = plt.figure(figsize=plt.figaspect(0.2))



fig.suptitle('Potencial')
#  Primera imagen a imprimir
ax = fig.add_subplot(2, 2, 1, projection='3d')
fig = plt.figure(4,figsize=(6,4.5)) #(Ancho, alto)
surf = ax.plot_surface(X, Y, Vtt, cmap = cm.get_cmap("jet"))#, antialiased=False)
ax.set_zlim(300, 1800)
fig.colorbar(surf)

#------------------------------------------------------------------------------ 
#Graficas en 2D
#------------------------------------------------------------------------------ 
x1=Xa

ax = fig.add_subplot(2, 2, 2)
ax.title.set_text('Eje X1 vs V')
ax.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
ax.plot(x1, Vxa, color="blue", linewidth=1.0, linestyle="-")

ax = fig.add_subplot(2, 2, 3)
ax.title.set_text('Eje X2 vs V')
ax.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
ax.plot(x1, Vxb, color="red", linewidth=1.0, linestyle="-")

ax = fig.add_subplot(2, 2, 4)
ax.title.set_text('Eje X,Y vs V')
ax.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
ax.plot(x1, Vxy, color="green", linewidth=1.0, linestyle="-")


plt.pause(25)
pl.savefig('tierras.pdf')
