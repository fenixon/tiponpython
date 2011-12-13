class Proyecto(object):
    def __init__(self):
        self.ultimoIdEns=0
        self.ultimoIdObs=0
        self.ensayos=[]
        self.observaciones=[]        
    def obtenerIdEns(self):
##        print "tentgo: "+ str(self.ultimoIdEns)            
        self.ultimoIdEns=self.ultimoIdEns + 1
##        print "devuelvo: "+ str(self.ultimoIdEns)
        return self.ultimoIdEns
    def agregarEnsayo(self,ensayo):
        self.ensayos.append(ensayo)
    def obtenerIdObs(self):
        self.ultimoIdObs=self.ultimoIdObs + 1
        return self.ultimoIdObs
    def agregarObservacion(self,obser):
        self.observaciones.append(obser)
    def traerid(self):
        return self.ultimoIdEns
