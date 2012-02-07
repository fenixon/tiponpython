import sys
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pylab as p
import mpl_toolkits.mplot3d.axes3d as p3


nix=3
niy=3;

nix=nix+1;
niy=niy+1;

xx = np.linspace(0,3,nix);
yy = np.linspace(3,0,niy);
X, Y = np.meshgrid(xx, yy) 

print X
print Y


h0=np.zeros((niy,nix), float);




for i in range(0,nix):
    for j in range (0,niy):
        #la matriz a generar se indexa primero en el eje y y dps en el x
        h0[j,i]=10.0;

##h0[1,1]=3

fig=p.figure()
#fig = plt.figure()
print h0

ax = p3.Axes3D(fig)

#ax.plot_surface(x,y,z)
##surf = ax.plot_surface(X, Y, h0)

ax.contour(X, Y, h0)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
p.show()

#ax = fig.add_subplot(111, projection='3d')


#ax.show()


    


