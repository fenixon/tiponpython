class condicionExterna(object):

    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor
        print "Se ha creado una Condicion Externa"
        
    def __del__(self):
        print "Se ha eliminado una Condicion Externa"

