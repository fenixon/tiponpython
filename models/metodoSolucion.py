import numpy
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
            
        print "Se ha creado el Metodo de Solucion"
        
    def __del__(self):
        print "Se ha eliminado el Metodo de Solucion"

    def setearValores(self, valores):
        i=0
        for i in range(len(valores)):
            print "indice "+str(i)
            ##Se crea una nueva instancia de valoresparametros que va a tener un link bidireccional con parametros            
            v=valoresParametros(valores[i], self.listaParametros[i])
            ##al parametro se le asocia el valor
            self.listaParametros[i].valoresParametro=v
            ## Tambien se asocia el valor al dominio poara que este lo guarde para futuros metodos de solucion
            self.dominio.valores.append(v)

    ## Este meotod tiene que llamar alvaro al momento de graficar y le devuelve la matriz
    def calcular(self):
        # Se indentifica donde esta el pozo de bombeo           
        # Por ahora tomar el primero de bombeo que se detecte. Luego cambia cuando hayan mas pozos
        
        ###Esto se podria obtener desde el dominio        
        pozoBombeo=self.dominio.obtenerPozoBombeo()
        x0=pozoBombeo.x
        y0=pozoBombeo.y
        #comentar cuando el pozo de bombeo esta bien posicioando
        #x0=5
        #y0=5

        print 'x0: ' + str(x0)
        print 'y0: ' + str(y0)

        ##Obtener el ensayo de bombeo, los caudales y tiempos(al menos hay uno) ...que pasa cuando hay mas de un ensayo asociado?????        
        bombeos=pozoBombeo.ensayos[0].devolverB()    
        
        # Recorrer todo el dominio
        d=self.dominio

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

                #print 'x: '+ str(x)+ 'y: '+str(y)+' r: '+str(r)

                for bom in bombeos:
##                  El tiempo t nunca puede ser 0, sino t da error                    
                    t=bom.tiempo
                    Q=bom.caudal

#Aca se llama al metodo Theis para ese punto, lo que nos da el descenso 's'
## Esto son los parametros q se mandan                    
##                    print 'r '+str(r)
##                    print 't '+str(t)
##                    print 'Q '+str(Q)
##                    print 'T '+str(T)
##                    print 'S '+str(S)
                    
                    s,dsdT,dsdS=self.calcularpozo(r, t, Q)                    
                
                    #el nivel "h" se calcula como "h=Ho-s"
                    h=H0-s

                    #print 'h: '+ str(h)+ 'H0: '+str(H0)+'s: '+str(s)                    
                    
                    #Operar y generar la matriz
                    ##La matriz es tiempo t y despues x,y
                    self.matrizDescenso[t,x,y]=h      
        
        X, Y = numpy.meshgrid(xx, yy)
##      se soluciona desd el tiempo 1 porque el t=0 da error al dividir        
        zz = self.matrizDescenso[1]
        print "zz "        
        print zz

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


    

class metodoAnalitico(metodoSolucion):
    pass

class metodoNumerico(metodoSolucion):
    pass
