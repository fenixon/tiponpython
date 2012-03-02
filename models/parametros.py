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

class parametros(object):

    def __init__(self, nombre, unidad, valoresParametro=None):
        self.nombre = nombre
        self.unidad = unidad
        self.valoresParametro = valoresParametro

    def __del__(self):
        print "Objeto eliminado"
