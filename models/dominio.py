from pozo import pozo
import numpy as np
from bombeo import bombeo

class dominio(object):

    def __init__(self):
        self.alto = 50
        self.ancho = 50
        #self.listaBarreras = []
        self.listaPozo=[]
        self.listaRecta = []
        self.pozosVirtuales=[]
        self.listaCondicionesExternas = []
        print "Se ha creado el Dominio"
        #Diccionario que guarda los pozos y el metodo de optimizacion asociado al mismo
        self.listaPozoOptimiza ={}
        #Diccionario que guarda el metodo a utilizar y un vector con los pozos asociados al mismo
        self.optimizaciones={}
        #Agregar el a, b, c de la ecuacion del plano. Valores que
        ##  deben ser seteados desde la creacion del proyecto
        self.a=1
        self.b=-1
        self.c=0
        self.valores=[]

    def __del__(self):
        print "Se ha eliminado el Dominio"

        #Agregar el metodo para la ecuacion del plano
    def calcularH0(self, x,y):
##      Al final el nivel en un punto de coordenadas "xp" e "yp"
##      se calcula como H0= a*xp+b*yp+c  -s1(xp,yp,t)        
        return self.a*x + self.b*y + self.c

    def obtenerPozoBombeo(self):
##        print "lista de pozos"
##        print self.listaPozo
        for p in self.listaPozo:
            ## si tiene ensayos entonces es de bombeo se recupera el primero           
            if len(p.ensayos)>0:
##                print p
                return p
        return None


    ##esto se podria hacer cada vez que se asocia para no tar llamando cada vez
    def obtenerPozosdeBombeo(self):
        lista=[]
        for p in self.listaPozo:
            ## si tiene ensayos entonces es de bombeo
            if len(p.ensayos)>0:
                lista.append(p)
        return lista


    def obtenerPBombeoYVirtuales(self):        
        return np.concatenate((self.obtenerPozosVirtuales(), self.obtenerPozosdeBombeo()),1)
        
    def obtenerPozosVirtuales(self):
        return self.pozosVirtuales
    
    def obtenerPozoObservacion(self):
        for p in self.listaPozo:
            ## si tiene ensayos entonces es de bombeo se recupera el primero           
            if len(p.observaciones)>0:
##                print p
                return p
        return None


    def obtenerPozosdeObservacion(self):
        lista=[]
        for p in self.listaPozo:
            ## si tiene ensayos entonces es de bombeo
            if len(p.observaciones)>0:
                lista.append(p)
        return lista



    def procesarBarrera(self):
        self.pozosVirtuales=[]

##        print 'hizo el calculo de la recta'
        #Hay una barrera definida en el sistema
        ## cuando aparece la barrera se duplica todo se duplican los mismos ensayos        
        if len(self.listaRecta)>0:
            ##se obtiene la primera recta q pasa si son mas ???
            recta=self.listaRecta[0]
            alfa,beta,gamma=recta.devolverCoef()
            print 'alfa: '+str(alfa)+'beta: '+str(beta)+'gamma: '+str(gamma)

            #Recorrer todos los pozos para irlos replicando
            ##solo para los pozos de bombeo
            Todoslospozos=self.obtenerPozosdeBombeo();
            for p in Todoslospozos:             
                x=0
                y=0
                
                if alfa == 0:
                   #Pim.x=P.x;
                   x=p.x
                   #    Pim.y=-P.y-2*barrera.gamma/barrera.beta;
                   y=-p.y-(2*amma/beta)
                else:
                    if beta==0:
                        #Pim.y=P.y;
                        y=p.y
                        #Pim.x=-P.x-2*barrera.gamma/barrera.alfa;
                        x=-p.x-(2*gamma/alfa)
                    else:

                        #a= barrera.alfa/-barrera.beta;
                        a=alfa/-beta                       
                        #b= barrera.gamma/-barrera.beta;
                        b=gamma/-beta
                        #angulo=atan(a);
                        angulo=np.arctan(a)

                        #x1p=P.x +b/a;
                        x1p=p.x + b/a
                        #x2p=x1p*cos(angulo)+P.y*sin(angulo);
                        x2p=x1p*np.cos(angulo)+p.y*np.sin(angulo)                        
                        #y2p=-x1p*sin(angulo)+P.y*cos(angulo);
                        y2p=-x1p*np.sin(angulo)+p.y*np.cos(angulo)
                           
                        #Pim.x= x2p*cos(angulo) +y2p*sin(angulo) -b/a ;
                        x=x2p*np.cos(angulo) +y2p*np.sin(angulo) -b/a
                        #Pim.y= x2p*sin(angulo) -y2p*cos(angulo) ;
                        y= x2p*np.sin(angulo) -y2p*np.cos(angulo)

                
                #se instancia un nuevo pozo cn una nueva lista de bombeos
                pvirtual=pozo(x,y)
                pvirtual.copiarAPozoVirtual(p,recta.tipo)
                self.pozosVirtuales.append(pvirtual)                

            ##barrera.signo=sign( p(1).x*barrera.alfa + p(1).y*barrera.beta +barrera.gamma );
            valorsigno=Todoslospozos[0].x * alfa + Todoslospozos[0].y * beta + gamma

            print np.sign(valorsigno)
            
            recta.setearSigno(np.sign(valorsigno))
##            if valorsigno==0:                
##                barrera.signo=0
##            else:
##                if valorsigno>0
##                    barrera.signo=1
##                    recta.setearSigno(1)
##                else:
##                    barrera.signo=-1
##                    recta.setearSigno(-1)
                    
        else:
            print 'no hay barreras'
            



        


        
