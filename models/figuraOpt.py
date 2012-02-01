# -*- coding: utf-8 -*-

import random
from matplotlib.figure import Figure #Clase para contener las gráficas
import matplotlib.pyplot as p

class figuraOpt():

    def __init__(self, x = None, y = None, z = None, xx = None, yy = None):

        self.fig = Figure(figsize = (0.9 * 4, 1.2 * 4))
        self.axt = self.fig.add_subplot(1, 1,1)

        if z == None:
            self.axt.plot(xx,yy, 'r.')
            self.axt.plot(x, y, 'b')
            

            lista = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4,
                4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9,
                9, 9, 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c',
                'c', 'd', 'd', 'd', 'd', 'e', 'e', 'e', 'e', 'f', 'f', 'f',
                'f']

##            for i in range(cantidad_observaciones):

##                tmp = random.sample(lista, 6)
##                tmpstr = '#' + str(tmp[0]) + str(tmp[1]) + str(tmp[2]) + str(tmp[3]) + str(tmp[4]) + str(tmp[5])
                ##plot(obs(i).t,obs(i).h,'bd',t,ho(i,:),'b')
##                self.fig.plot(obs_x, obs_y, ':', tmpstr)

        else:

            #ax = p.Axes(self.fig)
            self.axt.contour(x, y, z)
            self.axt.plot(xx, yy, 'rx')
            
