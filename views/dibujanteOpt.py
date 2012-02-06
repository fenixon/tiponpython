# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas #Clase para dibujar las gráficas
from models.figuraOpt import figuraOpt as FigureOpt


class dibujanteOpt(QWidget):

    def __init__(self, x = None, y = None, z = None, xx = None, yy = None, parent = None):

        QWidget.__init__(self, parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.fig = FigureOpt(x, y, z, xx, yy)

        if z == None:

            self.setWindowTitle(QString(u'Gráfica de Función objetivo'))

        else:

            self.setWindowTitle(QString(u'Gráfica de Parametros'))

##            self.fig = FigureOpt(x, y, xx,yy)

        self.canvas = FigureCanvas(self.fig.fig)

        self.canvas.draw()

        vbox = QVBoxLayout()
        vbox.addWidget(self.canvas)
        self.setLayout(vbox)

        self.center()
        self.setMinimumSize(288, 384)

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
