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

    def __init__(self, matrix, matx, maty, dominio, X, Y, xx, yy, tiempos, superficies, ming, maxg, selected = None, parent = None):

        fig = Figure(figsize = (1.8 * 4, 2.4 * 4))
        #self.axu = fig.add_subplot(2, 2, 1)
        #self.axd = fig.add_subplot(2, 2, 2)
        #self.axt = fig.add_subplot(2, 2, 3, projection = '3d')
        #self.axc = fig.add_subplot(2, 2, 4)

        self.ax = None
        self.axt = None

        fig.subplots_adjust(hspace=.2, wspace=.3, bottom=.07, left=.08, right=.92, top=.94)

        self.fig = fig
        self.matrix = matrix
        self.dominio=dominio
        #self.observaciones=observaciones
        #self.bombeos=bombeos
        self.X=X
        self.Y=Y
        self.matx = matx
        self.maty = maty
        self.ming=ming
        self.maxg=maxg
        self.xx = xx
        self.yy = yy
        self.tiempos = tiempos
        self.superficies=superficies

        #self.axt.set_ylim3d(0,1000)
        #self.axt.set_xlim3d(0,1000)
        #self.axt.set_zlim3d(self.ming, self.maxg)

    def plotU(self):

        #ax = self.axu
        if self.axt != None:

            self.fig.delaxes(self.axt)
            self.axt = None


        if self.ax == None:

            self.ax = self.fig.add_subplot(111)

        ax = self.ax
        ax.cla()
        ax.set_title('Descensos h en tiempo t')
        ax.set_xlabel('t')
        ax.set_ylabel('h')
        #x = np.arange(0, ran, .05)
        #print 'Aleatorio: ' + str(ran)
        #x = np.arange(0, 10, .05)#Descensos (h), son números que representan el nivel piezométrico
        #y = np.arange(0, 10, .05)#Tiempos (t), se supone están en días
        #y = np.sin(x) + ran*2
        #auxtx = [i for i,x in enumerate(self.xx) if x == pozoObs.x]
        #auxty = [i for i,x in enumerate(self.yy) if x == pozoObs.y]

        #h = self.matrix[:, auxty[0], auxtx[0]]
        #t = self.tiempos
        d=self.dominio
        ##Obtener todos los pozos de observacion
        TodoslospozosObservacion=d.obtenerPozosdeObservacion()

        ##recorrer todos los pozos de observacion
        for pozoObservacion in TodoslospozosObservacion:
            #h = self.matrix[:, auxty[0], auxtx[0]]
            h = pozoObservacion.devolverSolucionadas()
            t = self.tiempos
            ax.plot(t, h, 'b')
            for conjob in pozoObservacion.observaciones:
                ##Obtener todas las observacion del conjunto de observaciones
                self.observaciones=conjob.devolverO()

                x=[]
                y=[]
                for ob in self.observaciones:
                    x.append(ob.tiempo)
                    y.append(ob.nivelpiezometrico)
                ax.plot(x,y, 'r.')
        #print 'First plot loaded...'

    def plotD(self, t):

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

            #ax = self.axd
            if self.axt != None:

                self.fig.delaxes(self.axt)
                self.axt = None

            if self.ax == None:

                self.ax = self.fig.add_subplot(111)

            ax = self.ax
            ax.cla()
            #CS = contour(X, Y, Z)
            ax.contour(self.X, self.Y, Z)
            #clabel(CS, inline=1, fontsize=10)
            ax.set_title(u'Propagación')

        #print u'Segunda gráfica cargada.'

    def plotT(self, t):

        #add_subplot(filas, columnas, número de gráfica/posición, tipo de gráfica)
##        print 'Loading third plot...'
        #ax = self.axt

        if self.axt == None:

            self.axt = self.fig.add_subplot(1, 1, 1, projection = '3d')

        if self.ax != None:

            self.fig.delaxes(self.ax)
            self.ax = None

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

        Z = self.matrix[t]

        #print 'Matriz generada '
        #print 'Z: \n' + str(Z)

##        auxt = [i for i,x in enumerate(self.tiempos) if x == t]
##        print t
##        print self.superficies[t]

        #ax.add_collection3d(self.superficies[t])


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

        surf = ax.plot_surface(self.X, self.Y, Z, rstride=1, cstride=1, cmap=cm.jet,linewidth=0, antialiased=False)

###     comente lo de los limites porque hay que setearlos segun como venga el dominio
##      Esto tiene que cambiar segun los valores maximos y minimos de Z
##        ax.set_zlim3d(9.3, 10)
        ax.set_zlim3d(self.ming, self.maxg)
        #ax.set_zlim3d(-100, 100)# viewrange for z-axis should be [-4,4]
##        ax.set_ylim3d(0, 20)# viewrange for y-axis should be [-2,2]
##        ax.set_xlim3d(0, 20)
        ax.set_title(u'Representación 3d')
        #print u'Gráfica en tres dimensiones cargada.'
#            fig.colorbar(surf, shrink=0.5, aspect=10)

    def plotC(self, t):

##        print 'Loading fourth plot...'
        #ax = self.axc
        if self.axt != None:

            self.fig.delaxes(self.axt)
            self.axt = None

        if self.ax == None:

            self.ax = self.fig.add_subplot(111)

        ax = self.ax
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
        #print u'Cuarta gráfica cargada.'
        #xl = ax.xlabel("x (km)")
        #yl = ax.ylabel("y (km)")

    def salvar(self, filename = None, width = None, height = None, velocidad = None, directorio = None):#Esto se lo pasa el dialogo

        #print 'Evaluando entradas...'
        #print 'Nombre del archivo: ' + filename
        #print 'Ancho: ' + str(width)
        #print 'Alto: ' + str(height)
        #print 'Velocidad: ' + velocidad
        #print 'Listo, entradas correctas.'

        self.fig.clf()

        self.fig.delaxes(self.ax)

        self.axu = self.fig.add_subplot(2, 2, 1)
        self.axd = self.fig.add_subplot(2, 2, 2)
        self.axt = self.fig.add_subplot(2, 2, 3, projection = '3d')
        self.axc = self.fig.add_subplot(2, 2, 4)


        aux = len(self.matrix)
        for i in range(0, aux):

            #print u'Imágen ' + str(i + 1)

            self.plotD(i)
            self.plotT(i)
            self.plotC(i)

            tmpfilename = 'temp/_tmp_' + str(i) + '.png'

            #Regla de tres para sacar el dpi que debería tener cada imagen del video según el tamalo ingresado.
            ppp = ((float(width) + float(height)) * self.fig.get_dpi()) / ((self.fig.get_figwidth() + self.fig.get_figheight()) * self.fig.get_dpi())

            self.fig.savefig(tmpfilename, dpi=ppp)

            #print 'Creada.'

        #print u'Imágenes preparadas y listas'

        command = ('mplayer/mencoder.exe',#Para la version de linux hay que cambiar esto y sacar el .exe
            'mf://temp/_tmp_%d.png',
            '-mf',
            'type=png:w=' + str(width) + ':h=' + str(height) + ':fps=' + velocidad,
            '-ovc',
            'lavc',
            '-lavcopts',
            'vcodec=mpeg4',
            '-oac',
            'copy',
            '-o',
            directorio + '/' + filename + '.avi')

        #print u"\n\nSe ejecutará:\n%s\n\n" % ' '.join(command)
        subprocess.check_call(command)

        #print u'Comienza borrado de imagenes temporales.'

        for i in range(0, aux):

            #print u'Imágen ' + str(i + 1)

            tmpfilename = 'temp/_tmp_' + str(i) + '.png'
            os.remove(tmpfilename)

            #print 'Borrada.'

        #print 'Pronto.'

        self.fig.delaxes(self.axu)
        self.fig.delaxes(self.axd)
        self.fig.delaxes(self.axt)
        self.fig.delaxes(self.axc)