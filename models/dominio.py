class dominio(object):

    def __init__(self):
        self.alto = 0
        self.ancho = 0
        self.listaBarreras = []
        self.listaCondicionesExternas = []
        print "Se ha creado el Dominio"

    def __del__(self):
        print "Se ha eliminado el Dominio"

