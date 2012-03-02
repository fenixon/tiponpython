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

class observacionesensayo(object):
    def __init__(self,observaciones, ido, nombre):
        self.__observaciones=observaciones
        self.id=ido
        self.nombre=nombre
    def devolverO(self):
        return self.__observaciones
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
        o=observacionesensayo(self.__observaciones, self.id, self.nombre)
        return o
