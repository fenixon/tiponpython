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

