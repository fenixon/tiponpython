import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import pylab as p
import mpl_toolkits.mplot3d.axes3d as p3

nix=5
niy=10;

nix=nix+1;
niy=niy+1;

xx = np.linspace(0,5,nix);
yy = np.linspace(10,0,niy);
f = np.linspace(5,1,10);
X, Y = np.meshgrid(xx, yy) 

print xx
print yy

h0=np.zeros((niy,nix), float);
h1=np.zeros((niy,nix), float);
print h0

for i in range(0,nix):
    for j in range (0,niy):
        #la matriz a generar se indexa primero en el eje y y dps en el x
        h0[j,i]=yy[j];
        h1[j,i]=yy[j]*(-1);

fig = plt.figure(figsize = (1.8 * 1, 2.4 * 1))
axt = fig.add_subplot(1, 1,1)
##fig.subplots_adjust(hspace=.2, wspace=.3, bottom=.07, left=.08, right=.92, top=.94)
##axt.set_ylim3d(0,10)
##axt.set_xlim3d(0,5)
##axt.set_zlim3d(-10,10)

superficies=[]
data = np.random.rand(2, 25)



##axt.cla() 
axt = plt.contour(X, Y, h0)

##EL DRAW VA POR PARTE DE LA ANIMACION
canvas = FigureCanvas(fig)
canvas.draw()

p.show()





    


