from PyQt4 import QtCore, QtGui
from pozo  import pozo
from barrera import barrera
from calitheis2 import *
from calibracion2 import *
from calihantush import *
import numpy as np
import observacion
import observacionesensayo
import bombeo
import ensayobombeo
import dominio
from parametros import parametros

class Proyecto(object):
    
    def __init__(self):        
        self.ultimoIdEns=0
        self.ultimoIdObs=0
        self.ensayos=[]
        self.observaciones=[]
        self.ensayosCopia=[]
        self.observacionesCopia=[]
        self.dominio = dominio.dominio()
        self.metodo=None

        #Lista que guardan pozo y recta
##      self.listaPozo = []
        #self.listaRecta = []

        #Ultima recta y pozo agregados
        self.idP = 0
        self.idR = 0

        #Recta candidata a ser agregada
        self.rectaCandidata = ""
        self.parametros=[]

        ##Inicial la lista de parametros
        self.cargarParametros()

        self.nix=4
        self.niy=4

        self.ti=0.0
        self.tf=0.3
        nit=10
        tfo=1.8        

    def cargarParametros(self):
        ###Si se quiere un parametro nuevo se tiene q agregar        
        self.parametros.append(parametros('T','m^2/d'))    #parametro 0
        self.parametros.append(parametros('S',''))    #parametro 1
        self.parametros.append(parametros('C',''))    #parametro 2
        
    def leerParametros(self):
        for p in self.parametros:
            print p.nombre
                
    def agregarEnsayo(self, bombeos, nombre):
        self.ultimoIdEns=self.ultimoIdEns + 1
        e=ensayobombeo.ensayobombeo(bombeos, self.ultimoIdEns, nombre)
        self.ensayos.append(e)
        return e

    def restaurarEnsayo(self, e):
        self.ensayos.append(e) 

    def eliminarEnsayo(self, e):
        self.ensayos.remove(e)

    def agregarObservacion(self, observaciones, nombre):
        self.ultimoIdObs=self.ultimoIdObs + 1
        obse=observacionesensayo.observacionesensayo(observaciones, self.ultimoIdObs, nombre)
        self.observaciones.append(obse)
        return obse

    def restaurarObservacion(self, obse):
        self.observaciones.append(obse)

    def copiarObservacionesEnsayos(self):
        self.ensayosCopia=[]
        self.observacionesCopia=[]        
        for e in self.ensayos:
                self.ensayosCopia.append(e.copiaSuperficial())
        for o in self.observaciones:
                self.observacionesCopia.append(o.copiaSuperficial())

    def restaurarObservacionesEnsayos(self):
        self.ensayos=[]
        self.observaciones=[]        
        for e in self.ensayosCopia:
                self.ensayos.append(e.copiaSuperficial())
        for o in self.observacionesCopia:
                self.observaciones.append(o.copiaSuperficial())                 

    def eliminarObservaciones(self, obse):
        self.observaciones.remove(obse)

    def creadiscesp(self,Np,lx,m,xp):

        #Coordenada de pozos
        Np1=Np
        if Np>1:
            xp=np.zeros((Np),float)

        #de 0 a Np-2 numpy. 1 a Np-1 en matlab
        for i in range(Np-1):
            if np.abs(xp[i]-xp[i+1])<15:
                xp[i:Np-2]=xp[i+1:Np-1]
                xp[Np-1]=0
                Np=Np-1   
       
        if Np>1:
            Ix=np.zeros((Np+1),float)
            LnIx=np.zeros((Np),float)
            Ndiv=np.zeros((Np),float)
            DT=np.zeros((Np),float)
            AD=np.zeros((Np),float)
            indde=np.zeros((Np),float)
            indiz=np.zeros((Np),float)
            maxNdiv=0            
            for i in range(Np):
                Ix[0]=0
                Ix[i]=(xp[i]+xp[i-1])/2
                Ix[Np]=lx

            sumaLnIx=0
            for i in range (Np):
                LnIx[i]=np.log(np.abs(Ix[i+1]-Ix[i]))
                sumaLnIx=sumaLnIx+LnIx[i]

            for i in range(Np):
                Ndiv[i]=round(m*LnIx[i]/sumaLnIx)
                if Ndiv[i]<3:
                    Ndiv[i]=3
                if Ndiv[i]>maxNdiv:
                    maxNdiv=Ndiv[i]
                DT[i]=np.log(xp[i]-Ix[i])+np.log(Ix[i+1]-xp[i])
                AD[i]=DT[i]/Ndiv[i]

            xde=np.zeros((Np,maxNdiv+1),float)
            xiz=np.zeros((Np,maxNdiv+1),float)
            
            for i in range(Np):
                for j in range (Ndiv[i]):
                    xde[i,j]=xp[i]+np.exp(j*AD[i])
                    if (xde[i,j]>Ix[i+1]):
                        if abs(Ix[i]-xde[i,j])<abs(Ix[i+1]-xde[i,j]):
                            xde[i,j]=Ix[i]
                        else:
                            xde[i,j]=Ix[i+1]
                        indde[i]=j;
                        break

            for i in range(Np):
                for j in range (Ndiv[i]):
                    xiz[i,j]=xp[i]-np.exp(j*AD[i])
                    if xiz[i,j]<Ix[i]:
                        if np.abs(Ix[i]-xiz[i,j])<np.abs(Ix[i+1]-xiz[i,j]):
                            xiz[i,j]=Ix[i]
                        else:
                            xiz[i,j]=Ix[i+1]
                        indiz[i]=j;
                        break

            x=np.zeros((maxNdiv+3+maxNdiv),float)
            k=0
            for i in range(Np):
                #for j=indiz(i):-1:1;
                for j in range(indiz[i],-1,-1):
                    x[k]=xiz[i,j]
                    k=k+1

                x[k]=xp[i]
                k=k+1
                for j in range (indde[i]-1):
                    x[k]=xde[i,j]
                    k=k+1
                    
            x[k]=lx

            print "Ix ", Ix
            print "LnIx ", LnIx
            print "Ndiv ", Ndiv
            print "DT ", DT
            print "AD ", AD
            print "indde ", indde
            print "indiz ", indiz
            print "xde ", xde
            print "xiz ", xiz
            print "x ", x

        else:
            ##Revisado
            
            Ix=lx
            Ndiv=m/2
            DT=np.log(lx)
            AD=DT/Ndiv
            #xde=np.zeros((Ndiv),float)
            xde=[]
            #xiz=np.zeros((Ndiv),float)
            xiz=[]
            indde=-1
            
            for j in range (Ndiv):
                #xde[j]=xp+np.exp(j*AD)
                #print "Las sumas"
                #print xp
                #print np.exp(j*AD)
                #print np.add(xp,np.exp(j*AD)) 
                xde.append(np.add(xp[0],np.exp((j+1)*AD)))
                #[j]=
                if xde[j]>Ix:
                    #if np.abs(Ix-xde[j])<np.abs(Ix-xde[j]):
                    xde[j]=Ix
                    #else:
                    #xde[j]=Ix
                    indde=j
                    break

            #print "dps del for xde ", xde

            for j in range(Ndiv):
                xiz.append(xp[0]-np.exp((j+1)*AD))
                if xiz[j]<0:
                    #if abs(Ix-xiz(j))<abs(Ix-xiz(j));
                    xiz[j]=0
                    #else;
                    #  xiz(j)=0;
                    #end;
                    indiz=j
                    break
                
            #x=np.zeros((Ndiv-1+3+Ndiv-1),float)
            x=[]
            k=0
            #for j=indiz:-1:1;
            #indiz es uno menos y va hasta el o
            for j in range(indiz,-1,-1):
                x.append(xiz[j])
                k=k+1

            x.append(xp[0])
            k=k+1

            if indde>-1:
                ##indde es ya uno menos 
                for j in range (indde):
                    x.append(xde[j])
                    k=k+1
                
            x.append(lx)

            #print "Ix ", Ix
            #print "Ndiv ", Ndiv
            #print "DT ", DT
            #print "AD ", AD
            #print "indde ", indde
            #print "indiz ", indiz
            #print "xde ", xde
            #print "xiz ", xiz
            #print "x ", x          
            
        Np=Np1
        return x

        

    def setearValoresDiscretizaciones(self, nix, niy, ti, tf, nit, tfo, tipo=None):

        self.nix=nix
        self.niy=niy
        self.ti=ti
        self.tf=tf
        self.nit=nit
        self.tfo=tfo
        n=nix
        m=niy
        lx=self.dominio.ancho
        ly=self.dominio.alto
        self.X=None
        self.Y=None
        self.xx=None
        self.yy=None
        ##discretizacion temporal
        dt=(tf-ti)/nit
        self.dt=dt
        self.tipodis=tipo
        
        if (tipo!=None):
            if tipo=="Lineal":
                #x=(0:m-1)*lx/(m-1);
                x=np.divide(np.multiply(range(m),lx),(m-1) )
                #y=(0:n-1)*ly/(n-1);
                y=np.divide(np.multiply(range(n),ly),(n-1) )
            elif tipo=="Logaritmica":
                #Calculo del eje x

                if self.metodo.aceptaBarrera==True :
                    Todoslospbombeo=self.dominio.obtenerPBombeoYVirtuales()            
                else:
                    Todoslospbombeo=self.dominio.obtenerPozosdeBombeo()
                #print Todoslospbombeo
                Np=len(Todoslospbombeo)
                #xp=np.zeros((Np),float)
                xp=[]                
                #yp=np.zeros((Np),float)
                yp=[]
                for p in Todoslospbombeo:
                    xp.append(p.x)
                    yp.append(p.y)
                xp=np.sort(xp)
                x=self.creadiscesp(Np,lx,m,xp)                
                m=len(x)
                
                #Calculo del eje y
                yp=np.sort(yp)
                y=self.creadiscesp(Np,ly,n,yp)                
                n=len(y)
                

            print "x ",x
            print "y ",y    

            ##Se generan las matrices para usar en todas las graficas
            X, Y = np.meshgrid(x, y)

            #(1:nit)*dt
            ##discretizacion temporal
            tiempos=np.zeros((nit),float)
            tiempos[0]=ti
            tiemposobs=np.zeros((nit),float)
            dtobs=round((tf-ti)/(nit-1),2)
            tiemposobs[0]=dtobs            
            for i in range(1,nit):
                tiempos[i]=tiempos[i-1]+dt
                tiemposobs[i]=tiemposobs[i-1]+dtobs
                
            self.nix=m
            self.niy=n
            self.X=X
            self.Y=Y
            self.xx=x
            self.yy=y              
            self.tiempos=tiempos
            self.tiemposobs=tiemposobs
            #print self.X
                        
        else:
            nit=nit+1
            ##se suma 1 para que sea haga bien la division es un intervalo mas 0..100 (101)
            nix=nix+1
            niy=niy+1

            ##discretizacion espacial
            xx = np.linspace(0,self.dominio.ancho,nix)
            yy = np.linspace(self.dominio.alto,0,niy)
            ##Se generan las matrices para usar en todas las graficas
            X, Y = np.meshgrid(xx, yy)
            
            ##discretizacion temporal
            tiempos=np.zeros((nit),float)
            tiemposobs=np.zeros((nit),float)
            tiempos[0]=ti
            tiemposobs[0]=ti
            for i in range(1,nit):
                tiempos[i]=tiempos[i-1]+dt
                tiemposobs[i]=tiemposobs[i-1]+dt

            self.nit=nit
            self.nix=nix
            self.niy=niy
            self.X=X
            self.Y=Y
            self.xx=xx
            self.yy=yy                
            self.tiempos=tiempos
            self.tiemposobs=tiemposobs
            

    def devolverDiscretizaciones(self):
        return [self.X,self.Y, self.xx, self.yy, self.tiempos, self.tiemposobs, self.dt, self.tipodis]
         

    def devolverValoresDiscretizaciones(self):
        return [self.nix, self.niy, self.ti, self.tf, self.nit, self.tfo] 

    def verificarFormato(self,lista, t):
        control=True
        i=0
        #print "control "
        while( i<len(lista) and control  ):
            control=t>lista[i].tiempo
            #print "tiempo "+str(t)+" tiempo vector "+str(lista[i].tiempo) + " control "+str(control)
            i=i+1
        return control

    def obtenerDominio(self):
        return self.dominio
    

    #CRUD de pozos
    def agregarPozo(self, x, y):        
        p = pozo(x, y)
        self.idP = self.idP + 1
        p.id = self.idP
        self.dominio.listaPozo.append(p)
        return p.id
                

    def moverPozo(self, idElemento, x, y):
        
        for pozo in self.dominio.listaPozo:
            if pozo.id == idElemento:
                pozo.actualizarCoordenadas(x, y)
                return

    def buscarPozo(self, idElemento):
        for p in self.dominio.listaPozo:
            if p.id == int(idElemento):
                return p
         
    def removerPozo(self, idElemento):            
        for x in self.dominio.listaPozo:
            if x.id == idElemento:
                self.dominio.listaPozo.remove(x)
    """def optimizacioneslistar(self):
        self.optimizaciones = QtCore.QStringList()
        
        self.optimizaciones << "CaliTheis2" << "calibracion2" << "CaliHantush"""
    def optimizacioneslistar(self):
        
        self.optimizaciones = QtCore.QStringList()
        #print metodo.getoptimizaciones()
        print "optimizaciones:" + str(self.metodo.getoptimizaciones())
        #self.optimizaciones << "CaliTheis2" << "calibracion2" << "CaliHantush"
        for optimizacion in self.metodo.getoptimizaciones():
            self.optimizaciones << str(optimizacion)
        return self.optimizaciones
    def optimizacioneslistarmenos(self,nolistar):
        self.opt = QtCore.QStringList()
        for x in self.optimizaciones:
            if x != nolistar:
                #print "muestro " + x
                self.opt << x
        
        return self.opt
    """def asociarPozoOptimiazion(self,idElemento,metodo):
        for pozo in self.dominio.listaPozo:
            if pozo.id == idElemento:
                #en self.dominio.listaPozoOptimiza[idElemento] ahi 
                #que guardar una instancia de un objeto, cuyo tipo tiene que ser
                #determinado por el valor de metodo
                print "instancio:" + metodo
                ui = eval(str(metodo) + "()")
                ui.setpozo(pozo)
                #con el metodo getparametros obtengo la lista de parametros del metodo
                #print str(ui.getparametros())
                #for p in ui.getparametros():
                #    print p
                self.dominio.listaPozoOptimiza[idElemento]= ui
        print "se agrego a la lista de optimizaciones" """

    def instanciaoptimizacion(self,metodo):
        objeto=eval(str(metodo) + "()")
        return objeto


    def asociarPozoOptimiazion(self,idElemento,metodo):
        for pozo in self.dominio.listaPozo:
            if pozo.id == idElemento:
                #print "instancio:" + metodo
                #ui = eval(str(metodo) + "()")
                #Busco el indice del metodo
                claves=self.dominio.optimizaciones.keys()
                token=False
                for clave in claves:
                    if (clave==metodo):
                        #Si existe el metodo en el diccionario, le agrego el pozo
                        token=True
                        self.dominio.optimizaciones[clave].append(idElemento)
                if (token==False): #Si no existe el metodo, lo creo y le agrego el pozo
                    self.dominio.optimizaciones[metodo]=[]
                    self.dominio.optimizaciones[metodo].append(idElemento)      
                    #self.dominio.listaPozoOptimiza[metodo]= ui
                              
                #self.dominio.optimizaciones[metodo]= ui
        print "se agrego a la lista de optimizaciones" 
    def existeasociacionoptimizacion(self,idElemento,metodo):
        #Busco el indice del metodo
        claves=self.dominio.optimizaciones.keys()
        token=False
        for clave in claves:
            if (clave==metodo):
                #Busco si el metodo tiene el pozo ingresado
                for pozo in self.dominio.optimizaciones[metodo]:
                    if (pozo==idElemento):
                        token=True
        return token

    def listarPozosObsParaOptimizar(self):
        return self.dominio.optimizaciones

    def listarPozosParaOptimizar(self):
        return self.dominio.listaPozoOptimiza

    def quitarPozoOptimizacion(self,idpozo,metodo):
        print "entro en el metodo pa quitar"
        claves=self.dominio.optimizaciones.keys()
        for clave in claves:
            if (clave==metodo):
                self.dominio.optimizaciones[metodo].remove(idpozo)
                print "Se quito el pozo"
            

    def retornarCoordenadas(self, idElemento):
        listaRetorno = {}
        listaRetorno["x"] = 0
        listaRetorno["y"] = 0

        for pozo in self.dominio.listaPozo:
            if pozo.id == idElemento:
                listaRetorno["x"] = pozo.x
                listaRetorno["y"] = pozo.y
                
                return listaRetorno
            
        return listaRetorno
       

    #CRUD de barreras
    def agregarRecta(self, tipo, x1, y1, x2, y2, alto, ancho):

        r = barrera(x1, x2, y1, y2, tipo, alto, ancho)
        self.idR = self.idR + 1
        r.id = self.idR
	self.dominio.listaRecta.append(r)
	return r.id


    def buscarRecta(self, idElemento):
        for recta in self.dominio.listaRecta:
            if recta.id == idElemento:
                return recta

    def dibujarRecta(self):
        return self.dominio.listaRecta

    def buscarPuntoEnRecta(self, x, y):

        for barrera in self.dominio.listaRecta:

            recta = QtCore.QLine(barrera.x1, barrera.y1, barrera.x2, barrera.y2)

            puntoP = QtCore.QPoint(x, y)
            puntoQ = QtCore.QPoint(recta.x1(), recta.y1())

            rectay = QtCore.QLine(puntoP, puntoQ)           

            puntoR = QtCore.QPoint(recta.x2(), recta.y2())

            rectaw = QtCore.QLine(puntoP, puntoR)           

            valor1 = np.absolute(recta.dx() /2)
            valor2 = np.absolute(recta.dy() /2)
            
            #Recta proxima a las x
            if  np.absolute(rectay.dx()) < np.absolute(recta.dx() /2) and  np.absolute(rectay.dy()) < np.absolute((recta.dy() / 2)):               
                lista = {}
                lista['punto'] = puntoQ

                lista['eje'] = "x"
                lista['id'] = barrera.id
                return lista
            
            #Recta proxima a las y
            if np.absolute(rectaw.dx()) < np.absolute(recta.dx() /2) and  np.absolute(rectaw.dy()) < np.absolute((recta.dy() / 2)):
                lista = {}
                lista['punto'] = puntoR
               
                lista['eje'] = "y"
                lista['id'] = barrera.id
                return lista
        lista = {}
        return lista


    def buscarPuntoRecta(self, x, y, identificador):
        
        for barrera in self.dominio.listaRecta:

            if barrera.id == identificador:
                recta = QtCore.QLine(barrera.x1, barrera.y1, barrera.x2, barrera.y2)

                puntoP = QtCore.QPoint(x, y)
                puntoQ = QtCore.QPoint(recta.x1(), recta.y1())

                rectay = QtCore.QLine(puntoP, puntoQ)           

                puntoR = QtCore.QPoint(recta.x2(), recta.y2())

                rectaw = QtCore.QLine(puntoP, puntoR)           

                valor1 = np.absolute(recta.dx() /2)
                valor2 = np.absolute(recta.dy() /2)

                #Recta proxima a las x
                if  np.absolute(rectay.dx()) < np.absolute(recta.dx() /2) and  np.absolute(rectay.dy()) < np.absolute((recta.dy() / 2)):
                    lista = {}
                    lista['punto'] = puntoQ

                    lista['eje'] = "x"
                    lista['id'] = barrera.id
                    return lista

                #Recta proxima a las y
                if np.absolute(rectaw.dx()) < np.absolute(recta.dx() /2) and  np.absolute(rectaw.dy()) < np.absolute((recta.dy() / 2)):
                    lista = {}
                    lista['punto'] = puntoR

                    lista['eje'] = "y"
                    lista['id'] = barrera.id
                    return lista
        lista = {}
	lista['eje'] = "z"
        return lista


    def actualizarRecta(self, idRecta, x, y, tipoPunto, alto, ancho):
        for barrera in self.dominio.listaRecta:
            if barrera.id == idRecta:
                if tipoPunto == "Y":
                    barrera.actualizarBarrera3(barrera.x1, x, barrera.y1, y, alto, ancho)
                else:
		    print " VALOR DE X ", x, " DE Y", y
                    barrera.actualizarBarrera3(x, barrera.x2,  y, barrera.y2, alto, ancho)
		    print " VALOR DE X ", barrera.x1, " DE Y", barrera.y1

    def actualizarRectaCoord(self, idElemento, x1, y1, x2, y2, tipo):
        for recta in self.dominio.listaRecta:
            if recta.id == idElemento:
                recta.actualizarBarrera(x1, x2, y1, y2, tipo)
                return

    def actualizarRectaCoordenada(self, idElemento, x1, y1, x2, y2):
        for recta in self.dominio.listaRecta:
            if recta.id == idElemento:
                recta.actualizarBarrera2(x1, x2, y1, y2)
                return

    def actualizarRectaC(self, idElemento, x1, y1, x2, y2, alto, ancho):
        for recta in self.dominio.listaRecta:
            if recta.id == idElemento:
                recta.actualizarBarrera3(x1, x2, y1, y2, alto, ancho)
                return

                
                
    def buscarPuntoPorQ(self, x, y):
        for Q in self.dominio.listaRecta:
            
            recta = QtCore.QLine(Q.x1, Q.y1, Q.x2, Q.y2)

            puntoP = QtCore.QPoint(x, y)

            puntoQ = QtCore.QPoint(recta.x1(), recta.y1())

            rectax = QtCore.QLine(puntoP, puntoQ)   

            #Recta proxima a las x
            if  np.absolute(rectax.dx()) < np.absolute(recta.dx() /2) and  np.absolute(rectax.dy()) < np.absolute((recta.dy() / 2)):               

                return Q.id

    def buscarPuntoPorR(self, x, y):
        for R in self.dominio.listaRecta:
            
            recta = QtCore.QLine(R.x1, R.y1, R.x2, R.y2)

            puntoP = QtCore.QPoint(x, y)

            puntoR = QtCore.QPoint(recta.x2(), recta.y2())

            rectay = QtCore.QLine(puntoP, puntoR)   

            #Recta proxima a las x
            if  np.absolute(rectay.dx()) < np.absolute(recta.dx() /2) and  np.absolute(rectay.dy()) < np.absolute((recta.dy() / 2)):
                
                return R.id

    def eliminarRecta(self, idElemento):
        for recta in self.dominio.listaRecta:
            if recta.id == idElemento:
                self.dominio.listaRecta.remove(recta)

    def agregarRectaCandidata(self, tipo, x1, y1, x2, y2, alto, ancho):
        self.rectaCandidata = barrera(x1, x2, y1, y2, tipo, alto, ancho)

    def actualizarRectaCandidata(self, x1, y1, x2, y2, alto, ancho):
		self.rectaCandidata.actualizarBarrera3(x1, x2, y1, y2, alto, ancho)


    def obtenerCandidata(self):
        return self.rectaCandidata

    def hayRectaCandidata(self):

        if self.rectaCandidata:
            return True

        return False

    def eliminarRectaCandidata(self):
        self.rectaCandidata = ""

    def incluirCandidata(self, signo):
        self.idR = self.idR + 1
        self.rectaCandidata.id = self.idR
	self.rectaCandidata.tipo = signo
        self.dominio.listaRecta.append(self.rectaCandidata)
        self.rectaCandidata = None
	return self.idR
