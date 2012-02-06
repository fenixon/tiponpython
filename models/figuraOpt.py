# -*- coding: utf-8 -*-

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
            self.ax.plot(x, y, 'b')

        else:

            #ax = p.Axes(self.fig)
            self.ax.contour(x, y, z)
            self.ax.plot(xx, yy, 'rx', markersize = 20)

            #self.ax.set_title('Grafica de Parametros')
            self.ax.set_xlabel('T')
            self.ax.set_ylabel('S')
