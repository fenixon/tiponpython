"""
	tiponpython Simulacion de ensayos de acuiferos
	Copyright 2012 Andres Pias, Mathias Chubrega, Alvaro Correa, Sebastian Daloia, Jesus Guibert
	
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

    def copiaSuperficial(self):
        e=ensayobombeo(self.__bombeos, self.id, self.nombre)
        e.__bombeosproc=self.__bombeosproc
        return e
