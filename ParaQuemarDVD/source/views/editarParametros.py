# -*- coding: utf-8 -*-
"""
	tiponpython Simulacion de ensayos de acuiferos
	Copyright 2012 Andres Pias, Alvaro Correa, Jesus Guibert
	
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
from PyQt4 import QtCore, QtGui
import sys
sys.path.append("../models")
from controlador import *

import metodoSolucion
import parametros
from Hantush import Hantush
from theis import Theis
from DiferenciaFinita import DiferenciaFinita
import numpy as np

try:

    _fromUtf8 = QtCore.QString.fromUtf8

except AttributeError:

    _fromUtf8 = lambda s: s

class cajaTexto(QtGui.QLineEdit):

        def __init__(self, padre):

            super(cajaTexto, self).__init__(padre)
            self.setFocusPolicy(QtCore.Qt.StrongFocus)
            self.setText('0')

        def focusOutEvent(self, evento):

            if str(self.text()) == '':

                self.setText('0')

            evento.lostFocus()
            self.setStyleSheet("background-color: white")
            self.setCursor(QtCore.Qt.IBeamCursor)

        def focusInEvent(self, evento):

            if self.text()=='0' :

                self.setText('')

            self.setStyleSheet("background-color:  rgb(40, 255, 40)")
            #evento.gotFocus()
            self.setCursor(QtCore.Qt.IBeamCursor)

        def leaveEvent(self, evento):

            self.setCursor(QtCore.Qt.IBeamCursor)

        def mouseDoubleClickEvent(self, evento):

            evento.ignore()

        def mouseMoveEvent(self, evento):

            evento.ignore()

class UifrmEditarParametros(QtGui.QDialog):

    def setupUi(self, frmNuevoProyecto,controlo):

        global controlador
        controlador = controlo

        global ventana
        ventana = frmNuevoProyecto
        frmNuevoProyecto.setObjectName(_fromUtf8("frmNuevoProyecto"))
        frmNuevoProyecto.resize(405, 496)
        frmNuevoProyecto.setWindowTitle(QtGui.QApplication.translate("frmNuevoProyecto", "Editar valores de Parámetros hidrológicos", None, QtGui.QApplication.UnicodeUTF8))
        self.esNuevo = True
        self.btnNuevo = QtGui.QPushButton(frmNuevoProyecto)
        self.btnNuevo.setGeometry(QtCore.QRect(230, 460, 99, 23))
        self.btnNuevo.setText(QtGui.QApplication.translate("frmNuevoProyecto", "Guardar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnNuevo.setObjectName(_fromUtf8("btnNuevo"))

        self.gbParametrosDominio = QtGui.QGroupBox(frmNuevoProyecto)
        self.gbParametrosDominio.setGeometry(QtCore.QRect(30, 430, 351, 21))
        self.gbParametrosDominio.setTitle(QtGui.QApplication.translate("frmNuevoProyecto", "Parametros", None, QtGui.QApplication.UnicodeUTF8))
        self.gbParametrosDominio.setObjectName(_fromUtf8("gbParametrosDominio"))

        #seteando dimension de interfaz por defecto
        ventanaY=80
        groupboxY=21
        botonY = 40
        elementoNuevoY =20
        self.gbParametrosDominio.setGeometry(QtCore.QRect(30, 430, 351, groupboxY))
        self.btnNuevo.setGeometry(QtCore.QRect(230, botonY , 99, 23))
        ventana.resize(405, ventanaY)

        #agregando nuevos elementos
        self.val = QtGui.QDoubleValidator(-100, 900, 5, self.gbParametrosDominio)

        for n in range(0,len(controlador.metodo.listaParametros)):

            ejec='self.txtParam'+ str(n) +' = cajaTexto(self.gbParametrosDominio)'
            exec(ejec)
            ejec='self.txtParam'+ str(n) +'.setGeometry(QtCore.QRect(200, '+ str(elementoNuevoY) +', 113, 28))'
            exec(ejec)
            ejec='self.txtParam'+ str(n) +'.setObjectName(_fromUtf8("txtParam'+ str(n) +'"))'
            exec(ejec)
            ejec='self.txtParam'+ str(n) +'.setValidator(self.val)'
            exec(ejec)
            ejec='self.txtParam'+ str(n) +'.setVisible(True)'
            exec(ejec)
##            print 'hola caja'
            ejec= 'self.lblParam'+ str(n) +' = QtGui.QLabel(self.gbParametrosDominio)'
            exec(ejec)
            ejec= 'self.lblParam'+ str(n) +'.setGeometry(QtCore.QRect(10, '+ str(elementoNuevoY+7) +', 171, 18))'
            exec(ejec)
            ejec= 'self.lblParam'+ str(n) +'.setText(QtGui.QApplication.translate("frmNuevoProyecto", str(controlador.metodo.listaParametros['+ str(n) +'].nombre), None, QtGui.QApplication.UnicodeUTF8))'
            exec(ejec)
            ejec= 'self.lblParam'+ str(n) +'.setObjectName(_fromUtf8("lblParam'+ str(n) +'"))'
            exec(ejec)
            ejec= 'self.lblParam'+ str(n) +'.setAlignment(QtCore.Qt.AlignHCenter)'
            exec(ejec)
            ejec= 'self.lblParam'+ str(n) +'.setVisible(True)'
            exec(ejec)
            ejec='self.txtParam'+ str(n) +'.setText(str(controlador.metodo.listaParametros['+ str(n) +'].valoresParametro.valor))'
            exec(ejec)            

            #alargando la interfaz
            elementoNuevoY = elementoNuevoY + 40
            groupboxY = groupboxY + 40
            ventanaY = ventanaY + 40
            botonY = botonY + 40
            ventana.resize(405, ventanaY)
            self.gbParametrosDominio.setGeometry(QtCore.QRect(30, 10 , 351, groupboxY))
            self.btnNuevo.setGeometry(QtCore.QRect(230, botonY , 99, 23))


        self.retranslateUi(frmNuevoProyecto)
        QtCore.QObject.connect(self.btnNuevo, QtCore.SIGNAL(_fromUtf8("clicked()")), self.guardarSalir)
        QtCore.QMetaObject.connectSlotsByName(frmNuevoProyecto)

    def guardarSalir(self):

        lista=[]

        for n in range(0,len(controlador.metodo.listaParametros)):
            ejec='lista.append(float(self.txtParam'+ str(n) +'.text()))'
            exec(ejec)

        controlador.metodo.setearValores(lista)        

        QtGui.QMessageBox.information(self,
            u"Información",
            u"Los nuevos valores han sido almacenados")

        ventana.close()

    def retranslateUi(self, frmNuevoProyecto):
        pass

if __name__ == "__main__":

    p=controlador.Proyecto()
    dominio.alto = 3000
    dominio.ancho = 3000
    dominio.a=0
    dominio.b=0
    dominio.c=10

    app = QtGui.QApplication(sys.argv)
    frmNuevoProyecto = QtGui.QWidget()
    ui = UifrmEditarParametros()
    #m=Theis(p.dominio, p.parametros, True)
    #m.setearValores([1000,1.e-4])
    m=Hantush(p.dominio, p.parametros, True) 
    m.setearValores([1000,1.e-4,676.7])
    
    p.metodo=m    
    ui.setupUi(frmNuevoProyecto,p)
    frmNuevoProyecto.show()
    sys.exit(app.exec_())
