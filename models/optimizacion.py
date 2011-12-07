from numpy import *

class optimizacion(object):

    def __init__(self):
        self.MatrizDescenso = zeros( (3,1) )
        self.listaParametros = []

    def __del__(self):
        print "Objeto eliminado"
