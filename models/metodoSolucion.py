import numpy

class metodoSolucion(object):

    def __init__(self, dominio):
        self.dominio = dominio
        self.listaParametros = []        
        print 'self.matrizDescenso = numpy.zeros(1,3)'
        print "Se ha creado el Metodo de Solucion"
        
    def __del__(self):
        print "Se ha eliminado el Metodo de Solucion"

class metodoAnalitico(metodoSolucion):
    pass

class metodoNumerico(metodoSolucion):
    pass
