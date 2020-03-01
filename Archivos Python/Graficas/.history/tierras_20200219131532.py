import os
import pylab as pl
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
os.system("clear")

fig = pl.figure()
axx = Axes3D(fig)
raiz=np.sqrt
ln=np.log

X = np.arange(0, 10, 0.25)
Y = np.arange(0, 10, 0.25)
X, Y = np.meshgrid(X, Y)

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


axx.plot_surface(X, Y, Vt, rstride=1, cstride=1, alpha=0.3)# cmap=pl.cm.Pastel1)
#axx.contourf(X, Y, Vt, zdir='Vt', offset=450, cmap=pl.cm.hot)
axx.set_zlim(500, 2000)
pl.show()