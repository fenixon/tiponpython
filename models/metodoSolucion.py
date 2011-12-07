class metodoSolucion(object):
    
    def __init__(self, dominio):
	self.dominio = dominio
        self.listaParametros = [] 
        self.matrizDescenso = zeros(1,3)
        print "Se ha creado el Metodo de Solucion"
        
    def __del__(self):
        print "Se ha eliminado el Metodo de Solucion"

class metodoAnalitico(metodoSolucion):

    def __init__(self):
        print "Se ha creado un Metodo Analitico"

    def __del__(self):
        pass

class metodoNumerico(metodoSolucion):

    def __init__(self):
        print "Se ha creado un Metodo Numerico"

    def __del__(self):
        pass
