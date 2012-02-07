class observacionesensayo(object):
    def __init__(self,observaciones, ido, nombre):
        self.__observaciones=observaciones
        self.id=ido
        self.nombre=nombre
    def devolverO(self):
        return self.__observaciones
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

    def copiaSuperficial(self):
        o=observacionesensayo(self.__observaciones, self.id, self.nombre)
        return o
