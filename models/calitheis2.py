import sys
sys.path.append("views")
sys.path.append("models")
import numpy

import metodoSolucion
import metodooptimizacion
from dominio import *
from numpy import hypot, mgrid, linspace
from parametros import *
import numpy as np
from theis  import *
import controlador


class CaliTheis2(metodooptimizacion.metodooptimizacion):
#	def __init__(self):
		#print "creo"
	def test(self):
		T=800;
		S=1e-3;
		Q=10;

		N_obs=10;
		r_obs=[10,10,10,10,10,10,100,100,100,100]
		t_obs=[0.100,0.200,0.400,0.600,0.900,1.200,0.900,1.200,1.800,2.500]
		self.parametrosTheis=[]
		self.parametrosTheis.append(parametros('S','m^2/d'))    #parametro 0
		self.parametrosTheis.append(parametros('T','')) 
		obs=numpy.zeros((N_obs),float)
		self.d=dominio()
		
		for i in range(N_obs):
			m=Theis(self.d, self.parametrosTheis)
			m.setearValores([T,S])
			obs[i]=m.calcularpozo(r_obs[i],t_obs[i],Q)[0]
			print obs[i]

		Tmin=500
		Tmax=1500
		Smin=1e-4
		Smax=1e-2
		return self.calcular(Q,obs,r_obs,t_obs,Tmin,Tmax,Smin,Smax)

	def calcular(self,Q,obs,r_obs,t_obs,Tmin,Tmax,Smin,Smax):
		N_int_T=10
		N_int_S=10
		N_ref_max=20
		esc_ref=0.5

		N_obs=len(obs)
		obs_sim=numpy.zeros((N_obs),float)

		T_vec=numpy.zeros((N_int_T),int)		
		S_vec=numpy.zeros((N_int_S),float)		

		Tinf=Tmin
		Tsup=Tmax
		Sinf=Smin
		Ssup=Smax
		ref=0
		n=Theis(self.d, self.parametrosTheis)
		
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
					f=0
					for k in range (N_obs):
						n.setearValores([T_vec[i],S_vec[j]])
						obs_sim[k]=n.calcularpozo(r_obs[k],t_obs[k],Q)[0]
						f=f+ numpy.power((obs_sim[k]-obs[k]),2)/numpy.power((obs[k]),2)
					if (f<f_min):
						f_min=f
						T=T_vec[i]
						S=S_vec[j]
			DT=DT*esc_ref
			if (T-DT/2 <Tmin):
				Tinf=Tmin
				Tsup=Tmin+DT
			elif(T+DT/2 >Tmax):
				Tsup=Tmax
				Tmin=Tmax-DT
			else:
				Tsup=T+DT/2
				Tmin=T-DT/2
			DS=DS*esc_ref
			if (S-DS/2 <Smin):
				Sinf=Smin
				Ssup=Smin+DS
			elif(S+DS/2 >Smax):
				Ssup=Smax
				Smin=Smax-DS
			else:
				Ssup=S+DS/2
				Smin=S-DS/2
			ref=ref+1
		return [T, S, f_min,obs_sim]


if __name__ == "__main__":
    cont=1
    ui = CaliTheis2()
    T, S, f_min,obs_sim=ui.test()
    print "Valor optimo de T: " + str(T)
    print "Valor optimo de S: " +str(S)
    print "Valor optimo de f_min: " +str(f_min)
    print "Valor optimo de obs_sim: " +str(obs_sim)
                                 
##    ui.calcular()