# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------------------------------------------------------------------------#
#
#-----------------------------------------------------------------------------------------------------------------------------------------------#
from PyQt4.QtGui import * #Para la interfáz gráfica
from PyQt4.QtCore import * #Para la interfáz gráfica
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas #Clase para dibujar las gráficas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar #Clase para dibujar la barra de herramientas de navegación

from models.figura import figura as fm

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
        self.setMaximumSize(self.fm.fig.get_figwidth() * self.fm.fig.get_dpi(), self.fm.fig.get_figheight() * self.fm.fig.get_dpi())
        self.setMinimumSize(self.fm.fig.get_figwidth() * self.fm.fig.get_dpi(), self.fm.fig.get_figheight() * self.fm.fig.get_dpi())
        print 'width: ' + str(self.fm.fig.get_figwidth() * self.fm.fig.get_dpi()) + ', height: ' +str(self.fm.fig.get_figheight() * self.fm.fig.get_dpi()) + ', dpi: ' + str(self.fm.fig.get_dpi())
        self.canvas = FigureCanvas(self.fm.fig)
        self.canvas.setParent(self.main_frame)
        #self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)
        vbox = QVBoxLayout()
        vbox.addWidget(self.canvas)
        self.setCentralWidget(self.main_frame)
        self.fm.axt.mouse_init()

    def draw(self):

        self.canvas.draw()

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    fv = dibujante()
    fv.show()
    sys.exit(app.exec_())