# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------------------------------------------------------------------------#
#Esto va a dibujar las gráficas y controlar el tema de la animación
#-----------------------------------------------------------------------------------------------------------------------------------------------#
from PyQt4.QtGui import * #Para la interfáz gráfica
from PyQt4.QtCore import * #Para la interfáz gráfica
from PyQt4 import QtCore
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas #Clase para dibujar las gráficas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar #Clase para dibujar la barra de herramientas de navegación

from models.figura import figura as fm

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class dibujante(QMainWindow):

    def __init__(self, parent):#Hay que pasarle la ventana que lo invoca

        QMainWindow.__init__(self, parent)
        self.fm = fm()
        self.fm.plotU()
        self.fm.plotD()
        self.fm.plotT()
        self.fm.plotC()
        self.main_frame = QWidget()
        self.setWindowTitle(u'Gráficas')
        self.setMaximumSize(self.fm.fig.get_figwidth() * self.fm.fig.get_dpi(), self.fm.fig.get_figheight() * self.fm.fig.get_dpi() + 43)
        self.setMinimumSize(self.fm.fig.get_figwidth() * self.fm.fig.get_dpi(), self.fm.fig.get_figheight() * self.fm.fig.get_dpi() + 43)
        print 'Figure: width: ' + str(self.fm.fig.get_figwidth() * self.fm.fig.get_dpi()) + ', height: ' +str(self.fm.fig.get_figheight() * self.fm.fig.get_dpi()) + ', dpi: ' + str(self.fm.fig.get_dpi())
        self.canvas = FigureCanvas(self.fm.fig)
        self.canvas.setParent(self.main_frame)
        #self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)

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

        guardarb = QPushButton()
        guardarb.setMinimumSize(32, 32)
        guardarb.setMaximumSize(32, 32)
        guardarb.setIcon(QIcon('content/images/guardar.png'))
        self.guardarb = guardarb
        QtCore.QObject.connect(self.guardarb, QtCore.SIGNAL(_fromUtf8('released()')), self.guardar)

        estadob = QSlider(Qt.Horizontal)
        estadob.setMinimumSize(480, 32)
        estadob.setToolTip(u'Próximamente: mostrará el avance de la animación.')

        vbox = QVBoxLayout()
        vbox.addWidget(self.canvas)
        vbox.addWidget(separador)
        hbox = QHBoxLayout()
        hbox.addWidget(reproducirb)
        hbox.addWidget(guardarb)
        hbox.addWidget(estadob)
        vbox.addLayout(hbox)
        self.main_frame.setLayout(vbox)
        self.setCentralWidget(self.main_frame)
        self.fm.axt.mouse_init()

    def draw(self):

        self.canvas.draw()

    def reproducir(self):

        print u'Próximamente: reproducción de las gráficas.'

    def pausar(self):

        print u'Próximamente: pausa de la animación de las gráficas.'

    def guardar(self):

        print u'Próximamente: guardará la animación de las gráficas en un video.'

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    fv = dibujante()
    fv.show()
    sys.exit(app.exec_())