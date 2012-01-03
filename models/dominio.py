class dominio(object):

    def __init__(self):
        self.alto = 50
        self.ancho = 50
        self.listaBarreras = []
        self.listaPozo=[]
        self.listaCondicionesExternas = []
        print "Se ha creado el Dominio"
        #Lista que guarda los pozos y el metodo de optimizacion asociado al mismo
        self.listaPozoOptimiza ={}        
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
        print "lista de pozos"
        print self.listaPozo
        for p in self.listaPozo:
            ## si tiene ensayos entonces es de bombeo se recupera el primero           
            if len(p.ensayos)>0:
                print p
                return p
                
    def obtenerPozoObservacion(self):
        for p in self.listaPozo:
            ## si tiene ensayos entonces es de bombeo se recupera el primero           
            if len(p.observaciones)>0:
                print p
                return p                