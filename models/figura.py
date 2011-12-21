# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------------------------------------------------------------------------#
#
#-----------------------------------------------------------------------------------------------------------------------------------------------#
from matplotlib.figure import Figure #Clase para contener las gráficas
from mpl_toolkits.mplot3d.axes3d import Axes3D #Clase para trabajar con gráficas 3d
import matplotlib#Quitar luego, solo está para propósitos de generar los ejemplos
import matplotlib.mlab as mlab#Quitar luego, solo está para propósitos de generar los ejemplos
from matplotlib import cm#Para los colores de la gráfica 3d
import numpy as np

class figura():

    def __init__(self, matrix = None, selected = None, parent = None):

        fig = Figure(figsize = (1.8 * 4, 2.4 * 4))
        self.axu = fig.add_subplot(2, 2, 1)
        self.axd = fig.add_subplot(2, 2, 2)
        self.axt = fig.add_subplot(2, 2, 3, projection = '3d')
        self.axc = fig.add_subplot(2, 2, 4)
        fig.subplots_adjust(hspace=.2, wspace=.3, bottom=.07, left=.08, right=.92, top=.94)
        self.fig = fig

    def plotU(self):#Tengo que ver como voy a hacer para igualar el tamaño de los arreglos para x e y

        ax = self.axu
        x = np.arange(0, 10, .05)#Descensos (h), son números que representan el nivel piezométrico
        y = np.arange(0, 10, .05)#Tiempos (t), se supone está en días
        ax.set_title('Descensos h en tiempo t')
        ax.set_xlabel('h')
        ax.set_ylabel('t')
        ax.plot(x,y)
        print 'First plot loaded...'

    def plotD(self):#Tengo que ver como voy a hacer para igualar el tamaño de los arreglos para los tres ejes

        print 'Loading second plot...'
        matplotlib.rcParams['xtick.direction'] = 'out'
        matplotlib.rcParams['ytick.direction'] = 'out'

        delta = 0.025
        x = np.arange(-3.0, 3.0, delta)
        y = np.arange(-2.0, 2.0, delta)
        X, Y = np.meshgrid(x, y)
        Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
        Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
        # difference of Gaussians
        Z = 10.0 * (Z2 - Z1)

        # Create a simple contour plot with labels using default colors.  The
        # inline argument to clabel will control whether the labels are draw
        # over the line segments of the contour, removing the lines beneath
        # the label
        ax = self.axd
        #CS = contour(X, Y, Z)
        ax.contour(X, Y, Z)
        #clabel(CS, inline=1, fontsize=10)
        ax.set_title('Propagacion')
        print 'Second plot loaded...'

    def plotT(self):#Tengo que ver como voy a hacer para igualar el tamaño de los arreglos para los tres ejes

        #add_subplot(filas, columnas, numero de grafica/posicion, tipo de grafica)
        print 'Loading third plot...'
        ax = self.axt
        #X = np.arange(-5, 5, 0.25)
        #Y = np.arange(-5, 5, 0.25)
        X = np.arange(0, 20)
        Y = np.arange(0, 20)
        X, Y = np.meshgrid(X, Y)
        print '\n' + str(X) + '\n' + str(Y) + '\n'
        #R = np.sqrt(X**2 + Y**2)
        #Z = np.sin(R)
        #Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
        #Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
        #Z = 10.0 * (Z2 - Z1)
        #print 'Z: \n' + str(Z)
        #Esto de abajo tiene volar una vez definidas correctamente las matrices
        Z = [[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
            ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
            ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
            ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
            ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
            ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
            ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
            ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
            ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 9.9997, 9.9977, 9.9977, 9.9997, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
            ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 9.9977, 9.9668, 9.9668, 9.9977, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
            ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 9.9977, 9.9668, 9.9668, 9.9977, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
            ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 9.9997, 9.9977, 9.9977, 9.9997, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
            ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
            ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
            ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
            ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
            ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
            ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
            ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
            ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]]
        print 'Z: \n' + str(Z)
        ax.set_zlim3d(-20, 20)
        surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet,
        linewidth=0, antialiased=True)
        ax.set_zlim3d(9.5, 10)# viewrange for z-axis should be [-4,4]
        ax.set_ylim3d(0, 20)# viewrange for y-axis should be [-2,2]
        ax.set_xlim3d(0, 20)
        ax.set_title('Representacion 3d')
        print 'Third plot loaded...'
#            fig.colorbar(surf, shrink=0.5, aspect=10)

    def plotC(self):

        print 'Loading fourth plot...'
        ax = self.axc
        #x = np.linspace(0,10,11)
        #y = np.linspace(0,15,16)
        x = np.arange(0, 10, 0.5)
        y = np.arange(-2, 2, 0.5)
        (X,Y) = np.meshgrid(x,y)
        u = 5*X
        v = 5*Y
        q = ax.quiver(X, Y, u, v, angles='xy', scale=1000, color=['r'])
        p = ax.quiverkey(q,1,16.5,50,"50 m/s",coordinates='data',color='r')
        ax.set_title('Velocidad')
        print 'Fourth plot loaded...'
        #xl = ax.xlabel("x (km)")
        #yl = ax.ylabel("y (km)")