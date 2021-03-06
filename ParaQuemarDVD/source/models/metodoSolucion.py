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

import numpy as np
from valoresParametros import valoresParametros
from parametros import parametros


class metodoSolucion(object):

    def __init__(self, dominio, parametrosC, asociar=None): 
##        self.paramcard=cardinales
        self.dominio=dominio
        ##Maximos y minimos de la grafica              
        self.min=1000000
        self.max=-1000000
        self.asociar=asociar
        #Lista que contendra las optimizaciones para un metodo especifico
        #self.optimizaciones=[]

        #print 'MEtodo de solucion '
        #print 'SE INSTANCIO ',self.asociar
        
        ## Asociar el metodo al dominio
        if self.asociar!=None and self.asociar==True :
            self.dominio.metodo=self
            #print "setio el metodo al dominio "
        self.listaParametros=[]
        for i in self.paramcard:
            self.listaParametros.append(parametros(parametrosC[i].nombre,parametrosC[i].unidad,parametrosC[i].valoresParametro))            
        #print "Se ha creado el Metodo de Solucion"
        
    def __del__(self):
        #print "Se ha eliminado el Metodo de Solucion"
	return

    def gettipo(self):
        return "solucion"

    def getoptimizaciones(self):
        return self.optimizaciones

    def setearValores(self, valores):
        i=0
        self.dominio.valores=[]
        for i in range(len(valores)):
            #print "indice "+str(i)
            ##Se crea una nueva instancia de valoresparametros que va a tener un link bidireccional con parametros            
            v=valoresParametros(valores[i], self.listaParametros[i])
            ##al parametro se le asocia el valor
            self.listaParametros[i].valoresParametro=v
            ## Tambien se asocia el valor al dominio poara que este lo guarde para futuros metodos de solucion
            if self.asociar!=None and self.asociar==True :
                self.dominio.valores.append(v)
                #print "valor seteado para  ",self.listaParametros[i].nombre," es: ",v.valor

    def gradienteX(self):
        return self.gxh

    def gradienteY(self):
        return self.gyh

    def minimoMatriz(self):
        return self.min

    def maximoMatriz(self):
        return self.max    
       
class metodoAnalitico(metodoSolucion):
    def __init__(self, dominio, parametros, asociar=None):
        self.aceptaBarrera=False
        metodoSolucion.__init__(self,dominio,parametros, asociar)
    def gettipo(self):
        return "analitico"

    ## Este meotod tiene que llamar alvaro al momento de graficar y le devuelve la matriz
    def calcular(self,tiempos, ti, tf,dt, nix, niy, xx,yy, X, Y):
               
        # Recorrer todo el dominio
        d=self.dominio

        ##Llamado a procesar la barrera.. para generar los pozos virtuales porque se duplican por precensia de la barrera
        if self.aceptaBarrera==True :
            d.procesarBarrera()
        
        #Se guardan los valores para usarlos en todos los metodos
        self.tiempos=tiempos
        self.xx=xx
        self.yy=yy        

        #Q=500
        #r=1

        #####ver como llamar la matriz de los tiempos
        ## por ahora consideramos que va a ser lineal que arranca en el tiempo 0 al 10

        ##se toman los tamanios de la discretizacion espacial y temporal
        ##la matriz se tiene que generar primero en y y dps en x para darle bien los datos a las graficas
        self.matrizDescenso=np.zeros((len(tiempos),len(yy),len(xx)), float)  
        #print self.matrizDescenso[1]
        ##Matrices para guardar los gradientes en x e y
        self.gyh=np.zeros((len(tiempos),len(yy),len(xx)), float)
        self.gxh=np.zeros((len(tiempos),len(yy),len(xx)), float)            

        ##dominio en x        
        ##xx = numpy.arange(0, d.ancho, 1)
        ### dominio en y
        ##yy = numpy.arange(0, d.alto, 1)        

        ##Obtener todos los pozos de observacion
        TodoslospozosObservacion=d.obtenerPozosdeObservacion()
        
        ##Matrices para el calculo de loS H0 niveles inciales
        H0=np.zeros((len(yy),len(xx)), float)
        cardx=0
        for x in xx:
            cardy=0
            for y in yy:
                #hay que cargar la matriz primero en el indice y luego en el x
                #Obtener el Ho llamando a la clase dominio
                H0[cardy,cardx]=d.calcularH0(x,y)
                cardy=cardy+1            
            cardx=cardx+1

        ##Se instancias de una para todos los tiempos una lista de Observaciones solucionadas para cada pozo de observacion
        for pozoObservacion in TodoslospozosObservacion:
            pozoObservacion.instanciarSolucionadas(d.calcularH0(pozoObservacion.x, pozoObservacion.y), tiempos)

        ## Para todos los tiempos se empieza desde los niveles iniciales
        cardt=0
        for t in tiempos:
            self.matrizDescenso[cardt,:,:]=H0[:,:]
            cardt=cardt+1
        
        ##se recupera todos los pozos de bombeo que hay en el sistema + los virtuales
        if self.aceptaBarrera==True :
            Todoslospbombeo=d.obtenerPBombeoYVirtuales()            
        else:
            Todoslospbombeo=d.obtenerPozosdeBombeo()

        #print "holaa" +str(Todoslospbombeo)
        
        for pozoBombeo in Todoslospbombeo:
            ###Esto se podria obtener desde el dominio        
            #pozoBombeo=self.dominio.obtenerPozoBombeo()
            x0=pozoBombeo.x
            y0=pozoBombeo.y
            #comentar cuando el pozo de bombeo esta bien posicioando
            #x0=5
            #y0=5
            print 'x0: ' + str(x0)
            print 'y0: ' + str(y0)

            ##Obtener el ensayo de bombeo, los caudales y tiempos(al menos hay uno) ...que pasa cuando hay mas de un ensayo asociado?????        
            bombeos=pozoBombeo.ensayos[0].devolverBProc()

            for bom in bombeos:
                print 'tiempos: '+str(bom.tiempo)
                print 'caudal: '+str(bom.caudal)
                
            cardt=0
            for t in tiempos:
                cardx=0
##                self.matrizDescenso[cardt,:,:]=H0[:,:]            
                for x in xx:
                    cardy=0
                    for y in yy:
                        #calculo de la distancia radial            
                        #sqrt(|X0-X1|^2 + |y0-y1|^2)
                        r=np.sqrt(np.square(x0-x) + np.square(y0-y))                                       
                        #print 'x: '+ str(x)+ 'y: '+str(y)+' r: '+str(r)
                    
                        for bom in bombeos:
        ##                  El tiempo t nunca puede ser 0, sino t da error                    
                            tpozo=bom.tiempo
                            Q=bom.caudal                    
                            ##Al restar deja una diferencia de 1.8 * 10-16 por eso el redondeo                        
                            tmandado=round(float(float(t)-float(tpozo)),14)



                            if tmandado>0:
                                #Aca se llama al metodo Theis para ese punto, lo que nos da el descenso 's'
                                #print 'r '+str(r)+'t '+str(tmandado)+'Q '+str(Q)
                                told=tmandado
                                try:
                                    s,dsdT,dsdS=self.calcularpozo(r, tmandado, Q)
                                except:
                                    print 'Error - r: ' + str(r) +'t: '+str(t) + 'Q: ' + str(Q) + 'x: '+str(x) + 'y: '+str(y)
                                    print 'T mandado: '+str(told) + 'T pozo: '+str(tpozo)
                                    s=0
                            else:
                                s=0

                            #if t>=0.3:
                            #    print 'Error - r: ' + str(r) +'t: '+str(t) + 'Q: ' + str(Q) + 'x: '+str(x) + 'y: '+str(y)

                            #if t==0.03:
                                #print 'Punto ('+str(x)+', '+str(y)+') pozo ('+str(x0)+', '+str(y0)+') caudal pozo: '+str(Q)+' tiempo pozo: '+str(tpozo)+' tiempo: '+str(t), '-Cual es el descenso: '+str(s)
                                #print 'r ('+str(r)+') caudal pozo: '+str(Q)+' tiempo : '+str(tmandado), '-Cual es el descenso: '+str(s)
                                
##                              print 'Que habia? '+ str(self.matrizDescenso[cardt,cardy,cardx])
                                #print 'Cual es el descenso: '+str(s)

                            #el nivel "h" se calcula como "h=Ho-s"
                            #print 'h: '+ str(h)+ 'H0: '+str(H0)+'s: '+str(s)
                            ##La matriz es tiempo t y despues y,x
                            self.matrizDescenso[cardt,cardy,cardx]=self.matrizDescenso[cardt,cardy,cardx]-s
                            #se incrementa el cardinal del tiempo

##                            if t==0.03:                                
##                                print 'h: '+str(self.matrizDescenso[cardt,cardy,cardx])
                            
                        ##calculo de maximos y minimos
                        if self.matrizDescenso[cardt,cardy,cardx]>self.max:
                            self.max=self.matrizDescenso[cardt,cardy,cardx]
                        if self.matrizDescenso[cardt,cardy,cardx]<self.min:
                            self.min=self.matrizDescenso[cardt,cardy,cardx]
                        cardy=cardy+1            
                    cardx=cardx+1
                
                #[gxh(:,:,k),gyh(:,:,k)] = gradient(-h(:,:,k),xx(2),yy(niy-1));
                #Matplotlib t invierte el orden de las matrices a diferenciade matlab
                #[py,px] = np.gradient(z,1,1)
                [self.gyh[cardt,:,:],self.gxh[cardt,:,:]] = np.gradient(-self.matrizDescenso[cardt,:,:],xx[1],yy[len(yy)-2])            


                #print "arranco el calculo"

                #Calculo para todos los pozos de observacion
                for pozoObservacion in TodoslospozosObservacion:
                    x=pozoObservacion.x
                    y=pozoObservacion.y
                    #calculo de la distancia radial            
                    #sqrt(|X0-X1|^2 + |y0-y1|^2)
                    r=np.sqrt(np.square(x0-x) + np.square(y0-y))                                       
                    #print 'x: '+ str(x)+ 'y: '+str(y)+' r: '+str(r)
                    for bom in bombeos:
    ##                  El tiempo t nunca puede ser 0, sino t da error                    
                        tpozo=bom.tiempo
                        Q=bom.caudal                    
                        ##Al restar deja una diferencia de 1.8 * 10-16 por eso el redondeo                        
                        tmandado=round(float(float(t)-float(tpozo)),14)
                        #print tmandado
                        if tmandado>0:
                            #Aca se llama al metodo Theis para ese punto, lo que nos da el descenso 's'
                            #print 'r '+str(r)+'t '+str(tmandado)+'Q '+str(Q)
                            told=tmandado
                            try:
                                s,dsdT,dsdS=self.calcularpozo(r, tmandado, Q)
                                
                                #if t==0.3:
                                    #print 'Error - r: ' + str(r) +'t: '+str(t) + 'Q: ' + str(Q) + 'x: '+str(x) + 'y: '+str(y)+'s: '+str(s)                                
                            except:
                                print 'Error - r: ' + str(r) +'t: '+str(t) + 'Q: ' + str(Q) + 'x: '+str(x) + 'y: '+str(y)
                                print 'T mandado: '+str(told) + 'T pozo: '+str(tpozo)
                                s=0
                        else:
                            s=0

                        #Se actualizan solo las observaciones solucionadas
                        pozoObservacion.obssolucionadas[cardt]=pozoObservacion.obssolucionadas[cardt]-s

                #se incrementa el cardinal del tiempo
                cardt=cardt+1

                            
        ## correccion por barrera
        ## if haybarrera
        if len(d.listaRecta)>0 and self.aceptaBarrera==True:
            ##se obtiene la primera recta
            recta=d.listaRecta[0]
            alfa,beta,gamma=recta.devolverCoef()            

            cardx=0
            for x in xx:
                cardy=0
                for y in yy:
                   #hay que cargar la matriz primero en el indice y luego en el x
                    if np.sign(x*alfa + y*beta +gamma)!= recta.signo:
                        ## h(j,i,:) =h0(j,i);                        
                        self.matrizDescenso[:,cardy,cardx]=H0[cardy,cardx]
                        self.gyh[:,cardy,cardx]=0
                        self.gxh[:,cardy,cardx]=0
##                        print self.matrizDescenso[10,cardy,cardx]
                    cardy=cardy+1            
                cardx=cardx+1
        
        
        ##ahora se soluciono lo del 0       
        #zz = self.matrizDescenso[0]
        #print "zz "        
        #print zz

        ##descomentar para generar la grafica atraves de esta clase
####        fig = Figure(figsize = (1.8 * 4, 2.4 * 4))
##        self.axu = fig.add_subplot(2, 2, 1)
##        self.axd = fig.add_subplot(2, 2, 2)
##        self.axt = fig.add_subplot(2, 2, 3, projection = '3d')
##        self.axc = fig.add_subplot(2, 2, 4)
##        fig.subplots_adjust(hspace=.2, wspace=.3, bottom=.07, left=.08, right=.92, top=.94)
##        self.fig = fig
        
##        ax = self.axt
##        surf = ax.plot_surface(X, Y, zz, rstride=1, cstride=1, cmap=cm.jet, linewidth=0, antialiased=True)
        
        return self.matrizDescenso


    ##Metodo que se llama luego de la Optimizacion, para graficar los pozos de observacions con S y T optimos
    def funcionObjetivo(self,pozoObservacion):
        #Topt=self.listaParametros[0].valoresParametro.valor
        #Sopt=self.listaParametros[1].valoresParametro.valor

        ##se recupera todos los pozos de bombeo que hay en el sistema + los virtuales
        if self.aceptaBarrera==True :
            Todoslospbombeo=self.dominio.obtenerPBombeoYVirtuales()
        else:
            Todoslospbombeo=self.dominio.obtenerPozosdeBombeo()        
        ##Obtener todos los pozos de observacion
##        TodoslospozosObservacion=self.dominio.obtenerPozosdeObservacion()        
        ##usar la misma discretizacion para el calculo del metodo de solucion
        tiempos=self.tiempos

        ##Se instancias de una para todos los tiempos una lista de Niveles optimos para cada pozo de observacion
##        for pozoObservacion in TodoslospozosObservacion:
        pozoObservacion.instanciarNivelesOptimos(self.dominio.calcularH0(pozoObservacion.x, pozoObservacion.y), tiempos)        
        
        for pozoBombeo in Todoslospbombeo:
            x0=pozoBombeo.x
            y0=pozoBombeo.y       
            bombeos=pozoBombeo.ensayos[0].devolverBProc()
                
            cardt=0
            for t in tiempos:        
                #Calculo para todos los pozos de observacion
##                for pozoObservacion in TodoslospozosObservacion:
                x=pozoObservacion.x
                y=pozoObservacion.y
                #calculo de la distancia radial            
                #sqrt(|X0-X1|^2 + |y0-y1|^2)
                r=np.sqrt(np.square(x0-x) + np.square(y0-y))
                for bom in bombeos:
                ## El tiempo t nunca puede ser 0, sino t da error                    
                    tpozo=bom.tiempo
                    Q=bom.caudal                    
                    ##Al restar deja una diferencia de 1.8 * 10-16 por eso el redondeo                        
                    tmandado=round(float(float(t)-float(tpozo)),14)

                    if tmandado>0:
                        #Aca se llama al metodo Theis para ese punto, lo que nos da el descenso 's'
                        #print 'r '+str(r)+'t '+str(tmandado)+'Q '+str(Q)
                        told=tmandado
                        try:
                            #s,dsdT,dsdS=self.calcularpozoGenerico(r, tmandado, Q, Topt, Sopt)
                            s,dsdT,dsdS=self.calcularpozo(r, tmandado, Q)
                        except:
                            print 'Error - r: ' + str(r) +'t: '+str(tmandado) + 'Q: ' + str(Q) + 'x: '+str(x) + 'y: '+str(y)
                            print 't mandado: '+str(told) + 't pozo: '+str(tpozo)
                            s=0.0
                    else:
                        s=0.0

                    #print 'Error - r: ' + str(r) +'t: '+str(tmandado) + 'Q: ' + str(Q) + 'T: '+str(Topt) + 'S: '+str(Sopt)+'desc '+str(float(s)) 

                    #Se actualizan los niveles Optimos                      
                    pozoObservacion.nivelesOptimos[cardt]=float(pozoObservacion.nivelesOptimos[cardt])-float(s)
                #se incrementa el cardinal del tiempo
                cardt=cardt+1                
        #pozoObservacion.nivelesOptimos[0]=9.0


    ##Metodo que se llama desde la Optimizacion, para graficar hayar los desdencos dentro del algoritmo
    def funcionObjetivo2(self,p,t,mostrar=None):
        x=p.x
        y=p.y
        #Topt=self.listaParametros[0].valoresParametro.valor
        #Sopt=self.listaParametros[1].valoresParametro.valor        
        ##se recupera todos los pozos de bombeo que hay en el sistema + los virtuales
        if self.aceptaBarrera==True :
            Todoslospbombeo=self.dominio.obtenerPBombeoYVirtuales()
        else:
            Todoslospbombeo=self.dominio.obtenerPozosdeBombeo()  
        
        descenso=0

        if mostrar!=None:
            print "acepta ",self.aceptaBarrera
            print "todoslospboimbeo ", Todoslospbombeo 
            
            #print 'x_obs :', x, 'y_obs :', y, 't_med :', t                                      
                                        
        
        for pozoBombeo in Todoslospbombeo:
            x0=pozoBombeo.x
            y0=pozoBombeo.y       
            bombeos=pozoBombeo.ensayos[0].devolverBProc()

            #calculo de la distancia radial            
            #sqrt(|X0-X1|^2 + |y0-y1|^2)
            r=np.sqrt(np.square(x0-x) + np.square(y0-y))

            for bom in bombeos:
            ## El tiempo t nunca puede ser 0, sino t da error                    
                tpozo=bom.tiempo
                Q=bom.caudal                    
                ##Al restar deja una diferencia de 1.8 * 10-16 por eso el redondeo                        
                tmandado=round(float(float(t)-float(tpozo)),14)

                if tmandado>0:
                    #Aca se llama al metodo Theis para ese punto, lo que nos da el descenso 's'
                    try:
                        #s,dsdT,dsdS=self.calcularpozoGenerico(r, tmandado, Q, Topt, Sopt)
                        s,dsdT,dsdS=self.calcularpozo(r, tmandado, Q)
                    except:
                        s=0.0
                else:
                    s=0.0
                #Se actualizan los niveles Optimos
                descenso=descenso + float(s)

                #if mostrar!=None:
                    #print 'p(i).x :', x0,'p(i).y :', y0,' p(i).q :', Q
                    
        return descenso


    

class metodoNumerico(metodoSolucion):
    def __init__(self, dominio, parametros, asociar=None):
        self.aceptaBarrera=False
        metodoSolucion.__init__(self,dominio,parametros, asociar)
    def gettipo(self):
        return "numerico"  

