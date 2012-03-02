"""
	tiponpython Simulacion de ensayos de acuiferos
	Copyright 2012 Andres Pias, Alvaro Correa
	
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

from PyQt4 import QtGui, QtCore, uic
import sys

class modelotabla(QtCore.QAbstractTableModel):

    def __init__(self, datos = [], campos=[],  parent = None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.__datos=datos
        self.__campos=campos

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.__campos[section];
            else:
                return QtCore.QString("%1").arg(section)
    
    def rowCount(self, parent):
        return len(self.__datos)

    def columnCount(self, parent):
        return len(self.__campos)

    def data(self, index, role):
##        print "rol "+str(role)
        if role == QtCore.Qt.DisplayRole:
            fila=index.row()
            columna=index.column()          
            value=self.__datos[fila]
            return value.devolverAt(columna)
    
    def objeto(self,index):
         fila=index.row()
         columna=index.column()          
         return self.__datos[fila]

