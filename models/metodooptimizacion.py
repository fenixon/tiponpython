from numpy import *
from parametros import *
from valoresParametros import valoresParametros
import controlador
class metodooptimizacion(object):

    def __init__(self):
        
        self.matrizDescenso = zeros( (3,1) )

        self.listaObservaciones = []
        
        self.listaParametros=[]
        self.params={}

    def __del__(self):
        print "Objeto eliminado"

    def setearValores(self, valores):
        i=0
        for i in range(len(valores)):
            ##Se crea una nueva instancia de valoresparametros que va a tener un link bidireccional con parametros            
            v=valoresParametros(valores[i], self.listaParametros[i])
            ##al parametro se le asocia el valor
            self.listaParametros[i].valoresParametro=v
            ## Tambien se asocia el valor al dominio poara que este lo guarde para futuros metodos de solucion
    def setvalor(self,indice,valor):
        print "cambio el valor al parametro: " +self.listaParametros[indice].nombre
        print "cuyo valor es:" + self.listaParametros[indice].valoresParametro.valor
        self.listaParametros[indice].valoresParametro.valor=valor
    def getlistaparametros(self):
        #return "aca va la lista de parametros"
        return self.listaParametros
    def calcular():
        pass