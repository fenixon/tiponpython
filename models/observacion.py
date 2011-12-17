class observacion(object):
    def __init__(self,tiempo,nivelpiezometrico):
        self.tiempo=tiempo
        self.nivelpiezometrico=nivelpiezometrico
    def devolverAt(self, indice):
        if indice==0 :
            return self.tiempo
        if indice==1 :
            return self.nivelpiezometrico
    def datosNombre(self):
        return ["Tiempo", "Nivel Piezometrico"]

