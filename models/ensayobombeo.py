from bombeo import bombeo

class ensayobombeo(object):
    def __init__(self,bombeos, idb, nombre):                
        self.__bombeos=bombeos
        self.__bombeosproc=self.proceso(bombeos)
        self.id=idb
        self.nombre=nombre
    ##postproceos
    def proceso(self, bombeos):
        #solo se hace si hay mas de un ensayo de bombeo
        #nuevo lista de bombeos procesada
        nuevaBombeos=[]
        ##Se comienza agregando el primer bombeo recibido
        nuevaBombeos.append(bombeos[0])
        if len(bombeos)>1:           
            
            #se modifica a partir de la segunda medida
            for j in range(1,len(bombeos)):               
                 
                t=bombeos[j].tiempo
                c=0.0
                for k in range(1,j+1):
                    c=c-bombeos[k-1].caudal
                #p(new).t(1)=p(i).t(j);
                nb=bombeo(t,c)

                nuevaBombeos.append(nb)

        return nuevaBombeos   
            
    def devolverB(self):
        return self.__bombeos 
    def devolverBProc(self):
        return self.__bombeosproc
    def setearBProc(self, bombeos):
        self.__bombeosproc=bombeos
    def devolverAt(self, indice):
        if indice==0 :
            return self.id
        else:
            if indice==1:
                return self.nombre
    def datosNombre(self):
        return ["Id", "Nombre"]
##        self.id=self.generarId()

##    def generarId(self):
        #a implementar un mecanismo para generar id
##        return 1
        
