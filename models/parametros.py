class parametros(object):

    def __init__(self, nombre, unidad):
        self.nombre = nombre
        self.unidad = unidad

    def __del__(self):
        print "Objeto eliminado"
