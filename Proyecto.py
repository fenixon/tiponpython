'''
Created on 11/11/2011

@author: mathias
'''

class metodoSolucion(object):
    
    def __init__(self, nombre, param1, param2):
        self.nombre = nombre
        self.param1 = param1
        self.param2 = param2
        print "Se ha creado el Metodo de Solucion"
        
    def __del__(self):
        print "Se ha eliminado el Metodo de Solucion"


class Proyecto(object):
    
    def __init__(self, metodoSolucion):
        self.metodoSolucion = metodoSolucion;
        print "Se ha creado el Proyecto"
        
    def __del__(self):
        self.metodoSolucion.__del__()
        print "Se cerro el Proyecto"
