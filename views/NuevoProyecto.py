# -*- coding: utf-8 -*-
"""
	tiponpython Simulacion de ensayos de acuiferos
	Copyright 2012 Mathias Chubrega
	
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
import condicionExterna
import metodoSolucion
import parametros
from Hantush import Hantush
from theis import Theis
from DiferenciaFinita import DiferenciaFinita
import CondicionesExternas
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

class Ui_frmNuevoProyecto(object):

    def setupUi(self, frmNuevoProyecto,controlo):

        global controlador
        controlador = controlo

        global ventana
        ventana = frmNuevoProyecto
        frmNuevoProyecto.setObjectName(_fromUtf8("frmNuevoProyecto"))
        frmNuevoProyecto.resize(405, 496)
        frmNuevoProyecto.setWindowTitle(QtGui.QApplication.translate("frmNuevoProyecto", "Crear un nuevo proyecto", None, QtGui.QApplication.UnicodeUTF8))
        self.esNuevo = True
        self.btnNuevo = QtGui.QPushButton(frmNuevoProyecto)
        self.btnNuevo.setGeometry(QtCore.QRect(230, 460, 99, 23))
        self.btnNuevo.setText(QtGui.QApplication.translate("frmNuevoProyecto", "Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.btnNuevo.setObjectName(_fromUtf8("btnNuevo"))
        self.gbDimensionesDominio = QtGui.QGroupBox(frmNuevoProyecto)
        self.gbDimensionesDominio.setGeometry(QtCore.QRect(30, 10, 351, 111))
        self.gbDimensionesDominio.setTitle(QtGui.QApplication.translate("frmNuevoProyecto", "Dimensiones del dominio", None, QtGui.QApplication.UnicodeUTF8))
        self.gbDimensionesDominio.setObjectName(_fromUtf8("gbDimensionesDominio"))
        self.txtAlto = cajaTexto(self.gbDimensionesDominio)
        self.txtAlto.setGeometry(QtCore.QRect(200, 30, 113, 28))
        self.txtAlto.setObjectName(_fromUtf8("txtAlto"))
        self.txtAncho = cajaTexto(self.gbDimensionesDominio)
        self.txtAncho.setGeometry(QtCore.QRect(200, 70, 113, 28))
        self.txtAncho.setObjectName(_fromUtf8("txtAncho"))
        self.lblAlto = QtGui.QLabel(self.gbDimensionesDominio)
        self.lblAlto.setGeometry(QtCore.QRect(80, 40, 70, 18))
        self.lblAlto.setText(QtGui.QApplication.translate("frmNuevoProyecto", "Largo", None, QtGui.QApplication.UnicodeUTF8))
        self.lblAlto.setObjectName(_fromUtf8("lblAlto"))
        self.lblAncho = QtGui.QLabel(self.gbDimensionesDominio)
        self.lblAncho.setGeometry(QtCore.QRect(70, 80, 51, 18))
        self.lblAncho.setText(QtGui.QApplication.translate("frmNuevoProyecto", "Ancho", None, QtGui.QApplication.UnicodeUTF8))
        self.lblAncho.setObjectName(_fromUtf8("lblAncho"))
        self.gbParametrosDominio = QtGui.QGroupBox(frmNuevoProyecto)
        self.gbParametrosDominio.setGeometry(QtCore.QRect(30, 430, 351, 21))
        self.gbParametrosDominio.setTitle(QtGui.QApplication.translate("frmNuevoProyecto", "Parametros", None, QtGui.QApplication.UnicodeUTF8))
        self.gbParametrosDominio.setObjectName(_fromUtf8("gbParametrosDominio"))

        self.gbMetodo = QtGui.QGroupBox(frmNuevoProyecto)
        self.gbMetodo.setGeometry(QtCore.QRect(30, 280, 351, 141))
        self.gbMetodo.setTitle(QtGui.QApplication.translate("frmNuevoProyecto", "Metodos de solucion", None, QtGui.QApplication.UnicodeUTF8))
        self.gbMetodo.setObjectName(_fromUtf8("gbMetodo"))
        self.cmbTipo = QtGui.QComboBox(self.gbMetodo)
        self.cmbTipo.setGeometry(QtCore.QRect(200, 30, 111, 28))
        self.cmbTipo.setObjectName(_fromUtf8("cmbTipo"))
        self.cmbMetodo = QtGui.QComboBox(self.gbMetodo)
        self.cmbMetodo.setGeometry(QtCore.QRect(200, 70, 111, 28))
        self.cmbMetodo.setObjectName(_fromUtf8("cmbMetodo"))
        self.lblTipo = QtGui.QLabel(self.gbMetodo)
        self.lblTipo.setGeometry(QtCore.QRect(60, 30, 70, 18))
        self.lblTipo.setText(QtGui.QApplication.translate("frmNuevoProyecto", "Tipo", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTipo.setObjectName(_fromUtf8("lblTipo"))
        self.lblMetodo = QtGui.QLabel(self.gbMetodo)
        self.lblMetodo.setGeometry(QtCore.QRect(50, 70, 70, 18))
        self.lblMetodo.setText(QtGui.QApplication.translate("frmNuevoProyecto", "Metodo", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMetodo.setObjectName(_fromUtf8("lblMetodo"))
        self.btnCondicionesExternas = QtGui.QPushButton(self.gbMetodo)
        self.btnCondicionesExternas.setGeometry(QtCore.QRect(10, 100, 171, 27))
        self.btnCondicionesExternas.setText(QtGui.QApplication.translate("frmNuevoProyecto", "Condiciones Externas", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCondicionesExternas.setObjectName(_fromUtf8("btnCondicionesExternas"))
        self.groupBox = QtGui.QGroupBox(frmNuevoProyecto)
        self.groupBox.setGeometry(QtCore.QRect(30, 130, 351, 141))
        self.groupBox.setTitle(QtGui.QApplication.translate("frmNuevoProyecto", "Nivel Inicial Ho = a*x+b*y+c", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lblB = QtGui.QLabel(self.groupBox)
        self.lblB.setGeometry(QtCore.QRect(70, 70, 70, 18))
        self.lblB.setText(QtGui.QApplication.translate("frmNuevoProyecto", "b", None, QtGui.QApplication.UnicodeUTF8))
        self.lblB.setObjectName(_fromUtf8("lblB"))
        self.lblC = QtGui.QLabel(self.groupBox)
        self.lblC.setGeometry(QtCore.QRect(70, 110, 70, 18))
        self.lblC.setText(QtGui.QApplication.translate("frmNuevoProyecto", "c", None, QtGui.QApplication.UnicodeUTF8))
        self.lblC.setObjectName(_fromUtf8("lblC"))
        self.txtA = cajaTexto(self.groupBox)
        self.txtA.setGeometry(QtCore.QRect(200, 30, 113, 28))
        self.txtA.setObjectName(_fromUtf8("txtA"))
        self.txtB = cajaTexto(self.groupBox)
        self.txtB.setGeometry(QtCore.QRect(200, 70, 113, 28))
        self.txtB.setObjectName(_fromUtf8("txtB"))
        self.lblA = QtGui.QLabel(self.groupBox)
        self.lblA.setGeometry(QtCore.QRect(70, 30, 70, 18))
        self.lblA.setText(QtGui.QApplication.translate("frmNuevoProyecto", "a", None, QtGui.QApplication.UnicodeUTF8))
        self.lblA.setObjectName(_fromUtf8("lblA"))
        self.txtC = cajaTexto(self.groupBox)
        self.txtC.setGeometry(QtCore.QRect(200, 110, 113, 28))
        self.txtC.setObjectName(_fromUtf8("txtC"))

        tipos = ['Analitico','Numerico']
        self.cmbTipo.addItems(tipos)
        self.cambioTipo(self.cmbTipo.currentText())
        self.cambioMetodo(self.cmbMetodo.currentText())
        self.validador = QtGui.QDoubleValidator(-100, 900, 5, self.gbDimensionesDominio)
        self.txtAlto.setValidator(self.validador)
        self.txtAncho.setValidator(self.validador)
        self.txtA.setValidator(self.validador)
        self.txtB.setValidator(self.validador)
        self.txtC.setValidator(self.validador)

        self.retranslateUi(frmNuevoProyecto)
        QtCore.QObject.connect(self.btnNuevo, QtCore.SIGNAL(_fromUtf8("clicked()")), self.guardarSalir)
        QtCore.QObject.connect(self.cmbTipo, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.cambioTipo)
        QtCore.QObject.connect(self.btnCondicionesExternas, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ventanaCondicionesExternas)
        QtCore.QObject.connect(self.cmbMetodo, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.cambioMetodo)
        QtCore.QMetaObject.connectSlotsByName(frmNuevoProyecto)


    def ventanaCondicionesExternas(self):

        frmCondicionesExternas = QtGui.QDialog()
        ui = CondicionesExternas.Ui_frmCondicionesExternas()
        ui.setupUi(frmCondicionesExternas,controlador)
        frmCondicionesExternas.exec_()

    def cambioMetodo(self,nombreMetodo):

        if nombreMetodo != '':

            if(controlador.metodo != None):

                if self.esNuevo == False:

                    for n in range(0,len(controlador.metodo.listaParametros)):

                        ejec='self.txtParam'+ str(n) +'.setVisible(False)'
                        exec(ejec)
                        ejec='del self.txtParam'+ str(n)
                        exec(ejec)
                        print 'chau caja'
                        ejec='self.lblParam'+ str(n) +'.setVisible(False)'
                        exec(ejec)
                        ejec='del self.lblParam'+ str(n)
                        exec(ejec)

                self.esNuevo = False
                controlador.metodo = None

            ejec = 'metodo= %s(controlador.dominio, controlador.parametros, True)' % (nombreMetodo)
            exec(ejec)
            controlador.metodo=metodo

            #seteando dimension de interfaz por defecto
            ventanaY=496
            groupboxY=21
            botonY = 460
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
                print 'hola caja'
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

                #alargando la interfaz
                elementoNuevoY = elementoNuevoY + 40
                groupboxY = groupboxY + 40
                ventanaY = ventanaY + 40
                botonY = botonY + 40
                ventana.resize(405, ventanaY)
                self.gbParametrosDominio.setGeometry(QtCore.QRect(30, 430 , 351, groupboxY))
                self.btnNuevo.setGeometry(QtCore.QRect(230, botonY , 99, 23))

    def guardarSalir(self):

        controlador.dominio.alto = np.int32(self.txtAlto.text())
        controlador.dominio.ancho = np.int32(self.txtAncho.text())
        controlador.dominio.a = np.int32(self.txtA.text())
        controlador.dominio.b = np.int32(self.txtB.text())
        controlador.dominio.c = np.int32(self.txtC.text())

        lista=[]

        for n in range(0,len(controlador.metodo.listaParametros)):

            ejec='lista.append(float(self.txtParam'+ str(n) +'.text()))'
            exec(ejec)

        ##Como prueba se elijio el metodo Theis de una, esto ya asocia el metodo al dominio
        controlador.metodo.setearValores(lista)

#        print str(self.txtCoefAlmacenamiento.text())
        #param1 = parametros.parametros('primerParametro',self.txtParametro1.text(),'pihas')
        #param2 = parametros.parametros('segundoParametro',self.txtParametro2.text(),'pihas')
        ##  controlador.metodoSolucion.listaParametros.insert(1,param1)
        ## controlador.metodoSolucion.listaParametros.insert(2,param2)
        ventana.close()

    def cambioTipo(self, tipo):

        self.cmbMetodo.clear()

        if tipo == 'Numerico':

            metodos = ['DiferenciaFinita']
            self.btnCondicionesExternas.setEnabled(True)

        else:

            metodos = ['Theis', 'Hantush']
            self.btnCondicionesExternas.setEnabled(False)

        self.cmbMetodo.addItems(metodos)

    def retranslateUi(self, frmNuevoProyecto):

        pass

if __name__ == "__main__":

    import sys
    app = QtGui.QApplication(sys.argv)
    frmNuevoProyecto = QtGui.QWidget()
    ui = Ui_frmNuevoProyecto()
    ui.setupUi(frmNuevoProyecto)
    frmNuevoProyecto.show()
    sys.exit(app.exec_())
