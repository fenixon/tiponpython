import sys
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import pylab as p
import mpl_toolkits.mplot3d.axes3d as p3
from mpl_toolkits.mplot3d.art3d import Poly3DCollection



def update_line(num, data, line):
    line.set_data(data[...,:num])
    return line

nix=5
niy=10;

nix=nix+1;
niy=niy+1;

xx = np.linspace(0,5,nix);
yy = np.linspace(10,0,niy);
f = np.linspace(5,1,10);
X, Y = np.meshgrid(xx, yy) 

##print xx
##print yy

h0=np.zeros((niy,nix), float);

for i in range(0,nix):
    for j in range (0,niy):
        #la matriz a generar se indexa primero en el eje y y dps en el x
        h0[j,i]=yy[j];


print h0

fig=p.figure()
#fig = plt.figure()

ax = p3.Axes3D(fig)
##h0[1,1]=1

##graf1 = p.subplot(111)
##graf1.

##ax.plot_surface(x,y,z)
surf = ax.plot_surface(X, Y, h0)

##surf.set_verts(h0)

print surf

#j=np.meshgrid(X,Y)
#b=np.meshgrid(j,h0)

##print surf
a = np.array( [2,3,4] )

data = np.random.rand(2, 25)

####line_ani = animation.FuncAnimation(fig, update_line, 25, fargs=(data, surf),
##    interval=50, blit=True)

##k = p.pcolor(X,Y,h0[0])

##for i in range(1,len(h0)):
##  k.set_array(h0[i,0:-1,0:-1].ravel())
##  k.autoscale()
##  p.draw()


#ax.axes.set_rasterization_zorder(4)


#print yy

#ax.contour(X,Y,h0)
#surf.set_array(f)

k=Poly3DCollection()

ax.cla()
ax.add_collection3d(surf)


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
p.show()

#ax = fig.add_subplot(111, projection='3d')
#ax.show()


    


