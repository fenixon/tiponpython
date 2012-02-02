import numpy as np

class barrera():
                
                id = 0
                        
                def __init__(self, x1, x2, y1, y2, tipo):
                                self.x1 = x1
                                self.x2 = x2
                                self.y1 = y1
                                self.y2 = y2
                                self.tipo = tipo
                                self.calcularRecta()


                def actualizarBarrera(self, x1, x2, y1, y2, tipo):
                                self.x1 = x1
                                self.x2 = x2
                                self.y1 = y1
                                self.y2 = y2
                                self.tipo = tipo
                                self.calcularRecta()

                def actualizarBarrera2(self, x1, x2, y1, y2):
                                self.x1 = x1
                                self.x2 = x2
                                self.y1 = y1
                                self.y2 = y2




                def calcularRecta( self ):
      
                                self.m  =  (self.y2 - self.y1)  /   (self.x2 - self.x1) 
                                self. n = 0
                                xPorm = self.m * self.x1

                                if xPorm < 0 :
                                                self.n = self.y1 +  xPorm
                                else:
                                                self.n = self.y1 -  xPorm

 
                                self.x3 = self.x1 - 600

                                self.y3 = (self.m * self.x3) + self.n
                                
                                self.x4 = self.x2 + 600
                                
                                self.y4 = (self.m * self.x4) + self.n

                                ## calculo de los coeficientes de la recta
                                ## (-y1+y2)x + (x1-x2)y + (-x1y2 + y1x2)=0
                                self.alfa=-self.y1+self.y2
                                self.beta=self.x1-self.x2
                                self.gamma=-self.x1*self.y2 + self.y1*self.x2                                

                def devolverCoef(self):
                    ##poner el calculo q habia puesto
##                    print 'x1 '+str(self.x1)+'x2 '+str(self.x2)+'y1 '+str(self.y1)+'y2 '+str(self.y2)
                    return [self.alfa,self.beta,self.gamma]

