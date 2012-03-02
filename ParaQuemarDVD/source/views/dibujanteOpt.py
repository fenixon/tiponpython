# -*- coding: utf-8 -*-
"""
	tiponpython Simulacion de ensayos de acuiferos
	Copyright 2012 Andres Pias, Jesus Guibert
	
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
