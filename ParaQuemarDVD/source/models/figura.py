# -*- coding: utf-8 -*-
"""
	tiponpython Simulacion de ensayos de acuiferos
	Copyright 2012 Andres Pias, Mathias Chubrega, Alvaro Correa, Sebastian Daloia, Jesus Guibert
	
	This file is part of tiponpython.

	tiponpython is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	any later version.

	tiponpython is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with tiponpython.  If not, see http://www.gnu.org/licenses/gpl.txt.
"""
#-----------------------------------------------------------------------------------------------------------------------------------------------
#Acá se van a calcular las gráficas
#-----------------------------------------------------------------------------------------------------------------------------------------------
from matplotlib.figure import Figure #Clase para contener las gráficas
from mpl_toolkits.mplot3d.axes3d import Axes3D #Clase para trabajar con gráficas 3d
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas #Clase para dibujar las gráficas
from matplotlib import cm#Para los colores de la gráfica 3d
import numpy as np #Clase que contiene funciones y clases matemáticas que se van a utilizar mucho
import pylab as p #???
import matplotlib.pyplot as plt
import subprocess #Esta clase, nativa en python 2.7, permite deribar el trabajo a un subproceso, se utiliza para llamar a mencoder
import os #Provee al programa accesibilidad a funciones del sistema operativo, como acceder al sistema de archivos
import sys

class figura():

    def __init__(self, matrix, matx, maty, dominio, tipodis, X, Y, tiempos, tiemposobs, superficies, ming, maxg, selected = None, parent = None):

        fig = Figure(figsize = (1.8 * 4, 2.4 * 4))

        self.ax = None
        self.axt = None

        fig.subplots_adjust(hspace=.2, wspace=.3, bottom=.07, left=.08, right=.92, top=.94)



        print "tipos q ",tiempos
        print "tiempos obs ", tiemposobs

        self.fig = fig
        self.matrix = matrix
        self.dominio=dominio
        self.tipodis=tipodis
        self.X=X
        self.Y=Y
        self.matx = matx
        self.maty = maty
        self.ming=ming
        self.maxg=maxg
        self.tiempos = tiempos
        self.tiemposobs = tiemposobs
        self.superficies=superficies

        #self.axt.set_ylim3d(0,1000)
        #self.axt.set_xlim3d(0,1000)
        #self.axt.set_zlim3d(self.ming, self.maxg)

    def plotU(self):

        if self.axt != None:

            self.axt.cla()
            self.fig.delaxes(self.axt)
            self.axt = None


        if self.ax == None:

            self.ax = self.fig.add_subplot(111)

        ax = self.ax
        ax.cla()
        ax.set_title(u'Simulación de niveles (h) en puntos de observación (Problema directo)')
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
            t = self.tiemposobs
            print "tiempos",t
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


    def plotU2(self, ax):       
        ax.cla()
##        ax.set_title(u'Gráficos de evolución de niveles (Problema directo)')
        #ax.set_title(u'Simulación de niveles (h) en puntos de observación (Problema directo)')
        ax.set_xlabel('t')
        ax.set_ylabel('h')
        d=self.dominio
        ##Obtener todos los pozos de observacion
        TodoslospozosObservacion=d.obtenerPozosdeObservacion()

        ##recorrer todos los pozos de observacion
        for pozoObservacion in TodoslospozosObservacion:
            #h = self.matrix[:, auxty[0], auxtx[0]]
            h = pozoObservacion.devolverSolucionadas()
            t = self.tiemposobs
            print "tiempos",t
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
                

    def plotD(self, t):

        Z = self.matrix[t]

        if self.axt != None:

            self.axt.cla()
            self.fig.delaxes(self.axt)
            self.axt = None

        if self.ax == None:

            self.ax = self.fig.add_subplot(111)

        ax = self.ax
        ax.cla()
        ax.set_title(u'Evolución de curvas de nivel en el dominio (Problema directo, 2D)')

        divi=np.zeros((len(self.Y),len(self.X)), float)
        divi[:,:]=Z[0,0]
        #BUG DE MATPLOTLIB: se grafica solo si la matriz no es multiplo de ones, no hay una curva de nivel

        if not p.all(np.equal(Z,divi)):

            ax.contour(self.X, self.Y, Z)


    def plotD2(self, t,ax):

        Z = self.matrix[t]
        ax.cla()

        divi=np.zeros((len(self.Y),len(self.X)), float)
        divi[:,:]=Z[0,0]
        #BUG DE MATPLOTLIB: se grafica solo si la matriz no es multiplo de ones, no hay una curva de nivel

        if not p.all(np.equal(Z,divi)):
            ax.contour(self.X, self.Y, Z)


    def plotT(self, t):

        if self.ax != None:

            self.ax.cla()
            self.fig.delaxes(self.ax)
            self.ax = None

        if self.axt == None:

            self.axt = self.fig.add_subplot(1, 1, 1, projection = '3d')
            #Esto se agregó para darle la proyección necesaria igual a Matlab
            self.axt.view_init(20,-140)

        ax = self.axt
        ax.cla()

        #print "va en el tiempo: ",t, "valor: ",self.tiempos[t]

        Z = self.matrix[t]        

        #print "tamaño", len(Z)
        #print "Z ",Z
        #print "X " ,self.X
        #print "Y " ,self.Y        

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

        #print "tipo metodo ",self.dominio.metodo.gettipo()

        if self.dominio.metodo.gettipo()=="analitico":       
            surf = ax.plot_surface(self.X, self.Y, Z, rstride=1, cstride=1, cmap=cm.jet,linewidth=1, antialiased=False)
        else:
            surf = ax.plot_wireframe(self.X, self.Y, Z, cmap=cm.jet)      

        ax.set_zlim3d(self.ming, self.maxg)
        ax.set_title(u'Evolución de niveles en el dominio (Problema directo, 3D)')
        ax.mouse_init()

    def plotT2(self, t, ax):
        ax.view_init(20,-140)
        ax.cla()
        Z = self.matrix[t]       
        if self.dominio.metodo.gettipo()=="analitico":       
            surf = ax.plot_surface(self.X, self.Y, Z, rstride=1, cstride=1, cmap=cm.jet,linewidth=1, antialiased=False)
        else:
            surf = ax.plot_wireframe(self.X, self.Y, Z, cmap=cm.jet)      
        ax.set_zlim3d(self.ming, self.maxg)
##        ax.set_title(u'Evolución de niveles en el dominio (Problema directo, 3D)')
        ax.mouse_init()
        

    def plotC(self, t):

        if self.axt != None:

            self.axt.cla()
            self.fig.delaxes(self.axt)
            self.axt = None

        if self.ax == None:

            self.ax = self.fig.add_subplot(111)

        ax = self.ax
        ax.cla()

        X = self.X
        Y = self.Y
        u = self.matx[t]
        ax.set_title(u'Gradiente del nivel (Problema directo, dirección de flujo)')

        ##Esta pregunta es para que no salten los warnings porque los vectores son 000
        divi=np.zeros((len(self.Y),len(self.X)), float)

        if not p.all(np.equal(u,divi)):

            if self.tipodis!=None and self.tipodis=="Logaritmica":

                print 'Aún no disponible para este tipo de discretización'

            else:

                if self.tipodis==None:

                    v = self.maty[t]*-1

                elif self.tipodis=="Lineal":

                    #quiver(x,y,gxh(:,:,i),gyh(:,:,i));
                    v = self.maty[t]

                q = ax.quiver(X, Y, u, v, color=['r'])


    def plotC2(self, t, ax):
        ax.cla()
        X = self.X
        Y = self.Y
        u = self.matx[t]
        #ax.set_title(u'Gradiente del nivel (Problema directo, dirección de flujo)')
        ##Esta pregunta es para que no salten los warnings porque los vectores son 000
        divi=np.zeros((len(self.Y),len(self.X)), float)
        if not p.all(np.equal(u,divi)):
            if self.tipodis==None or self.tipodis!="Logaritmica":
##                print 'Aún no disponible para este tipo de discretización'
            #else:
                if self.tipodis==None:
                    v = self.maty[t]*-1
                elif self.tipodis=="Lineal":
                    #quiver(x,y,gxh(:,:,i),gyh(:,:,i));
                    v = self.maty[t]
                q = ax.quiver(X, Y, u, v, color=['r'])

                

    def salvar(self, filename = None, width = None, height = None, velocidad = None, directorio = None):#Esto se lo pasa el dialogo

        self.fig.clf()

##        self.fig.delaxes(self.ax)
##        self.fig.delaxes(self.axt)

        fig2= Figure(figsize = (1.8 * 4, 2.4 * 4))
        fig2 = plt.figure(figsize = (1.8 * 4, 2.4 * 4))

        axu2 = fig2.add_subplot(2, 2, 1)
        axd2 = fig2.add_subplot(2, 2, 2)
        axt2 = fig2.add_subplot(2, 2, 3, projection = '3d')
        axc2 = fig2.add_subplot(2, 2, 4)

##        self.axu = self.fig.add_subplot(2, 2, 1)
##        self.axd = self.fig.add_subplot(2, 2, 2)
##        self.axt = self.fig.add_subplot(2, 2, 3, projection = '3d')
##        self.axc = self.fig.add_subplot(2, 2, 4)
        fig2.subplots_adjust(hspace=.2, wspace=.3, bottom=.07, left=.08, right=.92, top=.94)
        
        self.plotU2(axu2)
##        self.plotU()

        aux = len(self.matrix)
        for i in range(0, aux):

            self.plotD2(i, axd2)
            self.plotT2(i, axt2)
            self.plotC2(i, axc2)
##            self.plotD(i)
##            self.plotT(i)
##            self.plotC(i)            

            canvas = FigureCanvas(fig2)
            canvas.draw() 
            #p.show()            

            tmpfilename = 'temp/_tmp_' + str(i) + '.png'

            #Regla de tres para sacar el dpi que debería tener cada imagen del video según el tamaño ingresado.
            ppp = ((float(width) + float(height)) * self.fig.get_dpi()) / ((self.fig.get_figwidth() + self.fig.get_figheight()) * self.fig.get_dpi())

            fig2.savefig(tmpfilename, dpi=ppp)
##            self.fig.savefig(tmpfilename, dpi=ppp)


        if sys.platform == 'linux2':

            command = ('mencoder',
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

        #elif os.platform == 'darwin':

        else:

            command = ('mplayer/mencoder.exe',
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

        subprocess.check_call(command)

        for i in range(0, aux):

            tmpfilename = 'temp/_tmp_' + str(i) + '.png'
            os.remove(tmpfilename)

##        self.fig.delaxes(self.axu)
##        self.fig.delaxes(self.axd)
##        self.fig.delaxes(self.axt)
##        self.fig.delaxes(self.axc)            

