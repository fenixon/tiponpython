class ensayobombeo(object):
    def __init__(self,bombeos, idb, nombre):                
        self.__bombeos=bombeos
        self.id=idb
        self.nombre=nombre
    def devolverB(self):
        return self.__bombeos
    def devolverAt(self, indice):
        if indice==0 :
            return self.id
        else:
            if indice==1:
                return self.nombre
    def datosNombre(self):
        return ["Id", "Nombre"]
##        self.id=self.generarId()

##    def generarId(self):
        #a implementar un mecanismo para generar id
##        return 1
        
