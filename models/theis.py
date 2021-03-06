"""
	tiponpython Simulacion de ensayos de acuiferos
	Copyright 2012 Andres Pias

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

import metodoSolucion

from numpy import hypot, mgrid, linspace

import numpy as np
import controlador


#from scipy.special import j0

class Theis(metodoSolucion.metodoAnalitico):

    def __init__(self, dominio, parametros, asociar=None): 
        ##Lista de cardinales de los parametros que utiliza el metodo
        ##Parametros 0: S, parametro 1:T
        self.paramcard=[0,1]
        #### Llamar al constructor del metodo de solucion
        ## probar llamar al metodo padre        
        metodoSolucion.metodoAnalitico.__init__(self,dominio,parametros, asociar)
        #print 'Se creo el loco theis'
        ##Theis es un metodo que acepta barrera        
        self.aceptaBarrera=True
        #Seteo las optimizaciones disponibles que puede aplicarse a theis
        self.optimizaciones=['CaliTheis2']
        #print "se creo theis"

    def calcularpozo(self,r,t,Q):

        #### Recuperar los valores de T y el S guardados en el dominio y en el metodo,
        ## ver como obtenerlo siguiendo el modelo de dominio
        T=self.listaParametros[0].valoresParametro.valor
        S=self.listaParametros[1].valoresParametro.valor

        #print "T: "+str(T)
        #print "S: "+str(S)
        
        # [s, dsdT, dsdS]=Theis(r,t,Q,T,S)
        # nro de valores que devuelve la funcion, esto lo vemos dps xq varia
        nargout=3        
        if r<=0.15 :
            r=0.15
 
        #u=r^2*S/T/t/4;
        u=numpy.power(r,2)*S/T/t/4.000
        
        
        if (nargout == 1):
            w=self.WTheis(u) 
            s=Q/4.000/numpy.pi/T*w
        else:
            lista=[]
            try:
                ## se captura en dos parametros la lista q devuelve            
                w,dWdu=self.WTheis(u)

                #print "u.. " + str(u)
                #print "w.. " + str(w)
                ## w=lista[0]           
                ## dWdu=lista[1]
                #print "dw.. " + str(dWdu)

                #print "Q "+ str(Q)
                #print "T "+ str(T)

                #print "pi "+ str(numpy.pi)
                
                s=Q/4.000/numpy.pi/T*w


                #print "s "+ str(s)
                #print str(s)
                #dsdT=s*(-1/T + dWdu*(-u/T)/w);
                if w==0:
                    aux1=0
                else:
                    aux1=dWdu*(-u/T)/w
                # print "T " + str(T)
                
                aux2=-1.000/T

                #print "aux1 " + str(aux1)
                #print "aux2 " + str(aux2)
                
                dsdT=s*(aux2 + aux1)

                ## print "dsdT " + str(dsdT)
                if w==0:
                    dsdS=0
                else:                
                    dsdS=s/w*dWdu*u/S
                
                #print "s "+ str(s)

                #+" "+str(dsdT)+" "+str(dsdS)
            except:
                print 'Error - r: ' + str(r) +'t: '+str(t) + 'Q: ' + str(Q) + 'T: '+str(T) + 'S: '+str(S) 

        #if t==0.03:
        #    print 'Error - r: ' + str(r) +'t: '+str(t) + 'Q: ' + str(Q) + 'T: '+str(T) + 'S: '+str(S) + 's: '+str(s) 

        return [s, dsdT, dsdS]



    def calcularpozoGenerico(self,r,t,Q, T, S):

        #print "T: "+str(T)
        #print "S: "+str(S)
        
        # [s, dsdT, dsdS]=Theis(r,t,Q,T,S)
        # nro de valores que devuelve la funcion, esto lo vemos dps xq varia
        nargout=3        
        if r<=0.15 :
            r=0.15
 
        #u=r^2*S/T/t/4;
        u=numpy.power(r,2)*S/T/t/4.000
        
        
        if (nargout == 1):
            w=self.WTheis(u) 
            s=Q/4.000/numpy.pi/T*w
        else:
            lista=[]
            try:
                ## se captura en dos parametros la lista q devuelve            
                w,dWdu=self.WTheis(u)

                #print "u.. " + str(u)
                #print "w.. " + str(w)
                ## w=lista[0]           
                ## dWdu=lista[1]
                #print "dw.. " + str(dWdu)

                #print "Q "+ str(Q)
                #print "T "+ str(T)

                #print "pi "+ str(numpy.pi)
                
                s=Q/4.000/numpy.pi/T*w


                #print "s "+ str(s)
                #print str(s)
                #dsdT=s*(-1/T + dWdu*(-u/T)/w);
                if w==0:
                    aux1=0
                else:
                    aux1=dWdu*(-u/T)/w
                # print "T " + str(T)
                
                aux2=-1.000/T

                #print "aux1 " + str(aux1)
                #print "aux2 " + str(aux2)
                
                dsdT=s*(aux2 + aux1)

                ## print "dsdT " + str(dsdT)
                if w==0:
                    dsdS=0
                else:                
                    dsdS=s/w*dWdu*u/S
                
                #print "s "+ str(s)

                #+" "+str(dsdT)+" "+str(dsdS)
            except:
                print 'Error - r: ' + str(r) +'t: '+str(t) + 'Q: ' + str(Q) + 'T: '+str(T) + 'S: '+str(S) 


        #print str(s)
        
        return [s, dsdT, dsdS]
                            


    def WTheis(self,u,du=0):
        #
        #unction [W, dW]= WTheis(u,du)
        #numero de argumentos que salen la funcion
        nargout=2
        #numero de argumentos que salen de la funcion
        nargin=1
        
        if u>20 :
            #if (nargout == 1):
            #    W=0
            #else:    
            W=0
            dW=0
            return [W, dW]
        else:
            if u>=1:
                err=1e-10;mgrid[-5:6,-5:6]
            else:
                err=1e-6

        n=1.0
        f=-u
        acumulador=f
        g=f

        if (nargout != 1) :
            acumulador2= -1.0
            dg= -1.0
        
        if (nargout == 1):
            while abs(g) >= err:
                n=n+1
                f=-f*u/n
                g=f/n
                acumulador=acumulador+g
            W=-0.577215664901532860 -numpy.log(u) -acumulador
        else:
            while   abs(g) >= err and abs(dg) >= err :
                n=n+1
                f=-f*u/n
                g=f/n
                dg=f/u
                acumulador=acumulador+g
                acumulador2=acumulador2+dg
            W=-0.577215664901532860 -numpy.log(u) -acumulador
            dW=-1./u-acumulador2

        if (nargin != 1) :
            dW=dW*du

        return [W, dW]


if __name__ == "__main__":
    cont=1
    ui = Theis(cont,1)
##    Calcula bien el metodo de tezis para un pozo solo
    #ui.calcularprueba(1,1,500,1000,0.0001)

    #Theis()
    #ui.calcularpozoGenerico(559.0169,0.03,480,700,1.1e-4)
    

    #Error - r: 559.016994375t: 0.03Q: 480.0T: 700S: 0.0001s: 0.0410170857301
    ui.calcularpozoGenerico(559.016994375,0.03,480.0,700,0.0001)

    #Error - r: t: Q: T: 700S: s: -0.0410170857301

    #Error - r: 1091.15599791t: 0.09Q: 480.0T: 999.456893055S: 0.000100226593018desc 0.0
    #ui.calcularpozoGenerico(1091.15599791,0.09,480.0,999.456893055,0.000100226593018)
                                 
##    ui.calcular()
    


