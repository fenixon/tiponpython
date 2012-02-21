import sys
sys.path.append("views")
sys.path.append("models")
import numpy

import metodoSolucion
from scipy.interpolate import interp2d
from numpy import hypot, mgrid, linspace

from matplotlib.figure import Figure
from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib

import matplotlib.mlab as mlab

from matplotlib import cm

import numpy as np
import controlador


from scipy.special import j0

class Theis(metodoSolucion.metodoSolucion):

    def __init__(self, cont):
        global ContEnsayo
        ContEnsayo=cont
        
        print 'venta'
        #metodoSolucion.metodoSolucion.__init__(self, 2)

    def velocidad(self):

        v = np.arange(-3, 3,1)
        [x,y] = np.meshgrid(v,v)

        z=np.multiply(x,np.exp( -np.power(x,2) - np.power(y,2) ))

        [py,px] = np.gradient(z,1,1)

        print py
        print px
        #fig = Figure(figsize = (1.8 * 4, 2.4 * 4))
        #x = np.arange(0, 10, 0.5)
        #y = np.arange(-2, 2, 0.5)
        #(X,Y) = np.meshgrid(v,v)
        #u = 5*X
        #v = 5*Y        


        #x = np.arange(-2.00, 3, 1)
        #y = np.arange(-2.00, 3, 1)
        #(X,Y) = np.meshgrid(x,y)
        #u = 5*X
        #v = 5*Y

        print 'x '+str(x)
        print 'y '+str(y)
        print 'z '+str(z)

        print 'px '+str(px)
        print 'py '+str(py)
        
        #q = plt.quiver(X, Y, u, v, angles='xy', scale=40, color=['r'])
        #p = plt.quiverkey(q,1,16.5,50,"50 m/s",coordinates='data',color='r')        

        q = plt.quiver(x,y, px, py)
        p = plt.quiverkey(q,1,16.5,50,"50 m/s",coordinates='data',color='r')
        plt.title('Velocidad')
        plt.show()
        print 'Fourth plot loaded...'        


    def velocidadlimpio(self):
        #sino no llega al 2, asi funciona        
        v = np.arange(-3, 3,1)
        [x,y] = np.meshgrid(v,v)

        z=np.multiply(x,np.exp( -np.power(x,2) - np.power(y,2) ))

        #Matplotlib t invierte el orden de las matrices a diferenciade matlab
        [py,px] = np.gradient(z,1,1)

        print 'x '+str(x)
        print 'y '+str(y)
        print 'z '+str(z)
        print 'px '+str(px)
        print 'py '+str(py)
        
        #q = plt.quiver(X, Y, u, v, angles='xy', scale=40, color=['r'])
        #p = plt.quiverkey(q,1,16.5,50,"50 m/s",coordinates='data',color='r')        

        #primero los rangos, despues los valores q contiene
        q = plt.quiver(x,y, px, py)
        p = plt.quiverkey(q,1,16.5,50,"50 m/s",coordinates='data',color='r')
        plt.title('Velocidad')
        plt.show()
        print 'Fourth plot loaded...'  

    
    def calcularold(self):
#ver como obtener los datos para pasarlo al otro
#recorrer todos los pozos de observacion
## se va generando la matriz

        ##Para un determinado tiempo
        ## obtener x e y y el z
        
#        x,y = mgrid[0:2,0:2]

        x=numpy.vstack([[2 ,7],[6,4]])
        y=numpy.vstack([[10,15],[12,11]])
        
##        x,y = mgrid[1:4,1:4]
##        z=hypot(x,y)

        z=numpy.vstack([[9.9756,10.0000, 3.0000],
                        [9.9965,9.9134, 4.6000],
                        [9.9965,9.9134, 4.8000]])
        
        g,k=numpy.gradient(z, 25,25)
##primer pozo
#####x 2
##y 10
##9.9756	

##segundo pozo
####x 7
##y 15
##10.0000

##x 6
##y 12
##9.9965

####x 4
##y 11
#9.9134

        #print x
        #print y
        print z
        print "mat "
        print g
        print k
        
####        newfunc=interp2d(x,y,z,kind='linear')
### ak tiene que configurarse todo el dominio en xx e yy
####        xx = numpy.arange(0, 30, 1)
####        yy=xx

##        print "todo el dominio"
        
##        print xx

        ## A la funcion le pasas x e y
####        print "x: 1  y: 7 - "+str(newfunc(1,7))
####        print "x: 7  y: 15  - "+str(newfunc(7,15))
##        print "x: 2  y: 10  - "+str(newfunc(2,10))
##        print "x: 6  y: 12    - "+str(newfunc(6,12))
##        print "x: 4  y: 11 - "+str(newfunc(4,11))        
        
##        zz=newfunc(xx,yy)

##        print "La interpolacion"
        ## En el arreglo queda primero la Y y luego la X
##        print str(zz[15][7])
##        print str(zz[10][2])
##        print str(zz[12][6])
##        print str(zz[11][4])
        
##        print zz

##        for indx in xx:
####            for indy in yy:
##                print "x :"+str(indx)+ " y :"+str(indy)+ " z:"+str(zz[indy][indx])

####        X, Y = numpy.meshgrid(xx, yy)


####        fig = Figure(figsize = (1.8 * 4, 2.4 * 4))
####        self.axu = fig.add_subplot(2, 2, 1)
####        self.axd = fig.add_subplot(2, 2, 2)
####        self.axt = fig.add_subplot(2, 2, 3, projection = '3d')
####        self.axc = fig.add_subplot(2, 2, 4)
####        fig.subplots_adjust(hspace=.2, wspace=.3, bottom=.07, left=.08, right=.92, top=.94)
####        self.fig = fig
##        
####        ax = self.axt
####        surf = ax.plot_surface(X, Y, zz, rstride=1, cstride=1, cmap=cm.jet, linewidth=0, antialiased=True)
        

    ## Este meotod tiene que llamar alvoro al momento de graficar y le devuelve la matriz
    def calcular(self):
        # Se indentifica donde esta el pozo de bombeo
        global ContEnsayo
        ContEnsayo                
        # Por ahora tomar el primero de bombeo que se detecte. Luego cambia cuando hayan mas pozos
        
        ###Esto se podria obtener desde el dominio        
        pozoBombeo=ContEnsayo.obtenerPozoBombeo()
        x0=pozoBombeo.x
        y0=pozoBombeo.y
        #comentar cuando el pozo de bombeo esta bien posicioando
        x0=5
        y0=5


        print 'x0: ' + str(x0)
        print 'y0: ' + str(y0)

        ##Obtener el ensayo de bombeo, los caudales y tiempos(al menos hay uno) ...que pasa cuando hay mas de un ensayo asociado?????        
        bombeos=pozoBombeo.ensayos[0].devolverB()    
        
        # Recorrer todo el dominio
        d=ContEnsayo.obtenerDominio()
        #### Recuperar los valores de T y el S guardados en el dominio, ver como obtenerlo siguiendo el modelo de dominio
        T=500
        S=0.000000001
        #Q=500
        #r=1

        #####ver como llamar la matriz de los tiempos
        ## por ahora consideramos que va a ser lineal que arranca en el tiempo 0 al 10

        ##el tiempo va desde 0 a 4, el 0 no se usa      
        self.matrizDescenso=numpy.zeros((len(bombeos)+1,d.ancho,d.alto), float)   

        #print self.matrizDescenso[1]

        ##dominio en x        
        xx = numpy.arange(0, d.ancho, 1)
        ### dominio en y
        yy = numpy.arange(0, d.alto, 1)

        for x in xx:
            for y in yy:
                #calculo de la distancia radial            
                #sqrt(|X0-X1|^2 + |y0-y1|^2)
                r=numpy.sqrt(numpy.square(x0-x) + numpy.square(y0-y))

                #Obtener el Ho llamando a la clase dominio
                H0=d.calcularH0(x,y)

                print 'x: '+ str(x)+ 'y: '+str(y)+' r: '+str(r)

                for bom in bombeos:
##                  El tiempo t nunca puede ser 0, sino t da error                    
                    t=bom.tiempo
                    Q=bom.caudal

#Aca se llama al metodo Theis para ese punto, lo que nos da el descenso 's'
## Esto son los parametros q se mandan
                    
####                    print 'r '+str(r)
##                    print 't '+str(t)
##                    print 'Q '+str(Q)
##                    print 'T '+str(T)
##                    print 'S '+str(S)
                    
                    s,dsdT,dsdS=self.calcularpozo(r, t, Q, T, S)
                    
                
                    #el nivel "h" se calcula como "h=Ho-s"
                    h=H0-s

                    print 'h: '+ str(h)+ 'H0: '+str(H0)+'s: '+str(s)
                    
                    
                    #Operar y generar la matriz
                    ##La matriz es tiempo t y despues x,y
                    self.matrizDescenso[t,x,y]=h

        

        
        X, Y = numpy.meshgrid(xx, yy)
##      se soluciona desd el tiempo 1 porque el t=0 da error al dividir        
        zz = self.matrizDescenso[1]

        print zz

        fig = Figure(figsize = (1.8 * 4, 2.4 * 4))
        self.axu = fig.add_subplot(2, 2, 1)
        self.axd = fig.add_subplot(2, 2, 2)
        self.axt = fig.add_subplot(2, 2, 3, projection = '3d')
        self.axc = fig.add_subplot(2, 2, 4)
        fig.subplots_adjust(hspace=.2, wspace=.3, bottom=.07, left=.08, right=.92, top=.94)
        self.fig = fig
        
        ax = self.axt
        surf = ax.plot_surface(X, Y, zz, rstride=1, cstride=1, cmap=cm.jet, linewidth=0, antialiased=True)
        

        return self.matrizDescenso



    def calcularpozo(self,r,t,Q,T,S):
        
        # [s, dsdT, dsdS]=Theis(r,t,Q,T,S)
        # nro de valores que devuelve la funcion, esto lo vemos dps xq varia
        nargout=3
        
        if r<=0.15 :
            r=.15;
 
        #u=r^2*S/T/t/4;
        u=numpy.power(r,2)*S/T/t/4;
##        print 'S: '+str(S)+'T: '+str(T)+'t: '+str(t) + 'U: ' + str(round(u,2))
        
        if (nargout == 1):
            w=self.WTheis(u) ; 
            s=Q/4/pi/T*w;
        else:
            lista=[]
            ## se captura en dos parametros la lista q devuelve            
            w,dWdu=self.WTheis(u) ;

##            print "u.. " + str(u)            
##          w=lista[0]           
##          dWdu=lista[1]
##            print "dw.. " + str(dWdu)
            
            s=Q/4/numpy.pi/T*w;
            #print str(s)
            #dsdT=s*(-1/T + dWdu*(-u/T)/w);

            aux1=dWdu*(-u/T)/w

##            print "T " + str(T)
            
            aux2=-1.0/T

##            print "aux1 " + str(aux1)
##            print "aux2 " + str(aux2)
            
            dsdT=s*(aux2 + aux1);

##            print "dsdT " + str(dsdT)
            
            dsdS=s/w*dWdu*u/S ;


##        print str(s)+" "+str(dsdT)+" "+str(dsdS)

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
                W=0;
            else:    
                W=0;
                dW=0;
            return
        else:
            if u>=1:
                err=1e-10;mgrid[-5:6,-5:6]
            else:
                err=1e-6;

        n=1. ;
        f=-u ;
        acumulador=f ;
        g=f ;

        if (nargout != 1) :
            acumulador2= -1. ;
            dg= -1.; 
        
        if (nargout == 1):
            while abs(g) >= err:
                n=n+1 ;
                f=-f*u/n ;
                g=f/n ;
                acumulador=acumulador+g ;
            W=-0.577215664901532860 -numpy.log(u) -acumulador ;
        else:
            while   abs(g) >= err and abs(dg) >= err :
                n=n+1 ;
                f=-f*u/n ;
                g=f/n ;
                dg=f/u ;
                acumulador=acumulador+g ;
                acumulador2=acumulador2+dg ;
            W=-0.577215664901532860 -numpy.log(u) -acumulador ;
            dW=-1./u-acumulador2 ;    

        if (nargin != 1) :
            dW=dW*du ;

        return [W, dW]


if __name__ == "__main__":
    cont=1
    ui = Theis(cont)
##    Calcula bien el metodo de tezis para un pozo solo
##    ui.calcularpozo(1,1,500,1000,0.0001)
                                 
    ui.velocidad()
    


