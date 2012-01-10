class condicionExterna(object):

    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor
        
    def __del__(self):
        print "Se ha eliminado una Condicion Externa"

