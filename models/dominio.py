class dominio(object):

    def __init__(self):
        self.alto = 40
        self.ancho = 40
        self.listaBarreras = []
        self.listaCondicionesExternas = []
        print "Se ha creado el Dominio"
        
        #Agregar el a, b, c de la ecuacion del plano. Valores que
        ##  deben ser seteados desde la creacion del proyecto
        self.a=1
        self.b=-1
        self.c=0             

    def __del__(self):
        print "Se ha eliminado el Dominio"

        #Agregar el metodo para la ecuacion del plano
    def calcularH0(self, x,y):
##      Al final el nivel en un punto de coordenadas "xp" e "yp"
##      se calcula como H0= a*xp+b*yp+c  -s1(xp,yp,t)        
        return self.a*x + self.b*y + self.c
