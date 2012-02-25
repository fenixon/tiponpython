class bombeo(object):
    def __init__(self,tiempo, caudal):
        self.tiempo=tiempo
        self.caudal=caudal
    def devolverAt(self, indice):
        if indice==0 :
            return self.tiempo
        if indice==1 :
            return self.caudal
    def datosNombre(self):
        return ["Tiempo", "Caudal"]


