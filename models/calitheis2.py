"""
	tiponpython Simulacion de ensayos de acuiferos
	Copyright 2012 Jesus Guibert
	
	This file is part of tiponpython.

	tiponpython is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	any later version.

	tiponpython is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with tiponpython.  If not, see http://www.gnu.org/licenses/gpl.txt.
"""

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
		self.pozosobs=[]
		self.listaParametros.append(parametros('Tmin','')) #parametro 0
		self.listaParametros.append(parametros('Tmax','')) #parametro 1
		self.listaParametros.append(parametros('Smin','')) #parametro 2
		self.listaParametros.append(parametros('Smax','')) #parametro 3
		self.listaParametros.append(parametros('N_int_T','')) #parametro 4
		self.listaParametros.append(parametros('N_int_S','')) #parametro 5
		self.listaParametros.append(parametros('N_ref_max','')) #parametro 6
		self.listaParametros.append(parametros('esc_ref','')) #parametro 7
		#self.setearValores(['500','1500','1e-4','1e-2','10','10','20','.5'])
		self.setearValores(['100','3000','5e-4','5.0e-6','100','100','20','.5'])
		print "se creo CaliTheis2"

	def setpozos(self,pozos):
		for p in pozos:
			pozoobs=self.controlador.buscarPozo(p)
			self.pozosobs.append(pozoobs)
		
		print "Se cargaron los pozos:" + str(self.pozosobs)
	
	def setcontrolador(self,controlador):
		self.controlador=controlador		


	def calcular(self):

                ##Hay que copiar el dominio, sino se cambian los parametros del propio
                ##AHORA NOES NECESARIO COOPIAR PORQUE AL DOMINIO NO SE LE MODIFICAN LOS PARAMETOS
		self.domActual=self.controlador.obtenerDominio()
		self.d=self.controlador.obtenerDominio()
##		self.d.alto = 10
		#self.d.alto = self.domActual.alto
##		self.d.ancho = 10
		#self.d.alto = self.domActual.ancho
		#self.d.a=0
                #self.d.a = self.domActual.a		
		#self.d.b=0
		#self.d.b = self.domActual.b
		#self.d.c=10
		#self.d.c = self.domActual.c                

		Tmin=float(self.listaParametros[0].valoresParametro.valor)
		Tmax=float(self.listaParametros[1].valoresParametro.valor)
		Smin=float(self.listaParametros[2].valoresParametro.valor)
		Smax=float(self.listaParametros[3].valoresParametro.valor)
		
		N_int_T=int(self.listaParametros[4].valoresParametro.valor)
		N_int_S=int(self.listaParametros[5].valoresParametro.valor)
		N_ref_max=int(self.listaParametros[6].valoresParametro.valor)
		esc_ref=float(self.listaParametros[7].valoresParametro.valor)

		T_vec=numpy.zeros((N_int_T),float)		
		T_vec=numpy.zeros((N_int_T),float)
		S_vec=numpy.zeros((N_int_S),float)
		obj=numpy.zeros((N_int_T,N_int_S),float)
		minobj=999999999999999
		Tinf=Tmin
		Tsup=Tmax
		Sinf=Smin
		Ssup=Smax
		ref=0

		#n=Theis(self.d, self.controlador.parametros, None)
		#T=self.controlador.obtenerDominio().metodo.listaParametros[0].valoresParametro.valor
		#S=self.controlador.obtenerDominio().metodo.listaParametros[1].valoresParametro.valor
		T=0.0
		S=0.0
                metodo=None

                #con los refinamientos queda re pesada
                #while (ref<N_ref_max):

                DT=Tsup-Tinf
                DS=Ssup-Sinf

                auxT=DT/(N_int_T-1)

                for i in range(1,N_int_T +1):
                        T_vec[i-1]=Tinf + (i-1)*auxT

                auxS=DS/(N_int_S-1)

                for a in range(1,N_int_S +1):
                        S_vec[a-1]=Sinf + (a-1)*auxS
                
                f_min=1.797693e+308
                n=Theis(self.d, self.controlador.parametros, None)
                for i in range(N_int_T):
                        for j in range (N_int_S):
                                f=0.0
                                ##Para hacerlo mas prolijo                                
                                n.setearValores([T_vec[i],S_vec[j]])                                
                                #Itero por todos los pozos de observacion
                                for p in self.pozosobs:
                                        #Itero por las observaciones de un pozo
                                        for obs in p.observaciones[0].devolverO():
                                                t=obs.tiempo
                                                mostrar=None
                                                if i==0 and j==0:
                                                        mostrar=1

                                                descenso= n.funcionObjetivo2(p,t)

                                                #print "descenso: ",descenso
                                                
                                                f=f+ numpy.power((descenso-obs.nivelpiezometrico),2)/numpy.power((obs.nivelpiezometrico),2)
                                                #obj(n_S,n_T)= obj(n_S,n_T) + (h_med - (Hopuntoobs - descensos) )^2;							
                                                obj[j,i]= obj[j,i] + numpy.power((obs.nivelpiezometrico - (self.d.calcularH0( p.x, p.y ) - descenso) ),2)				


                                                #if i==0 and j==0:
                                                        #print "obj[1,1] :",obj[j,i],"tiempo :",obs.tiempo,"h :",obs.nivelpiezometrico,"descenso :",descenso
                                                
                                                
                                if obj[j,i]<minobj:
                                        minobj=obj[j,i]
                                        T=T_vec[i]
                                        S=S_vec[j]
                                        #print "minobj-",minobj, "tmin-",T,"smin-",S
                                        
                                #obj(n_S,n_T)=log(obj(n_S,n_T));
                                obj[j,i]= np.log(obj[j,i])                                                
                                        
                                #if (f<f_min):
                                        #f_min=f
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

                self.T=T
                self.S=S
                self.obj=obj
                self.metodo=Theis(self.d, self.controlador.parametros, None)
                self.metodo.setearValores([T,S])


                

                #print "T dominio ", self.controlador.obtenerDominio().metodo.listaParametros[0].valoresParametro.valor
		#print "S dominio ",self.controlador.obtenerDominio().metodo.listaParametros[1].valoresParametro.valor

                self.domActual.optimizacioneshechas[self.__str__()]=self
                retorno={}
                retorno={'T':T,'S':S}
		#return [T, S, f_min,obj]
                return retorno
	


if __name__ == "__main__":
    cont=1
    a=CaliTheis2()
    a.setobservaciones2()
    a.cargar()
