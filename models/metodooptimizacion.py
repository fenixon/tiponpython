"""
	tiponpython Simulacion de ensayos de acuiferos
	Copyright 2012 Jesus Guibert
	
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

    def setpozo(self,pozo):
        self.pozo=pozo
        print "pozo a optimizar:" + str(pozo.id)

    def setcontrolador(self,controlador):
        self.controlador=controlador

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
