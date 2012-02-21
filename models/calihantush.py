import sys
sys.path.append("views")
sys.path.append("models")
import numpy
from valoresParametros import valoresParametros
import metodoSolucion
import metodooptimizacion
from dominio import *
from numpy import hypot, mgrid, linspace
from parametros import *
import numpy as np
from Hantush import *
import controlador


class CaliHantush(metodooptimizacion.metodooptimizacion):
	def __str__( self ):
		return  "CaliHantush"		
	def __init__(self):
		metodooptimizacion.metodooptimizacion.__init__(self)
		self.pozosobs=[]
		self.listaParametros.append(parametros('Tmin','')) #parametro 0
		self.listaParametros.append(parametros('Tmax','')) #parametro 1
		self.listaParametros.append(parametros('Smin','')) #parametro 2
		self.listaParametros.append(parametros('Smax','')) #parametro 3
		self.listaParametros.append(parametros('N_int_T','')) #parametro 4
		self.listaParametros.append(parametros('N_int_S','')) #parametro 5
		self.listaParametros.append(parametros('N_int_C','')) #parametro 6
		self.listaParametros.append(parametros('goteo_min','')) #parametro 8
		self.listaParametros.append(parametros('goteo_max','')) #parametro 9
		##Estos valores hay que tomarlos desde donde ingresa el usuario
		self.setearValores(['900','1000','1.0e-4','1.4e-4','15','15','15','650','700'])
		print "se creo CaliHantush"

	def setpozos(self,pozos):
		for p in pozos:
			pozoobs=self.controlador.buscarPozo(p)
			self.pozosobs.append(pozoobs)
		
		print "Se cargaron los pozos:" + str(self.pozosobs)

	def setcontrolador(self,controlador):
		self.controlador=controlador

	def calcular(self):
		#Q=self.Q
		#3tpozo=self.tpozo
		#obs=self.obs
		#print obs
                self.d=self.controlador.obtenerDominio()
		
		#t_obs=self.t_obs
		#r_obs=self.r_obs
		Tmin=float(self.listaParametros[0].valoresParametro.valor)
		Tmax=float(self.listaParametros[1].valoresParametro.valor)
		Smin=float(self.listaParametros[2].valoresParametro.valor)
		Smax=float(self.listaParametros[3].valoresParametro.valor)
		T_Nint=int(self.listaParametros[4].valoresParametro.valor)
		S_Nint=int(self.listaParametros[5].valoresParametro.valor)
		c_Nint=int(self.listaParametros[6].valoresParametro.valor)
		goteo_min=int(self.listaParametros[7].valoresParametro.valor)
		goteo_max=int(self.listaParametros[8].valoresParametro.valor)

		Test_T=numpy.linspace(Tmin,Tmax,T_Nint)
		Test_S=numpy.linspace(Smin,Smax,S_Nint)
		Test_c=numpy.linspace(goteo_min,goteo_max,c_Nint)

		#[T_T, T_S] = meshgrid(Test_T, Test_S)
		#[T_T, T_c] = meshgrid(Test_T, Test_c)

		obj=numpy.zeros((T_Nint,S_Nint,c_Nint),float)
		minobj=999999999999999
		iToptimo=0.0
		iSoptimo=0.0
		icoptimo=0.0
		metodo=None
		n=Hantush(self.d, self.controlador.parametros, None)
		for n_T in range(T_Nint):
			#acui.T=Test_T(n_T)
			for n_S in range(S_Nint):
				#acui.S=Test_S(n_S)
				for n_c in range(c_Nint):
					#acui.c=Test_c(n_c)
					n.setearValores([Test_T[n_T], Test_S[n_S], Test_c[n_c]])

					#print "paraemtros ", Test_T[n_T], Test_S[n_S], Test_c[n_c]
					#Itero por todos los pozos de observacion
					for p in self.pozosobs:
						#Itero por las observaciones de un pozo
						for obs in p.observaciones[0].devolverO():
							t=obs.tiempo
							descenso= n.funcionObjetivo2(p,t)
							obj[n_S,n_T,n_c]= obj[n_S,n_T,n_c] + numpy.power((obs.nivelpiezometrico - (self.d.calcularH0( p.x, p.y ) - descenso) ),2)


                                                        #if n_T==0 and n_S==0 and n_c==0:
                                                                #print "obj[1,1,1] :",obj[n_S,n_T,n_c],"tiempo :",obs.tiempo,"h :",obs.nivelpiezometrico,"descenso :",descenso
				#Luego del for de goteo va la comparacion			
                                if (obj[n_S,n_T,n_c]< minobj):
                                        minobj=obj[n_S,n_T,n_c]
                                        iToptimo=n_T
                                        iSoptimo=n_S
                                        icoptimo=n_c
                                obj[n_S,n_T,n_c]=np.log(obj[n_S,n_T,n_c])
		#acui.T=Test_T(iToptimo)
		#acui.S=Test_S(iSoptimo)
		#acui.c=Test_c(icoptimo)
                self.T=Test_T[iToptimo]
                self.S=Test_S[iSoptimo]
                self.c=Test_c[icoptimo]
                self.obj=obj[:,:,icoptimo]
                
                self.metodo=Hantush(self.d, self.controlador.parametros, None)
                self.metodo.setearValores([self.T,self.S,self.c])              
                self.d.optimizacioneshechas[self.__str__()]=self
                return [self.T,self.S,"",self.obj]
		#return [acui.T,acui.S,acui.c,obj]


if __name__ == "__main__":
    #cont=1
    #a=CaliHantush()
    #a.setobservaciones2()
    #a.cargar()
    print "hola"
