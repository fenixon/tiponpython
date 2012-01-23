from bombeo import bombeo
from ensayobombeo import ensayobombeo

class pozo(object):

        id = 0
        
        def __init__(self, x,y):
                self.x = x
                self.y = y
                self.ensayos=[]
                self.observaciones=[]
               
        def agregarObservaciones(self, observaciones):
                self.observaciones.append(observaciones)
        def agregarEnsayo(self, ensayo):
                self.ensayos.append(ensayo)
        def actualizarCoordenadas(self, x, y):
                self.x = x
                self.y = y

        def copiarAPozoVirtual(self,p,tipo):

                print 'pozo virutal x: '+str(self.x) + 'pozo virutal y: '+str(self.y) 
                
                bombeosn=[]                
                bombeosp=p.ensayos[0].devolverBProc()
                
                #CUANDO ES POSITIVA LA BARRERA EN EL 1?
                if tipo == 1:
                    #si en positiva se restan todos los caudales
                    for b in bombeosp:
                          bombeosn.append(bombeo(b.tiempo, -b.caudal))
                          print 'caudal: '+str(-b.caudal)
                          
                else:
                    ##si es negativa la copia es exacta
                    bombeosn=bombeosp
                    

                e=ensayobombeo(bombeosn,p.ensayos[0].id, p.ensayos[0].nombre)
                e.setearBProc(bombeosn)
                self.ensayos=[e]
