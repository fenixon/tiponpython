# -*- coding: utf-8 -*-
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
# Form implementation generated from reading ui file 'verensayos.ui'
#
# Created: Wed Dec 14 13:58:11 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import modelotabla
import bombeo
import ensayobombeo
import controlador

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog, cont):
        global ContEnsayo
        ContEnsayo=cont        
        
        Dialog.setObjectName(_fromUtf8("verensayosbombeo"))
        Dialog.resize(576, 276)
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Ver Ensayos de Bombeo", None, QtGui.QApplication.UnicodeUTF8))

## Se obtienen los ensayos lamcaneados en el controlador
        ens=ContEnsayo.ensayos
##      Se toma el primero de ellos
        e=ens[0]
##      Se instancia un modelo tabla con los ensayos y los nombres de los campos a mostrar(id)
        self.model=modelotabla.modelotabla(ens, e.datosNombre())
        
        self.tablita= QtGui.QTableView(Dialog)
        self.tablita.setGeometry(QtCore.QRect(20, 40, 256, 192))
        self.tablita.setObjectName(_fromUtf8("tablita"))
        self.tablita.setModel(self.model)

        self.tablita2= QtGui.QTableView(Dialog)
        self.tablita2.setGeometry(QtCore.QRect(300, 40, 256, 192))
        self.tablita2.setObjectName(_fromUtf8("tablita2"))     

##      QtCore.QObject.connect(self.tablita, QtCore.SIGNAL(_fromUtf8("cellClicked()")), self.elegirensayo)
        QtCore.QObject.connect(self.tablita, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), self.elegirensayo)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def elegirensayo(self, item):
##      print self.model.data(item,QtCore.Qt.DisplayRole)
##      Se Llama al metodo objeto del modelotabla para retornar el ensayo original asociado
        e=self.model.objeto(item)
        print "se elijiio ensayo "+str(e.id)        
       
##      Se crea una instancia de bombeo para tomar los nombres de los atributos        
        aux=bombeo.bombeo(0,0)
##      Se instancia un modelo tabla con el ensayo seleccionado y los atributos a mostrar(tiempo, caudal)
        model2=modelotabla.modelotabla(e.devolverB(), aux.datosNombre())
##      Se setea el modelo en la tabla 2
        self.tablita2.setModel(model2)  

    def retranslateUi(self, Dialog):
        pass

    

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    frmVerBombeo = QtGui.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(frmVerBombeo)
    frmVerBombeo.show()
    sys.exit(app.exec_())
