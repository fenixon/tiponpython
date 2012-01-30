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
from theis  import *
import controlador


class CaliTheis2(metodooptimizacion.metodooptimizacion):
	def __str__( self ):
		return  "CaliTheis2"		
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
		self.listaParametros.append(parametros('N_ref_max','')) #parametro 6
		self.listaParametros.append(parametros('esc_ref','')) #parametro 7
		#self.listaParametros.append(parametros('t_obs','')) #parametro 4
		##Estos valores hay que tomarlos desde donde ingresa el usuario
		self.setearValores(['500','1500','1e-4','1e-2','10','10','20','.5'])
		print "se creo CaliTheis2"

		#self.p=[]
		#self.p.append(parametros('S','m^2/d'))
		#self.p.append(parametros('T',''))  

	def setpozo(self,pozo):
		self.pozo=pozo
		print "pozo a optimizar:" + str(pozo.id)
		#self.setobservaciones()

	def setcontrolador(self,controlador):
		self.controlador=controlador
		self.setobservaciones()

	def setobservaciones(self):
		#obtengo las observaciones importadas
		observaciones= self.pozo.observaciones[0].devolverO()
		self.obs=self.pozo.devolverSolucionadas()
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
		self.d=self.controlador.obtenerDominio()
		#self.d=dominio()
		#self.d.alto = 10
		#self.d.ancho = 10
		#self.d.a=0
		#self.d.b=0
		#self.d.c=10
		
		for i in range(N_obs):
			#m.setearValores([T,S])
			#self.obs[i]=m.calcularpozo(self.r_obs[i],self.t_obs[i],Q)[0]
			m=Theis(self.d, self.controlador.parametros)                        
			#m=Theis(self.d, self.p)
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
		t_obs=self.t_obs
		r_obs=self.r_obs
		Tmin=int(self.listaParametros[0].valoresParametro.valor)
##		print 'Tmin: '+str(Tmin)
		Tmax=int(self.listaParametros[1].valoresParametro.valor)
		Smin=float(self.listaParametros[2].valoresParametro.valor)
		Smax=float(self.listaParametros[3].valoresParametro.valor)
		
		N_int_T=int(self.listaParametros[4].valoresParametro.valor)
		N_int_S=int(self.listaParametros[5].valoresParametro.valor)
		N_ref_max=int(self.listaParametros[6].valoresParametro.valor)
		esc_ref=float(self.listaParametros[7].valoresParametro.valor)

		N_obs=len(obs)
		obs_sim=numpy.zeros((N_obs),float)
		T_vec=numpy.zeros((N_int_T),float)		
		T_vec=numpy.zeros((N_int_T),float)
		S_vec=numpy.zeros((N_int_S),float)		

		Tinf=Tmin
		Tsup=Tmax
		Sinf=Smin
		Ssup=Smax
		ref=0
		n=Theis(self.d, self.controlador.parametros)
		#n=Theis(self.d, self.p)
		T=self.controlador.obtenerDominio().metodo.listaParametros[0].valoresParametro.valor
		S=self.controlador.obtenerDominio().metodo.listaParametros[1].valoresParametro.valor
		#T=self.p[0].valoresParametro.valor
		#S=self.p[1].valoresParametro.valor

		print 'T '+str(T)
		print 'S '+str(S)

		while (ref<N_ref_max): 

			DT=Tsup-Tinf
			DS=Ssup-Sinf

			auxT=DT/(N_int_T-1)

			for i in range(1,N_int_T +1):
				T_vec[i-1]=Tinf + (i-1)*auxT

			auxS=DS/(N_int_S-1)

			for a in range(1,N_int_S +1):
				S_vec[a-1]=Sinf + (a-1)*auxS
			
			f_min=1.797693e+308 
			for i in range(N_int_T):
				for j in range (N_int_S):
					f=0.0
					for k in range (N_obs):
						tmandado=round(float(float(t_obs[k])-float(tpozo)),14)
						n.setearValores([T_vec[i],S_vec[j]])
						#print 't mandado ' + str(tmandado)
						if tmandado>0:
							obs_sim[k]=n.calcularpozo(r_obs[k],tmandado,Q)[0]
						else:
							obs_sim[k]=0
						f=f+ numpy.power((obs_sim[k]-obs[k]),2)/numpy.power((obs[k]),2)
						
					if (f<f_min):
						f_min=f
						T=T_vec[i]
						S=S_vec[j]
						#print 'T: '+ str(T_vec[i]) + '-S: ' + str(S_vec[j]) + '-f: ' + str(f) +  '-fmin: ' + str(f_min) + '-Tmin: ' + str(T), '-Smin: ' + str(S)
			DT=DT*esc_ref
			if (T-DT/2.0 <Tmin):
				Tinf=Tmin
				Tsup=Tmin+DT
			elif(T+DT/2.0 >Tmax):
				Tsup=Tmax
				Tmin=Tmax-DT
			else:
				Tsup=T+DT/2.0
				Tmin=T-DT/2.0
			DS=DS*esc_ref
			if (S-DS/2 <Smin):
				Sinf=Smin
				Ssup=Smin+DS
			elif(S+DS/2 >Smax):
				Ssup=Smax
				Smin=Smax-DS
			else:
				Ssup=S+DS/2.0
				Smin=S-DS/2.0
			ref=ref+1


		#print 'T: '+ str(T) + '-S: ' + str(S) +  '-fmin: ' + str(f_min) + ' obs_sim: ' + str(obs_sim)
		
		return [T, S, f_min,obs_sim]


if __name__ == "__main__":
    cont=1
    a=CaliTheis2()
    a.setobservaciones2()
    a.cargar()
