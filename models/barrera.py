import numpy as np

class barrera():
                
                id = 0
                        
                def __init__(self, x1, x2, y1, y2, tipo, alto, ancho):
                                self.x1 = x1
                                self.x2 = x2
                                self.y1 = y1
                                self.y2 = y2
                                self.tipo = tipo
                                self.calcularRecta(alto , ancho)


                def actualizarBarrera(self, x1, x2, y1, y2, tipo):
                                self.x1 = x1
                                self.x2 = x2
                                self.y1 = y1
                                self.y2 = y2
                                self.tipo = tipo
                                self.calcularRecta(0, 0)

                def actualizarBarrera2(self, x1, x2, y1, y2):
                                self.x1 = x1
                                self.x2 = x2
                                self.y1 = y1
                                self.y2 = y2
                                self.calcularRecta(0, 0)

                def actualizarBarrera3(self, x1, x2, y1, y2, alto, ancho):
                                self.x1 = x1
                                self.x2 = x2
                                self.y1 = y1
                                self.y2 = y2
                                self.calcularRecta(alto, ancho)



                def calcularRecta( self, alto, ancho ):


				#try:
				"""
				if self.x1 == 0 and self.y1 >= alto:
					self.y1 = alto
					return

				if self.x1 == ancho and self.y1 >= alto:
					self.y1 = alto
					return

				if self.y1 >= alto:
					self.y1 = alto
					return

				if self.x1 == 0:
					return

				if self.x2 == 0 and self.y2 >= alto:
					self.y2 = alto
					return

				if self.x2 == ancho and self.y2 >= alto:
					self.y1 = alto
					return

				if self.y2 >= alto:
					self.y2 = alto
					return

				if self.x2 == 0:
					return

 				"""
				if (self.x2 - self.x1) == 0:
					return
				self.m  =  (self.y2 - self.y1)  /   (self.x2 - self.x1) 

				self.n = self.x1 * self.m * -1 + self.y1 

				self.y5 = 0

				if self.m == 0:
					return
				self.x5 = (self.y5 - self.n ) / self.m

				self.x6 = 0

				self.y6 = (self.m * self.x6) + self.n

				if alto > 0 and ancho > 0:

					if self.x5 > ancho or self.x5 < 0:
						self.x5 = ancho
						self.y5 = (self.m * self.x5) + self.n 
						if self.y5 > alto or self.y5 < 0:
							if self.m == 0:
								return
							self.y5 = alto
							self.x5 = (self.y5 - self.n ) / self.m
						self.x1 = np.int(self.x5)
						self.y1 = np.int(self.y5)

					if self.y6 > alto or self.y6 < 0:
						if self.m == 0:
							return
						self.y6 = alto
						self.x6 = (self.y6 - self.n ) / self.m
						if self.x6 > ancho or self.x6 < 0:
							self.x6 = ancho
							self.y6 = (self.m * self.x6) + self.n
						self.x2 = np.int(self.x6)
						self.y2 = np.int(self.y6)
 
					self.x1 = np.int(self.x5)
					self.y1 = np.int(self.y5) 
					self.x2 = np.int(self.x6)
					self.y2 = np.int(self.y6)


					## calculo de los coeficientes de la recta
					## (-y1+y2)x + (x1-x2)y + (-x1y2 + y1x2)=0
					self.alfa=-self.y1+self.y2
					self.beta=self.x1-self.x2
					self.gamma=-self.x1*self.y2 + self.y1*self.x2



				#except:
				#	print "ERROR!!!!"

                def devolverCoef(self):
                    return [self.alfa,self.beta,self.gamma]

