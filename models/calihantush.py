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
		self.t_obs=[]
		self.r_obs=[]
		self.obs=[]
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

	def setpozo(self,pozo):
		self.pozo=pozo
		print "pozo a optimizar:" + str(pozo.id)

	def setcontrolador(self,controlador):
		self.controlador=controlador
		self.setobservaciones()

	def setobservaciones(self):
		#obtengo las observaciones importadas
		observaciones= self.pozo.observaciones[0].devolverO()
##		self.obs=self.pozo.devolverSolucionadas()
		#coordenadas del pozo de observacion
		x0=self.pozo.x
		y0=self.pozo.y		
		#obtengo el pozo de bombeo
		self.pozoBombeo=self.controlador.obtenerDominio().obtenerPozoBombeo()
		bombeos=self.pozoBombeo.ensayos[0].devolverBProc()
		self.Q=bombeos[0].caudal
		self.tpozo=bombeos[0].tiempo
		print "caudal::::" + str(self.Q)
		xb=self.pozoBombeo.x
		yb=self.pozoBombeo.y
		#coordenadas de guias
		print "x0:" + str(x0)
		print "y0:" + str(y0)
		print "xb:" + str(xb)
		print "yb:" + str(yb)
		for o in observaciones:
			self.t_obs.append(o.tiempo)
			self.r_obs.append(np.sqrt(np.square(x0-xb) + np.square(y0-yb)))
		#calculo theis por cada self.t_obs y self.r_obs
		print 'mostrar los t '+str(self.t_obs)
		print 'mostrar los r '+str(self.r_obs)
		
	def setobservaciones2(self):
		self.r_obs=[179.63574254585305, 179.63574254585305, 179.63574254585305, 179.63574254585305, 179.63574254585305, 179.63574254585305]
		self.t_obs=[0.1, 0.2, 0.4, 0.6, 0.9, 1.2]
		self.Q=10
		self.tpozo=0
		
	def cargar(self):
		#T=800;
		#S=1e-3;		
		T=self.controlador.obtenerDominio().metodo.listaParametros[0].valoresParametro.valor
		S=self.controlador.obtenerDominio().metodo.listaParametros[1].valoresParametro.valor		
		#Q=10;
		Q=self.Q
		tpozo=self.tpozo
		N_obs=len(self.t_obs)
		self.obs=numpy.zeros((N_obs),float)
		self.domActual=self.controlador.obtenerDominio()
		self.d=dominio()
		self.d.alto = self.domActual.alto
		self.d.alto = self.domActual.ancho
		self.d.a = self.domActual.a		
		self.d.b = self.domActual.b
		self.d.c = self.domActual.c
		
		for i in range(N_obs):
			m=Hantush(self.d, self.controlador.parametros)
			tmandado=round(float(float(self.t_obs[i])-float(tpozo)),14)
			m.setearValores([T,S])
			if tmandado>0:
				self.obs[i]=m.calcularpozo(self.r_obs[i],tmandado,Q)[0]
			else:
				self.obs[i]=0
		return self.calcular()

	def calcular(self):
		Q=self.Q
		tpozo=self.tpozo
		obs=self.obs
		#print obs
		t_obs=self.t_obs
		r_obs=self.r_obs
		Tmin=int(self.listaParametros[0].valoresParametro.valor)
		Tmax=int(self.listaParametros[1].valoresParametro.valor)
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

		[T_T, T_S] = meshgrid(Test_T, Test_S)
		[T_T, T_c] = meshgrid(Test_T, Test_c)

		obj=numpy.zeros(N_int_T,N_int_S,N_int_C)
		minobj=999999999999999
		iToptimo=0
		iSoptimo=0
		n=Hantush(self.d, self.controlador.parametros)
		for n_T in range(1,T_Nint):
			acui.T=Test_T(n_T)
			for n_S in range(1,S_Nint):
				acui.S=Test_S(n_S)
				for n_c in range(1,c_Nint):
					acui.c=Test_c(n_c)
					for n_obs in range(1,Nobs):
						Hopuntoobs=dominio.H0a*x_obs +dominio.H0b*y_obs + dominio.H0c
						numeroobs=size(obs(n_obs).h)
						for n_med in range(1,numeroobs(1)):
							h_med=obs(n_obs).h(n_med)
							#absoluto
							descensos=n.calcularpozo(r_obs[n_obs],t_obs[n_med],Q)[0]
							#obj(n_S,n_T,n_c)= obj(n_S,n_T,n_c) + (h_med - (Hopuntoobs - descensos) )^2
							if (obj(n_S,n_T,n_c)< minobj):
								minobj=obj(n_S,n_T,n_c)
								iToptimo=n_T
								iSoptimo=n_S
								icoptimo=n_c
							#obj(n_S,n_T,n_c)=np.log(obj(n_S,n_T,n_c))
					acui.T=Test_T(iToptimo)
					acui.S=Test_S(iSoptimo)
					acui.c=Test_c(icoptimo)

if __name__ == "__main__":
    #cont=1
    #a=CaliHantush()
    #a.setobservaciones2()
    #a.cargar()
    print "hola"
