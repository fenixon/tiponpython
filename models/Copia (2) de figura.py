# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------------------------------------------------------------------------#
#Acá se van a calcular las gráficas
#-----------------------------------------------------------------------------------------------------------------------------------------------#
from matplotlib.figure import Figure #Clase para contener las gráficas
from mpl_toolkits.mplot3d.axes3d import Axes3D #Clase para trabajar con gráficas 3d
import matplotlib#Quitar luego, solo está para propósitos de generar los ejemplos
import matplotlib.mlab as mlab#Quitar luego, solo está para propósitos de generar los ejemplos
from matplotlib import cm#Para los colores de la gráfica 3d
import numpy as np
import pylab as p
import matplotlib.pyplot as plt
import random
import subprocess
import os

class figura():

    def __init__(self, matrix, matx, maty, dominio, observaciones, bombeos, X, Y, xx, yy, tiempos, superficies, selected = None, parent = None):

        fig = Figure(figsize = (1.8 * 4, 2.4 * 4))
        self.axu = fig.add_subplot(2, 2, 1)
        self.axd = fig.add_subplot(2, 2, 2)
        self.axt = fig.add_subplot(2, 2, 3, projection = '3d')
        self.axc = fig.add_subplot(2, 2, 4)
        fig.subplots_adjust(hspace=.2, wspace=.3, bottom=.07, left=.08, right=.92, top=.94)

        self.axt.set_ylim3d(0,1000)
        self.axt.set_xlim3d(0,1000)
        self.axt.set_zlim3d(9.3, 10)

        self.fig = fig
        self.matrix = matrix
        self.dominio=dominio
        self.observaciones=observaciones
        self.bombeos=bombeos
        self.X=X
        self.Y=Y
        self.matx = matx
        self.maty = maty
        self.xx = xx
        self.yy = yy
        self.tiempos = tiempos
        self.superficies=superficies

    def plotU(self, ran):#Tengo que ver como voy a hacer para igualar el tamaño de los arreglos para x e y

        ax = self.axu
        ax.cla()
        #x = np.arange(0, ran, .05)
        #print 'Aleatorio: ' + str(ran)
        #x = np.arange(0, 10, .05)#Descensos (h), son números que representan el nivel piezométrico
        #y = np.arange(0, 10, .05)#Tiempos (t), se supone están en días
        #y = np.sin(x) + ran*2

        pozoObs = self.dominio.obtenerPozoObservacion()

        auxtx = [i for i,x in enumerate(self.xx) if x == pozoObs.x]
        auxty = [i for i,x in enumerate(self.yy) if x == pozoObs.y]

        h = self.matrix[:, auxty[0], auxtx[0]]

        t = self.tiempos
    
        x=[]
        y=[]
        for ob in self.observaciones:
            x.append(ob.tiempo)
            y.append(ob.nivelpiezometrico)
        
        ax.set_title('Descensos h en tiempo t')
        ax.set_xlabel('t')
        ax.set_ylabel('h')
        ax.plot(t, h, 'b')
        ax.plot(x,y, 'r.')
        #print 'First plot loaded...'

    def plotD(self, ran, t):#Tengo que ver como voy a hacer para igualar el tamaño de los arreglos para los tres ejes

        #print 'Loading second plot...'
        matplotlib.rcParams['xtick.direction'] = 'out'
        matplotlib.rcParams['ytick.direction'] = 'out'

        

        delta = 0.025
        #x = np.arange(-3.00, 3.00, delta)
        #y = np.arange(-2.00, 2.00, delta)
        #x = np.arange(0, self.dominio.ancho+1)
        #y = np.arange(0, self.dominio.alto+1)
        #X, Y = np.meshgrid(x, y)
        #Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
        #Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
        #difference of Gaussians
        #Z = 10.0 * (Z2 - Z1)

##        print 'tiempo: '+str(t)
        Z = self.matrix[t]

##        print 'tamano z '+str(len(Z))
##        print 'tamano x '+str(len(self.X))
##        print 'tamano y '+str(len(self.Y))

##        print 'X: \n'+ str(self.X)
##        print 'Y: \n'+ str(self.Y)
##        print 'Z: \n'+ str(Z)

##        print 'tam '+str(len(self.Y))

        divi=np.zeros((len(self.Y),len(self.X)), float)
        divi[:,:]=Z[0,0]
        #BUG DE MATPLOTLIB: se grafica solo si la matriz no es multiplo de ones, no hay una curva de nivel
        if not p.all(np.equal(Z,divi)):

            # Create a simple contour plot with labels using default colors.  The
            # inline argument to clabel will control whether the labels are draw
            # over the line segments of the contour, removing the lines beneath
            # the label
            ax = self.axd
            ax.cla()
            #CS = contour(X, Y, Z)
            ax.contour(self.X, self.Y, Z)
            #clabel(CS, inline=1, fontsize=10)
            ax.set_title(u'Propagación')
    ##        print 'Second plot loaded...'

    def plotT(self, ran, t):#Tengo que ver como voy a hacer para igualar el tamaño de los arreglos para los tres ejes

        #add_subplot(filas, columnas, número de gráfica/posición, tipo de gráfica)
##        print 'Loading third plot...'
        ax = self.axt
        ax.cla()
        #X = np.arange(-5, 5, 0.25)
        #Y = np.arange(-5, 5, 0.25)

        
##      La matriz tiene que ir hasta el 0..99 En realidad de 0 a 100
##      Esta lina no estaba funcionando  
##      X, Y = np.meshgrid(np.arange(0, max(X), 1), np.arange(0, max(Y), 1))
        #X, Y = np.meshgrid(xx, Y)       
        #print '\n' + str(X) + '\n' + str(Y) + '\n'
        #R = np.sqrt(X**2 + Y**2)
        #Z = np.sin(R)
        #Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
        #Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
        #Z = 10.0 * (Z2 - Z1)
        #print 'Z: \n' + str(Z)
        #Esto de abajo va a volar una vez definidas correctamente las matrices
        #Z = [[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
        #    ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
        #    ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
        #    ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
        #    ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
        #    ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
        #    ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
        #    ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
        #    ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 9.9997, 9.9977, 9.9977, 9.9997, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
        #    ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 9.9977, 9.9668, 9.9668, 9.9977, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
        #    ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 9.9977, 9.9668, 9.9668, 9.9977, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
        #    ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 9.9997, 9.9977, 9.9977, 9.9997, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
        #    ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
        #    ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
        #    ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
        #    ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
        #    ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
        #    ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
        #    ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]
        #    ,[10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000, 10.0000]]


        ##Como dijo Alvarito esto va a volar cuando... Esta de la matriz que llega tomar el tiempo 1 y graficar eso     
##        Z = self.matrix[t]      

##        print 'Matriz generada '
##        print 'Z: \n' + str(Z)

##        auxt = [i for i,x in enumerate(self.tiempos) if x == t]
##        print t
##        print self.superficies[t]

        ax.add_collection3d(self.superficies[t])


##        fig2 = plt.figure(figsize = (1.8 * 4, 2.4 * 4))
##        axu2 = fig2.add_subplot(2, 2, 1)
##        axd2 = fig2.add_subplot(2, 2, 2)
##        axt2 = fig2.add_subplot(2, 2, 3, projection = '3d')
##        axc2 = fig2.add_subplot(2, 2, 4)
##        fig2.subplots_adjust(hspace=.2, wspace=.3, bottom=.07, left=.08, right=.92, top=.94)
##        axt2.cla()
        ##h0[1,1]=1
        #ax.plot_surface(x,y,z)
##        surf = axt2.add_collection3d(self.superficies[t])

##        canvas = FigureCanvas(fig2)
##        canvas.draw() 
        
##        p.show()

##        surf = ax.plot_surface(self.X, self.Y, Z, rstride=1, cstride=1, cmap=cm.jet,linewidth=0, antialiased=False)

###     comente lo de los limites porque hay que setearlos segun como venga el dominio
##      Esto tiene que cambiar segun los valores maximos y minimos de Z                 
##        ax.set_zlim3d(9.3, 10)
        #ax.set_zlim3d(-100, 100)# viewrange for z-axis should be [-4,4]
##        ax.set_ylim3d(0, 20)# viewrange for y-axis should be [-2,2]
##        ax.set_xlim3d(0, 20)
        ax.set_title(u'Representación 3d')
##        print 'Third plot loaded...'
#            fig.colorbar(surf, shrink=0.5, aspect=10)

    def plotC(self, ran, t):

##        print 'Loading fourth plot...'
        ax = self.axc
        ax.cla()
        #x = np.linspace(0,10,11)
        #y = np.linspace(0,15,16)
        #x = np.arange(0, 10, 0.5)
        #y = np.arange(-2, 2, 0.5)
        #(X,Y) = np.meshgrid(x,y)
        #u = 5*X
        #v = 5*Y
        X = self.X
        Y = self.Y
        u = self.matx[t]
        v = self.maty[t]*-1
        q = ax.quiver(X, Y, u, v, color=['r'])
        #p2 = ax.quiverkey(q,1,16.5,50,"50 m/s",coordinates='data',color='r')
        ax.set_title('Velocidad')
##        print 'Fourth plot loaded...'
        #xl = ax.xlabel("x (km)")
        #yl = ax.ylabel("y (km)")

    def salvar(self, filename = None, width = None, height = None, velocidad = None):#Esto se lo pasa el dialogo
        
        aux = len(self.matrix)
        for i in range(0, aux):
        
            print u'Imágen ' + str(i + 1)
            
            self.plotD(0, i)
            self.plotT(0, i)
            self.plotC(0, i)
            
            tmpfilename = 'temp/_tmp_' + str(i) + '.png'

            ppp = atoi(width) + atoi(height) / self.fig.getfigwidth() + self.fig.getfigheight()
            
            self.fig.savefig(tmpfilename, dpi=ppp)
            
            print 'Creada.'
            
        print u'Imágenes preparadas y listas'
        
        #filename = 'graficas'#Hay que pedirlo en el dialogo despues
        
        command = ('mplayer/mencoder.exe',#Para la version de linux hay que cambiar esto y sacar el .exe
            'mf://temp/_tmp_%d.png',
            '-mf',
            'type=png:w=' + width + ':h=' + height + ':fps=' + velocidad,#Estas opciones las debe poder elegir el usuario en el dialogo
            '-ovc',
            'lavc',
            '-lavcopts',
            'vcodec=mpeg4',
            '-oac',
            'copy',
            '-o',
            'videos/' + filename + '.avi')
        
        print u"\n\nSe ejecutará:\n%s\n\n" % ' '.join(command)
        subprocess.check_call(command)

        print u'Comienza borrado de imagenes temporales.'

        for i in range(0, aux):
        
            print u'Imágen ' + str(i + 1)
            
            tmpfilename = 'temp/_tmp_' + str(i) + '.png'
            os.remove(tmpfilename)
            
            print 'Borrada.'
        
        print 'Pronto.'
