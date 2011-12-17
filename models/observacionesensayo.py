class observacionesensayo(object):
    def __init__(self,observaciones, ido):
        self.__observaciones=observaciones
        self.id=ido
    def devolverO(self):
        return self.__observaciones
    def devolverAt(self, indice):
        if indice==0 :
            return self.id
    def datosNombre(self):
        return ["Id"]        
##        self.id=self.generarId()

##    def generarId(self):
        #a implementar un mecanismo para generar id
##        return 1        
