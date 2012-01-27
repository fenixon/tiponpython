import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
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


#fig = plt.figure(figsize = (1.8 * 4, 2.4 * 4))
#Figure(figsize = (1.8 * 4, 2.4 * 4))
#axu = fig.add_subplot(2, 2, 1)
#axd = fig.add_subplot(2, 2, 2)
#axt = fig.add_subplot(2, 2, 3, projection = '3d')
#axc = fig.add_subplot(2, 2, 4)
#fig.subplots_adjust(hspace=.2, wspace=.3, bottom=.07, left=.08, right=.92, top=.94)
#axt.set_ylim3d(0,10)
#axt.set_xlim3d(0,5)
#axt.set_zlim3d(-10,10)

#fig2 = Figure(figsize = (0.5, 0.5))
fig = plt.figure(figsize = (1.8 * 4, 2.4 * 4))
#Figure(figsize = (1.8 * 4, 2.4 * 4))
axu = fig.add_subplot(2, 2, 1)
axd = fig.add_subplot(2, 2, 2)
axt = fig.add_subplot(2, 2, 3, projection = '3d')
axc = fig.add_subplot(2, 2, 4)
fig.subplots_adjust(hspace=.2, wspace=.3, bottom=.07, left=.08, right=.92, top=.94)
axt.set_ylim3d(0,10)
axt.set_xlim3d(0,5)
axt.set_zlim3d(-10,10)

#axt2 = Axes3D(fig2) 
#ax = axt
##ax = p3.Axes3D(fig)
superficies=[]
##h0[1,1]=1
#ax.plot_surface(x,y,z)


#ax.contour(X,Y,h0)

data = np.random.rand(2, 25)

##EL DRAW VA POR PARTE DE LA ANIMACION
#canvas = FigureCanvas(fig)
#canvas.draw()

##p.show()

##axt.cla() 
##axt.add_collection3d(superficies[0])

##axt.cla() 
##axt.add_collection3d(superficies[1])


ims = []
#for add in np.arange(15):
##    'Poly3DCollection' object is not iterable
#    ims.append([axt.add_collection3d(superficies[add])])


surf = axt.plot_surface(X, Y, h0)
ims.append([surf])
surf2 = axt.plot_surface(X, Y, h1)
ims.append([surf2])

  
im_ani = animation.ArtistAnimation(fig, ims, interval=0.1, repeat_delay=0,
    blit=True)
#im_ani.save('im.mp4')
  
p.show()


#canvas.show()

#plt.show()






#ax = fig.add_subplot(111, projection='3d')
#ax.show()



    


