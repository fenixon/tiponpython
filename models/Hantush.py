import sys
sys.path.append("views")
sys.path.append("models")

import metodoSolucion
from scipy.special import kn,expn

import numpy as np
import controlador

import scipy


#from scipy.special import j0

class Hantush(metodoSolucion.metodoNumerico):

    def __init__(self, dominio, parametros):
        ##Lista de cardinales de los parametros que utiliza el metodo
        ##Parametros 0: S, parametro 1:T, parametro 2:c
        self.paramcard=[0,1,2]
        #### Llamar al constructor del metodo de solucion
        ## probar llamar al metodo padre        
        metodoSolucion.metodoNumerico.__init__(self,dominio,parametros)
        #print 'Se creo el loco hantush'

    def calcularpozo(self,r,t,Q):

        #### Recuperar los valores de T, S y c guardados en el dominio y en el metodo,
        ## ver como obtenerlo siguiendo el modelo de dominio
        T=self.listaParametros[0].valoresParametro.valor
        S=self.listaParametros[1].valoresParametro.valor
        c=self.listaParametros[2].valoresParametro.valor


        rho= r/np.sqrt(T*c)
        tau = np.log(2/rho*t/(c*S))
        s = Q/(4*np.pi*T)*self.F(rho,tau)


    def F(self,rho,tau):
        #tau = tau(:);
        #tau(find(tau > 100)) = 100;
        if tau>100:
            tau=100
        #h_inf = besselk(0,rho);
        h_inf = kn(0,rho)
        expintrho = expn(rho)
        w = (expintrho-h_inf)/(expintrho-expn(rho/2))
        I = h_inf - w*expn(rho/2*np.exp(abs(tau))) + (w-1)*expn(rho*cosh(tau))
        h=h_inf+self.sign(tau)*I

    def sign(self,valor):
        if valor==0:
            return 0
        else:
            if valor>0:
                return 1
            else:
                return -1


if __name__ == "__main__":
    cont=1
    ui = Hantush(cont,1)
##    Calcula bien el metodo de tezis para un pozo solo
    #ui.calcularprueba(1,1,500,1000,0.0001)
    #ui.calcularpozoGenerico(1,1,500,1000,0.0001)

    #Error - r: 1091.15599791t: 0.09Q: 480.0T: 999.456893055S: 0.000100226593018desc 0.0
    #ui.calcularpozoGenerico(1091.15599791,0.09,480.0,999.456893055,0.000100226593018)
                                 
##    ui.calcular()
    


