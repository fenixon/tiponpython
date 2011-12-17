class ensayobombeo(object):
    def __init__(self,bombeos, idb):                
        self.__bombeos=bombeos
        self.id=idb
    def devolverB(self):
        return self.__bombeos
    def devolverAt(self, indice):
        if indice==0 :
            return self.id
    def datosNombre(self):
        return ["Id"]
##        self.id=self.generarId()

##    def generarId(self):
        #a implementar un mecanismo para generar id
##        return 1
        
