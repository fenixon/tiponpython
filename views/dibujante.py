# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------------------------------------------------------------------------#
#Esto va a dibujar las gráficas y controlar el tema de la animación
#-----------------------------------------------------------------------------------------------------------------------------------------------#
from PyQt4.QtGui import * #Para la interfáz gráfica
from PyQt4.QtCore import * #Para la interfáz gráfica
from PyQt4 import QtCore
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas #Clase para dibujar las gráficas
import threading
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import cm#Para los colores de la gráfica 3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import random
from videoDialog import videoDialog

from models.figura import figura as fm
import numpy as np

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class dibujante(QMainWindow):

    def __init__(self, parent = None, dominio=None, tipodis=None, X=None,Y=None, xx=None, yy=None, nix=None, niy=None, tiempos=None, tiemposobs=None, ti=None, tf=None, dt=None, dia=None):

        QMainWindow.__init__(self, parent)
        self.dia=dia

        self.ti=ti
        self.tf=tf
        self.dt=dt
        #self.nix=nix
        #self.niy=niy
        #self.tfo=tfo
        self.cardt=0

        ##LLAMADO AL METODO DE SOLUCION
        ##llamamo al metodo de solucion asociado al dominio para que me de la matriz
        ### se envian ademas todas las discretizaciones
        print u'Empieaza...'
        matrix=dominio.metodo.calcular(tiempos, ti, tf, dt, nix, niy, xx,yy, X, Y)
    

        matx = dominio.metodo.gradienteX()

        maty = dominio.metodo.gradienteY()

        ming = dominio.metodo.minimoMatriz()

        maxg = dominio.metodo.maximoMatriz()
        print u'Termina'

        #pozoBombeo=dominio.obtenerPozoBombeo()
        ##Obtener el ensayo de bombeo, los caudales y tiempos(al menos hay uno) ...que pasa cuando hay mas de un ensayo asociado?????
        #bombeos=pozoBombeo.ensayos[0].devolverB()
        #self.bombeos=bombeos

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

#### Codigo nuevo introducido para prueba

        #fig2 = Figure(figsize = (1.5, 2.5))

        #fig2 = Figure(figsize = (1.8 * 4, 2.4 * 4))
        #axu2 = fig2.add_subplot(2, 2, 1)
        #axd2 = fig2.add_subplot(2, 2, 2)
        #axt2 = fig2.add_subplot(2, 2, 3, projection = '3d')
        #axc2 = fig2.add_subplot(2, 2, 4)
        #fig2.subplots_adjust(hspace=.2, wspace=.3, bottom=.07, left=.08, right=.92, top=.94)

        #axt = Axes3D(fig2)        
##        superficies=np.zeros((len(tiempos)),Poly3DCollection)
        superficies=[]
        #for i in range(0,nit):
        #    Z = matrix[i]
        #    axt2.cla()
##        print 'Matriz generada '
##            print 't: '+str(i)
##            print 'Z: \n' + str(Z)
        #    surf = axt2.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet,linewidth=0, antialiased=False)

        #    superficies.append(surf)
##            canvas = FigureCanvas(fig2)
##            canvas.draw()        

#### fIN Codigo nuevo introducido para prueba

        self.fm = fm(matrix, matx, maty, dominio, tipodis, X,Y, tiempos, tiemposobs, superficies, ming, maxg)

        self.sel = 0
        self.grafSel(0)
        self.main_frame = QWidget()
        self.setWindowTitle(u'Gráficas')
        self.setMinimumSize(276, 568)
        self.center()
        self.canvas = FigureCanvas(self.fm.fig)
        self.canvas.setParent(self.main_frame)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.canvas.draw()
        self.vel = [1, 2, 3]
        self.velActual = 0
        self.inter = 1

        separador = QFrame()
        separador.setFrameShadow(QFrame.Sunken)
        separador.setFrameShape(QFrame.HLine)
        separador.setLineWidth(576)

        selectc = QComboBox()
        selectc.addItem(QIcon(u'content/images/plot.png'), QString(u'Lineal'), 0)
        selectc.addItem(QIcon(u'content/images/contour.png'), QString(u'Propagación'), 1)
        selectc.addItem(QIcon(u'content/images/contour.png'), QString(u'3D'), 2)
        selectc.addItem(QIcon(u'content/images/quiver.png'), QString(u'Velocidad'), 3)
        self.selectc = selectc
        QtCore.QObject.connect(self.selectc, QtCore.SIGNAL(_fromUtf8('currentIndexChanged (int)')), self.grafSele)

        reproducirb = QPushButton()
        reproducirb.setMinimumSize(32, 32)
        reproducirb.setMaximumSize(32, 32)
        reproducirb.setIcon(QIcon('content/images/reproducir.png'))
        self.reproducirb = reproducirb
        QtCore.QObject.connect(self.reproducirb, QtCore.SIGNAL(_fromUtf8('released()')), self.reproducir)

        reversab = QPushButton()
        reversab.setMinimumSize(32, 32)
        reversab.setMaximumSize(32, 32)
        reversab.setIcon(QIcon('content/images/normal.png'))
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

        #Cambio por la discretizacion espacial

        print "tf ",tf,"dt ",dt, "maximo ",tf/dt

        if dominio.metodo.gettipo()!="analitico":        
            estadob.setMaximum(int(tf/dt)-1)
        else:
            estadob.setMaximum(int(tf/dt))
        estadob.setMinimum(0)

        self.estadob = estadob
        QtCore.QObject.connect(self.estadob, QtCore.SIGNAL(_fromUtf8('sliderReleased()')), self.actualizarSlider)
        QtCore.QObject.connect(self.estadob, QtCore.SIGNAL(_fromUtf8('sliderMoved()')), self.actualizarSlider)
        QtCore.QObject.connect(self.estadob, QtCore.SIGNAL(_fromUtf8('valueChanged(int)')), self.actualizarSlider)

        #el tiempo final elejido por el usuario
        timlab = QLabel(QString('0/' + str(tf)))
        self.timlab = timlab

        vbox = QVBoxLayout()
        vbox.addWidget(self.canvas)
        vbox.addWidget(separador)
        hbox = QHBoxLayout()
        hbox.addWidget(selectc)
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

        if self.dia!=None:
            self.dia.close()
            self.dia = None

    def draw(self):
        self.canvas.draw()

    def actualizarSlider(self):

        ##se recupera el tiempo que viene multiplicado
        t=float(self.estadob.value() * self.dt)

        ##AHORA SE CALCULO PARA TODOS LOS TIEMPOS DE LA DISCRETIZACION TEMPORAL
        self.grafSel(self.cardt)
        self.draw()

        self.estadob.setToolTip(str(t) + '/' + str(self.estadob.maximum()*self.dt))
        self.timlab.setText(self.estadob.toolTip())

    def reproducir(self):

        if self.timer.isActive() == True:

            #Si ya está reproducioendo, entonces pausamos.
            self.timer.stop()
            self.reproducirb.setIcon(QIcon('content/images/reproducir.png'))

        else:

            self.timer.start()
            self.reproducirb.setIcon(QIcon('content/images/pausar.png'))

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

        if self.inter < 0:

            self.reversab.setIcon(QIcon('content/images/reversa.png'))

        else:

            self.reversab.setIcon(QIcon('content/images/normal.png'))

    def pausar(self):

        t.stop()

    def velocidad(self):

        if self.velActual+1 < len(self.vel):
            self.velActual = self.velActual + 1
        else:
            self.velActual = 0

        self.timer.setInterval(1000 / (self.vel[self.velActual]))
        self.velocidadb.setText(QString(str(self.velActual + 1) + 'x'))

    def guardar(self):

        if self.timer.isActive() == True:
            self.reproducir()
        self.estadob.setValue(0)
        self.cardt=0

        self.dia = None

        self.dia = videoDialog(self.fm)
        self.dia.center()
        self.dia.show()

    def grafSel(self, cardt):

        if self.sel == 0:

            self.fm.plotU()

        elif self.sel == 1:

            self.fm.plotD(cardt)

        elif self.sel == 2:

            self.fm.plotT(cardt)

        elif self.sel == 3:

            self.fm.plotC(cardt)

    def grafSele(self, i):

        self.sel = i
        self.grafSel(self.cardt)
        self.draw()

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
