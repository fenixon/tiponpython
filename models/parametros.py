class parametros(object):

    def __init__(self, nombre, unidad, valoresParametro=None):
        self.nombre = nombre
        self.unidad = unidad
        self.valoresParametro = valoresParametro

    def __del__(self):
        print "Objeto eliminado"
