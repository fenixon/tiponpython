# -*- coding: utf-8 -*-
"""
	tiponpython Simulacion de ensayos de acuiferos
	Copyright 2012 Andres Pias, Alvaro Correa, Jesus Guibert
	
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



import random
from matplotlib.figure import Figure #Clase para contener las gráficas
import matplotlib.pyplot as p

class figuraOpt():

    def __init__(self, x = None, y = None, z = None, xx = None, yy = None):

        self.fig = Figure(figsize = (0.9 * 4, 1.2 * 4))
        self.ax = self.fig.add_subplot(1, 1,1)

        if z == None:

            #self.ax.set_title('Grafica de Funcion objetivo')
            self.ax.set_xlabel('t')
            self.ax.set_ylabel('h')

            self.ax.plot(xx, yy, 'r:')
            for h in y:
                self.ax.plot(x, h, 'b')

        else:

            #ax = p.Axes(self.fig)
            self.ax.contour(x, y, z)
            self.ax.plot(xx, yy, 'rx', markersize = 20)

            #self.ax.set_title('Grafica de Parametros')
            self.ax.set_xlabel('T')
            self.ax.set_ylabel('S')
