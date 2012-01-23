# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------------------------------------------------------------------------#
#Esto va a dibujar las gráficas y controlar el tema de la animación
#-----------------------------------------------------------------------------------------------------------------------------------------------#
from PyQt4.QtGui import * #Para la interfáz gráfica
from PyQt4.QtCore import * #Para la interfáz gráfica
from PyQt4 import QtCore
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas #Clase para dibujar las gráficas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar #Clase para dibujar la barra de herramientas de navegación
import threading
import random

from models.figura import figura as fm
import numpy as np

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class dibujante(QMainWindow):

    def __init__(self, parent = None, dominio=None):#Hay que pasarle la ventana que lo invoca

        QMainWindow.__init__(self, parent)
        ti=0.0
##        tf=3.0
        tf=0.3
        ##      
        ##justito para que quede 0.1 el dt        
##        nit=int(tf/0.1)
##        nit=100
        nit=100

        ##el mismo ancho y alto para que quede cada 1 unidad
####        nix=dominio.ancho
        nix=40
##        niy=dominio.alto
        niy=40

        ##discretizacion temporal
        dt=(tf-ti)/nit
        nit=nit+1
        tiempos=np.zeros((nit),float)
        tiempos[0]=ti        

        ##se suma 1 para que sea haga bien la division es un intervalo mas 0..100 (101)        
        nix=nix+1
        niy=niy+1
        
        #discretizacion temporal
        for i in range(1,nit):
            tiempos[i]=tiempos[i-1]+dt        
        
        ##discretizacion espacial
        xx = np.linspace(0,dominio.ancho,nix) ;
        yy = np.linspace(dominio.alto,0,niy) ;
        ##Se generan las matrices para usar en todas las graficas
        X, Y = np.meshgrid(xx, yy)

        print 'Matrices X, Y'
        print X
        print Y
        print '\n'

        self.ti=ti
        self.tf=tf
        self.dt=dt
        self.nix=nix
        self.niy=niy
        self.cardt=0


        ##Llamado a procesar la barrera.. para generar los pozos virtuales porque se duplican por precensia de la barrera
        dominio.procesarBarrera()

        ##LLAMADO AL METODO DE SOLUCION
        ##llamamo al metodo de solucion asociado al dominio para que me de la matriz
        ### se envian ademas todas las discretizaciones
        matrix=dominio.metodo.calcular(tiempos,xx,yy)

        matx = dominio.metodo.gradienteX()

        maty = dominio.metodo.gradienteY()

        ##se obtiene un pozo de observacion el primero por defecto
        pozoObservacion=dominio.obtenerPozoObservacion()            
        ##Obtener una observacion de ensayo ...que pasa cuando hay mas de una asociada?????        
        observaciones=pozoObservacion.observaciones[0].devolverO()
        self.observaciones = observaciones
      
        pozoBombeo=dominio.obtenerPozoBombeo()
        ##Obtener el ensayo de bombeo, los caudales y tiempos(al menos hay uno) ...que pasa cuando hay mas de un ensayo asociado?????        
        bombeos=pozoBombeo.ensayos[0].devolverB()           
        self.bombeos=bombeos
        
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.fm = fm(matrix, matx, maty, dominio, observaciones, bombeos,X,Y, xx, yy, tiempos)
        ran = random.randint(1, 10)
        self.fm.plotU(ran)
        ##1ero plotT dps plotD        
        self.fm.plotT(ran, 0)
        self.fm.plotD(ran, 0)
        self.fm.plotC(ran, 0)
        self.main_frame = QWidget()
        self.setWindowTitle(u'Gráficas')
        self.setMaximumSize(self.fm.fig.get_figwidth() * self.fm.fig.get_dpi(), self.fm.fig.get_figheight() * self.fm.fig.get_dpi() + 43)
        self.setMinimumSize(self.fm.fig.get_figwidth() * self.fm.fig.get_dpi(), self.fm.fig.get_figheight() * self.fm.fig.get_dpi() + 43)
        print 'Figure: width: ' + str(self.fm.fig.get_figwidth() * self.fm.fig.get_dpi()) + ', height: ' +str(self.fm.fig.get_figheight() * self.fm.fig.get_dpi()) + ', dpi: ' + str(self.fm.fig.get_dpi())
        self.center()
        self.canvas = FigureCanvas(self.fm.fig)
        self.canvas.setParent(self.main_frame)
        #self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)
        self.canvas.draw()
        self.vel = [1, 2, 3, 4, 5, 6]
        self.velActual = 0
        self.inter = 1

        separador = QFrame()
        separador.setFrameShadow(QFrame.Sunken)
        separador.setFrameShape(QFrame.HLine)
        separador.setLineWidth(576)

        reproducirb = QPushButton()
        reproducirb.setMinimumSize(32, 32)
        reproducirb.setMaximumSize(32, 32)
        reproducirb.setIcon(QIcon('content/images/reproducir.png'))
        self.reproducirb = reproducirb
        QtCore.QObject.connect(self.reproducirb, QtCore.SIGNAL(_fromUtf8('released()')), self.reproducir)

        reversab = QPushButton()
        reversab.setMinimumSize(32, 32)
        reversab.setMaximumSize(32, 32)
        reversab.setIcon(QIcon('content/images/reproducir.png'))
        self.reversab = reversab
        QtCore.QObject.connect(self.reversab, QtCore.SIGNAL(_fromUtf8('released()')), self.reversa)

        velocidadb = QPushButton()
        velocidadb.setMinimumSize(32, 32)
        velocidadb.setMaximumSize(32, 32)
        velocidadb.setText(QString(str(self.velActual + 1) + 'x'))
        self.velocidadb = velocidadb
        QtCore.QObject.connect(self.velocidadb, QtCore.SIGNAL(_fromUtf8('released()')), self.velocidad)

        guardarb = QPushButton()
        guardarb.setMinimumSize(32, 32)
        guardarb.setMaximumSize(32, 32)
        guardarb.setIcon(QIcon('content/images/guardar.png'))
        self.guardarb = guardarb
        QtCore.QObject.connect(self.guardarb, QtCore.SIGNAL(_fromUtf8('released()')), self.guardar)

        estadob = QSlider(Qt.Horizontal)
        estadob.setMinimumSize(324, 32)
        estadob.setToolTip(u'Próximamente: mostrará el avance de la animación.')

        ##cambie el tmp
        ####se grafica lo que hay en el primer tiempo
        #tmp = self.fm.matrix[0]
        #Habia un tmp -1
        #estadob.setMaximum(tmp[-1])
        #estadob.setMaximum(20)
        ##El maximo tiempo va a ser lo que hay en el ultimo tiempo de bombeo
        ##estadob.setMaximum(self.bombeos[-1].tiempo*10)
        #Cambio por la discretizacion espacial
        estadob.setMaximum(int(tf/dt))
        estadob.setMinimum(0)
        
        self.estadob = estadob
        QtCore.QObject.connect(self.estadob, QtCore.SIGNAL(_fromUtf8('sliderReleased()')), self.actualizarSlider)
        QtCore.QObject.connect(self.estadob, QtCore.SIGNAL(_fromUtf8('sliderMoved()')), self.actualizarSlider)
        QtCore.QObject.connect(self.estadob, QtCore.SIGNAL(_fromUtf8('valueChanged(int)')), self.actualizarSlider)

        #timlab = QLabel(QString('0/' + str(self.bombeos[-1].tiempo)))
        #el tiempo final elejido por el usuario
        timlab = QLabel(QString('0/' + str(tf)))
        #timlab=QLabel(QString('pepe'))
        self.timlab = timlab

        vbox = QVBoxLayout()
        vbox.addWidget(self.canvas)
        vbox.addWidget(separador)
        hbox = QHBoxLayout()
        hbox.addWidget(reproducirb)
        hbox.addWidget(reversab)
        hbox.addWidget(velocidadb)
        hbox.addWidget(guardarb)
        hbox.addWidget(estadob)
        hbox.addWidget(timlab)
        vbox.addLayout(hbox)
        self.main_frame.setLayout(vbox)
        self.setCentralWidget(self.main_frame)

        self.timer = QTimer(self)
        ##Cada un segundo, dps aca cambiar la velocidad de reproduccion
        self.timer.setInterval(1000 * self.vel[self.velActual])
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.reproducirBucle)

    def draw(self):

        self.canvas.draw()
        self.fm.axt.mouse_init()

    def actualizarSlider(self):

        ran = random.randint(1, 10)
        ##se recupera el tiempo que viene multiplicado
        #t=float(self.estadob.value()/10)
        t=float(self.estadob.value() * self.dt)
##        print 'tiempo: '+ str(t)
        #auxt=[i for i,x in enumerate(self.bombeos) if x.tiempo == t]
        #print 'indices: '+str(auxt)
        #if len(auxt)>0 :
        #    cardt=auxt[0]
        ##AHORA SE CALCULO PARA TODOS LOS TIEMPOS DE LA DISCRETIZACION TEMPORAL
        self.fm.plotD(ran, self.cardt)
        self.fm.plotT(ran, self.cardt)
        self.fm.plotC(ran, self.cardt)
        self.draw()
        #else:
        #    print 'no hay valores para t: '+str(t)
            
        self.estadob.setToolTip(str(t) + '/' + str(self.estadob.maximum()*self.dt))
        self.timlab.setText(self.estadob.toolTip())
        print u'Posición: segundo ' + str(t)

    def reproducir(self):

        if self.timer.isActive() == True:

            #Si ya está reproducioendo, entonces pausamos.
            self.timer.stop()
            self.reproducirb.setIcon(QIcon('content/images/reproducir.png'))
            print u'Próximamente: pausar de las gráficas.'

        else:

            self.timer.start()
            self.reproducirb.setIcon(QIcon('content/images/pausar.png'))
            print u'Próximamente: reproducción de las gráficas.'

    def reproducirBucle(self):

        if self.estadob.value() + self.inter > self.estadob.maximum():

            self.reproducir()
            self.estadob.setValue(0)
            self.cardt=0
            
        elif self.estadob.value() + self.inter < self.estadob.minimum():

            self.reproducir()
            self.estadob.setValue(0)
            self.cardt=0

        else:

            self.estadob.setValue(self.estadob.value() + self.inter)
            self.cardt = self.cardt + self.inter

    def reversa(self):

        self.inter = self.inter * -1

    def pausar(self):

        t.stop()
        print u'Próximamente: pausa de la animación de las gráficas.'

    def velocidad(self):

        if self.velActual+1 < len(self.vel):
            self.velActual = self.velActual + 1
        else:
            self.velActual = 0

        self.timer.setInterval(1000 / self.vel[self.velActual])
        self.velocidadb.setText(QString(str(self.velActual + 1) + 'x'))

    def guardar(self):

        print u'Próximamente: guardará la animación de las gráficas en un video.'

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    fv = dibujante()
    fv.show()
    sys.exit(app.exec_())
