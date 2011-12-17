from PyQt4 import QtCore, QtGui
from pozo  import pozo
from barrera import barrera
import numpy as np
import observacion
import observacionesensayo
import bombeo
import ensayobombeo

class Proyecto(object):
    
    def __init__(self):        
        self.ultimoIdEns=0
        self.ultimoIdObs=0
        self.ensayos=[]
        self.observaciones=[]

        #Lista que guardan pozo y recta
        self.listaPozo = []
        self.listaRecta = []
        
    def agregarEnsayo(self, bombeos):
        self.ultimoIdEns=self.ultimoIdEns + 1
        e=ensayobombeo.ensayobombeo(bombeos, self.ultimoIdEns)
        self.ensayos.append(e)
        return e

    def agregarObservacion(self, observaciones):
        self.ultimoIdObs=self.ultimoIdObs + 1
        obse=observacionesensayo.observacionesensayo(observaciones, self.ultimoIdObs)
        self.observaciones.append(obse)
        return obse

    #CRUD de pozos
    def agregarPozo(self, identificador, x, y):        
        p = pozo(x, y)
        p.id = identificador
        self.listaPozo.append(p)
        for x in self.listaPozo:
            print x.id
        

    def moverPozo(self, idElemento, x, y):
        for x in self.listaPozo:
            if x.id == idElemento:
                x.actualizarCoordenadas(x, y)
                return

    #CRUD de barreras
    def agregarRecta(self, tipo, x1, y1, x2, y2):        
        r = barrera(x1, x2, y1, y2, tipo)
        r.id = len(self.listaRecta)
        self.listaRecta.append(r)        

    def dibujarRecta(self):
        return self.listaRecta
            
    def buscarPuntoEnRecta(self, x, y):

        for barrera in self.listaRecta:

            recta = QtCore.QLine(barrera.x1, barrera.y1, barrera.x2, barrera.y2)

            puntoP = QtCore.QPoint(x, y)
            puntoQ = QtCore.QPoint(recta.x1(), recta.y1())

            rectay = QtCore.QLine(puntoP, puntoQ)           

            puntoR = QtCore.QPoint(recta.x2(), recta.y2())

            rectaw = QtCore.QLine(puntoP, puntoR)           
            
            #Recta prozima a las x
            if np.absolute(rectay.dx()) < np.absolute(recta.dx() /2) and  np.absolute(rectay.dy()) < np.absolute((recta.dy() / 2)):               
                lista = {}
                lista['punto'] = puntoQ
                lista['eje'] = "x"
                lista['id'] = barrera.id
                return lista
            
            #Recta proxima a las y
            if np.absolute(rectaw.dx()) < np.absolute(recta.dx() /2) and  np.absolute(rectaw.dy()) < np.absolute((recta.dy() / 2)):
                lista = {}
                lista['punto'] = puntoR
                lista['eje'] = "y"
                lista['id'] = barrera.id
                return lista
        lista = {}
        return lista

    def actualizarRecta(self, idRecta, x, y, tipoPunto):
        for barrera in self.listaRecta:
            if barrera.id == idRecta:
                if tipoPunto == "R":   
                    barrera.x2 = x
                    barrera.y2 = y
                else:
                    barrera.x1 = x
                    barrera.y1 = y
                return
