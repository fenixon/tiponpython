from bombeo import bombeo
from ensayobombeo import ensayobombeo

class pozo(object):

        id = 0
        
        def __init__(self, x,y):
                self.x = x
                self.y = y
                self.ensayos=[]
                self.observaciones=[]
                #lista de Observaciones solucionadas para cada pozo de observacion
                self.obssolucionadas=[]
                self.nivelesOptimos=[]
               
        def agregarObservaciones(self, observaciones):
                self.observaciones.append(observaciones)

        def eliminarObservaciones(self, observaciones):
                self.observaciones.remove(observaciones)                
                
        def agregarEnsayo(self, ensayo):
                self.ensayos.append(ensayo)

        def eliminarEnsayo(self, ensayo):
                self.ensayos.remove(ensayo)                
               
                
        def actualizarCoordenadas(self, x, y):
                self.x = x
                self.y = y

        def copiaSuperficial(self):
                p=pozo(self.x,self.y)
                for e in self.ensayos:
                        p.ensayos.append(e.copiaSuperficial())
                for o in self.observaciones:
                        p.observaciones.append(o.copiaSuperficial())
                return p

        def restaurarPozo(self, p):
                self.ensayos=[]
                self.observaciones=[]                
                for e in p.ensayos:
                        self.ensayos.append(e.copiaSuperficial())
                for o in p.observaciones:
                        self.observaciones.append(o.copiaSuperficial())


        def instanciarSolucionadas(self, num, tiempos):
                self.obssolucionadas=[]
                for t in tiempos:
                        #nuevao=observacion(t, num)
                        self.obssolucionadas.append(num)

        def instanciarNivelesOptimos(self, num, tiempos):
                self.nivelesOptimos=[]
                for t in tiempos:
                        self.nivelesOptimos.append(num)                
        
        def devolverSolucionadas(self):
                return self.obssolucionadas

        def devolverNivelesOptimos(self):
                return self.nivelesOptimos

        def copiarAPozoVirtual(self,p,tipo):

##                print 'pozo virutal x: '+str(self.x) + 'pozo virutal y: '+str(self.y) 
                
                bombeosn=[]                
                bombeosp=p.ensayos[0].devolverBProc()
                
                if tipo == "positivo":
                    #si en positiva se restan todos los caudales
                    for b in bombeosp:
                          bombeosn.append(bombeo(b.tiempo, -b.caudal))
##                          print 'caudal: '+str(-b.caudal)
                          
                else:
                    ##si es negativa la copia es exacta
                    bombeosn=bombeosp
                    

                e=ensayobombeo(bombeosn,p.ensayos[0].id, p.ensayos[0].nombre)
                e.setearBProc(bombeosn)
                self.ensayos=[e]
