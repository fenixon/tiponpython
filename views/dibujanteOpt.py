# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas #Clase para dibujar las gráficas
from models.figuraOpt import figuraOpt as FigureOpt


class dibujanteOpt(QMainWindow):

    def __init__(self, x = None, y = None, z = None, xx = None, yy = None, parent = None):

        QMainWindow.__init__(self, parent)
        self.setAttribute(Qt.WA_DeleteOnClose)        

        self.fig = FigureOpt(x, y, z, xx, yy)

        if z == None:

            self.setWindowTitle(QApplication.translate("frmdibujanteOpt", "Grafica de Funcion objetivo", None, QApplication.UnicodeUTF8))

        else:

            self.setWindowTitle(QApplication.translate("frmdibujanteOpt", "Grafica de Parametros", None, QApplication.UnicodeUTF8))

##            self.fig = FigureOpt(x, y, xx,yy)

        self.canvas = FigureCanvas(self.fig.fig)

        self.canvas.draw()

        self.setCentralWidget(self.canvas)

        self.center()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
