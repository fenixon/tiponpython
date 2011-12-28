class dominio(object):

    def __init__(self):
        self.alto = 30
        self.ancho = 30
        self.listaBarreras = []
        self.listaCondicionesExternas = []
        print "Se ha creado el Dominio"
        
        #Agregar el a, b, c de la ecuacion del plano. Valores que
        ##  deben ser seteados desde la creacion del proyecto
        self.a=1
        self.b=2
        self.c=3             

    def __del__(self):
        print "Se ha eliminado el Dominio"

        #Agregar el metodo para la ecuacion del plano
    def calcularH0(self, x,y):
##      Al final el nivel en un punto de coordenadas "xp" e "yp"
##      se calcula como H0= a*xp+b*yp+c  -s1(xp,yp,t)        
        return self.a*x + self.b*y + self.c
