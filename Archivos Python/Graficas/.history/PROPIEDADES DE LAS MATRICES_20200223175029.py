import numpy as np
import os
import pylab as pl
import matplotlib.pyplot as plt
os.system("clear")


g=np.array([
    [1.3444444, 2], #hola mundo
    [3, 4],
    [5, 6]
])
#g[0][1]=1+g[0][1]
#g= np.count_nonzero(g)
m=np.zeros((5,8))
m=round(3*0.444444573, 2)

print (round(np.sum(g),3))
print(m)

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

from mpl_toolkits.mplot3d.axes3d import get_test_data
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


# set up a figure twice as wide as it is tall
fig = plt.figure(figsize=plt.figaspect(0.5))

#===============
#  First subplot
#===============
# set up the axes for the first plot
ax = fig.add_subplot(1, 2, 1, projection='3d')

# plot a 3D surface like in the example mplot3d/surface3d_demo
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)
fig.colorbar(surf, shrink=0.5, aspect=10)

#===============
# Second subplot
#===============
# set up the axes for the second plot
ax = fig.add_subplot(1, 2, 2, projection='3d')

# plot a 3D wireframe like in the example mplot3d/wire3d_demo
X, Y, Z = get_test_data(0.05)
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()









"""

raiz=np.sqrt
ln=np.log

X = np.arange(-2, 12, 0.1)
Y = np.arange(-2, 12, 0.1)

J=np.count_nonzero(Y)
print (J)

a = [0] * J
for i in range(J):
    a[i] = Y[i]
X[25]=0.49
X[65]=4.49
X[105]=8.49
Y[25]=0.49
Y[65]=4.49
Y[105]=8.49


ax, ay = 0.5, 0.5
bx, by = 4.5, 0.4
cx, cy = 8.5, 0.5
dx, dy = 0.5, 4.5
ex, ey = 8.5, 4.5
fx, fy = 0.5, 8.5
gx, gy = 4.5, 8.5
hx, hy = 8.5, 8.5
l = 2
rho= 100
ik=25

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

print(type(Vt))
print(Vt.shape)

plt.figure(figsize=(X,Y))
plt.imshow(Vt, cmap = "summer")
plt.colorbar(
    plt.show()
)"""