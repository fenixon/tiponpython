    def instanciaoptimizacion(self,metodo):
        ##igual que antes hay que guardar una instancia de objeto, cuyo tipo que ser el determinado por el algoritmo  
        objeto=eval(str(metodo) + "()")
        self.dominio.optimizaciones[metodo]=objeto
        self.dominio.optimizaciones[metodo].pozos=[]
        return self.dominio.optimizaciones[metodo]


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
                        self.dominio.optimizaciones[clave].pozos.append(idElemento)
                if (token==False): #Si no existe el metodo, lo creo y le agrego el pozo
                    self.dominio.optimizaciones[metodo].pozos=[]
                    self.dominio.optimizaciones[metodo].pozos.append(idElemento)      
                    #self.dominio.listaPozoOptimiza[metodo]= ui
                              
                #self.dominio.optimizaciones[metodo]= ui
        print "se agrego a la lista de optimizaciones" 