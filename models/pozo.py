class pozo(object):
        def __init__(self, x,y):
                self.x = x
                self.y = y
                self.__ensayos=[]
                self.__observaciones=[]
        def agregarObservaciones(self, observaciones):
                self.__observaciones.append(observaciones)
        def agregarEnsayo(self, ensayo):
                self.__ensayos.append(ensayo)
