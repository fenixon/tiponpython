import numpy as np
from valoresParametros import valoresParametros
##from matplotlib.figure import Figure
####from mpl_toolkits.mplot3d.axes3d import Axes3D
##import matplotlib.mlab as mlab
##from matplotlib import cm


class metodoSolucion(object):

    def __init__(self, dominio, parametros): 
##        self.paramcard=cardinales
        self.dominio=dominio
        ## Asociar el metodo al dominio
        self.dominio.metodo=self                      
        self.listaParametros=[]
        for i in self.paramcard:
            self.listaParametros.append(parametros[i])
            
        #print "Se ha creado el Metodo de Solucion"
        
    def __del__(self):
        #print "Se ha eliminado el Metodo de Solucion"
	return

    def setearValores(self, valores):
        i=0
        for i in range(len(valores)):
            #print "indice "+str(i)
            ##Se crea una nueva instancia de valoresparametros que va a tener un link bidireccional con parametros            
            v=valoresParametros(valores[i], self.listaParametros[i])
            ##al parametro se le asocia el valor
            self.listaParametros[i].valoresParametro=v
            ## Tambien se asocia el valor al dominio poara que este lo guarde para futuros metodos de solucion
            self.dominio.valores.append(v)

    ## Este meotod tiene que llamar alvaro al momento de graficar y le devuelve la matriz
    def calcular(self,tiempos,xx,yy):
        # Se indentifica donde esta el pozo de bombeo           
        # Por ahora tomar el primero de bombeo que se detecte. Luego cambia cuando hayan mas pozos
                
        # Recorrer todo el dominio
        d=self.dominio

        #Q=500
        #r=1

        #####ver como llamar la matriz de los tiempos
        ## por ahora consideramos que va a ser lineal que arranca en el tiempo 0 al 10

        ##el tiempo va desde 0 a 4, el 0 no se usa
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
        Todoslospbombeo=d.obtenerPBombeoYVirtuales()
        
        
        for pozoBombeo in Todoslospbombeo:
            ###Esto se podria obtener desde el dominio        
            #pozoBombeo=self.dominio.obtenerPozoBombeo()
            x0=pozoBombeo.x
            y0=pozoBombeo.y
            #comentar cuando el pozo de bombeo esta bien posicioando
            #x0=5
            #y0=5
##            print 'x0: ' + str(x0)
##            print 'y0: ' + str(y0)

            ##Obtener el ensayo de bombeo, los caudales y tiempos(al menos hay uno) ...que pasa cuando hay mas de un ensayo asociado?????        
            bombeos=pozoBombeo.ensayos[0].devolverBProc()

##            for bom in bombeos:
##                print 'tiempos: '+str(bom.tiempo)
##                print 'caudal: '+str(bom.caudal)
                
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


##                            if t==0.03:
##                                print 'Punto ('+str(x)+', '+str(y)+') pozo ('+str(x0)+', '+str(y0)+') caudal pozo: '+str(Q)+' tiempo pozo: '+str(tpozo)+' tiempo: '+str(t)
##                                print 'Que habia? '+ str(self.matrizDescenso[cardt,cardy,cardx])
##                                print 'Cual es el descenso: '+str(s)

                            #el nivel "h" se calcula como "h=Ho-s"
                            #print 'h: '+ str(h)+ 'H0: '+str(H0)+'s: '+str(s)
                            ##La matriz es tiempo t y despues y,x
                            self.matrizDescenso[cardt,cardy,cardx]=self.matrizDescenso[cardt,cardy,cardx]-s
                            #se incrementa el cardinal del tiempo

##                            if t==0.03:                                
##                                print 'h: '+str(self.matrizDescenso[cardt,cardy,cardx])
                            
                            
                        cardy=cardy+1            
                    cardx=cardx+1
                
                #[gxh(:,:,k),gyh(:,:,k)] = gradient(-h(:,:,k),xx(2),yy(niy-1));
                #Matplotlib t invierte el orden de las matrices a diferenciade matlab
                #[py,px] = np.gradient(z,1,1)
                [self.gyh[cardt,:,:],self.gxh[cardt,:,:]] = np.gradient(-self.matrizDescenso[cardt,:,:],xx[1],yy[len(yy)-2])            


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

                        #Se actualizan solo las observaciones solucionadas
                        pozoObservacion.obssolucionadas[cardt]=pozoObservacion.obssolucionadas[cardt]-s

                #se incrementa el cardinal del tiempo
                cardt=cardt+1

                            



        
        
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

    def gradienteX(self):
        return self.gxh

    def gradienteY(self):
        return self.gyh
    

class metodoAnalitico(metodoSolucion):
    pass

class metodoNumerico(metodoSolucion):
    pass
