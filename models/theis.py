import sys
sys.path.append("views")
sys.path.append("models")
import numpy

import metodoSolucion
##from scipy.interpolate import interp2d
from numpy import hypot, mgrid, linspace

import numpy as np
import controlador


#from scipy.special import j0

class Theis(metodoSolucion.metodoAnalitico):

    def __init__(self, dominio, parametros):
        ##Lista de cardinales de los parametros que utiliza el metodo
        ##Parametros 0: S, parametro 1:T
        self.paramcard=[0,1]
        #### Llamar al constructor del metodo de solucion
        ## probar llamar al metodo padre        
        metodoSolucion.metodoAnalitico.__init__(self,dominio,parametros)
        #print 'Se creo el loco theis'

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
        #print 'r: ' + str(r) +'t: '+str(t) + 'Q: ' + str(Q) + 'T: '+str(T) + 'S: '+str(S) 
        
        if (nargout == 1):
            w=self.WTheis(u) 
            s=Q/4.000/numpy.pi/T*w
        else:
            lista=[]
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

            aux1=dWdu*(-u/T)/w
            # print "T " + str(T)
            
            aux2=-1.000/T

            #print "aux1 " + str(aux1)
            #print "aux2 " + str(aux2)
            
            dsdT=s*(aux2 + aux1)

            ## print "dsdT " + str(dsdT)
            
            dsdS=s/w*dWdu*u/S
            
            #print "s "+ str(s)

            #+" "+str(dsdT)+" "+str(dsdS)

        return [s, dsdT, dsdS]

                            


    def WTheis(self,u,du=0):
        #
        #unction [W, dW]= WTheis(u,du)
        #numero de argumentos que salen la funcion
        nargout=2
        #numero de argumentos que salen de la funcion
        nargin=1
        
        if u>20 :
            if (nargout == 1):
                W=0
            else:    
                W=0;
                dW=0
            return
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
    ui = Theis(cont)
##    Calcula bien el metodo de tezis para un pozo solo
    ui.calcularpozo(1,1,500,1000,0.0001)
                                 
##    ui.calcular()
    


