# -*- coding: utf-8 -*-
"""
	tiponpython Simulacion de ensayos de acuiferos
	Copyright 2012 Andres Pias
	
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
# Form implementation generated from reading ui file 'CondicionesExternas.ui'
#
# Created: Tue Dec 20 19:40:57 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from models.condicionExterna import condicionExterna

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


class Ui_frmCondicionesExternas(object):
    def setupUi(self, frmCondicionesExternas,controlo):
        self.listaCondicionesExternas = []
        global controlador
        controlador = controlo

        global ventana
        ventana = frmCondicionesExternas

        frmCondicionesExternas.setObjectName(_fromUtf8("frmCondicionesExternas"))
        frmCondicionesExternas.resize(437, 349)
        frmCondicionesExternas.setWindowTitle(QtGui.QApplication.translate("frmCondicionesExternas", "Condiciones Externas", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAgregar = QtGui.QPushButton(frmCondicionesExternas)
        self.btnAgregar.setGeometry(QtCore.QRect(20, 90, 111, 27))
        self.btnAgregar.setText(QtGui.QApplication.translate("frmCondicionesExternas", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAgregar.setObjectName(_fromUtf8("btnAgregar"))
        self.btnVolver = QtGui.QPushButton(frmCondicionesExternas)
        self.btnVolver.setGeometry(QtCore.QRect(20, 280, 111, 27))
        self.btnVolver.setText(QtGui.QApplication.translate("frmCondicionesExternas", "Volver", None, QtGui.QApplication.UnicodeUTF8))
        self.btnVolver.setObjectName(_fromUtf8("btnVolver"))
        self.txtValor = cajaTexto(frmCondicionesExternas)
        self.txtValor.setGeometry(QtCore.QRect(270, 20, 131, 28))
        self.txtValor.setObjectName(_fromUtf8("txtValor"))
        self.cmbTipo = QtGui.QComboBox(frmCondicionesExternas)
        self.cmbTipo.setGeometry(QtCore.QRect(70, 20, 111, 28))
        self.cmbTipo.setObjectName(_fromUtf8("cmbTipo"))
        tipos = ['Flujo','Nivel']
        self.cmbTipo.addItems(tipos)
        self.lblTipo = QtGui.QLabel(frmCondicionesExternas)
        self.lblTipo.setGeometry(QtCore.QRect(30, 30, 70, 18))
        self.lblTipo.setText(QtGui.QApplication.translate("frmCondicionesExternas", "Tipo", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTipo.setObjectName(_fromUtf8("lblTipo"))
        self.lblValor = QtGui.QLabel(frmCondicionesExternas)
        self.lblValor.setGeometry(QtCore.QRect(220, 30, 51, 18))
        self.lblValor.setText(QtGui.QApplication.translate("frmCondicionesExternas", "Valor", None, QtGui.QApplication.UnicodeUTF8))
        self.lblValor.setObjectName(_fromUtf8("lblValor"))
        self.btnQuitar = QtGui.QPushButton(frmCondicionesExternas)
        self.btnQuitar.setGeometry(QtCore.QRect(20, 140, 111, 27))
        self.btnQuitar.setText(QtGui.QApplication.translate("frmCondicionesExternas", "Quitar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnQuitar.setObjectName(_fromUtf8("btnQuitar"))
        self.lstFlujo = QtGui.QListView(frmCondicionesExternas)
        self.lstFlujo.setGeometry(QtCore.QRect(150, 80, 115, 230))
        self.lstFlujo.setObjectName(_fromUtf8("lstFlujo"))
        self.lstNivel = QtGui.QListView(frmCondicionesExternas)
        self.lstNivel.setGeometry(QtCore.QRect(285, 80, 115, 230))
        self.lstNivel.setObjectName(_fromUtf8("lstNivel"))

        self.retranslateUi(frmCondicionesExternas)
        QtCore.QObject.connect(self.btnAgregar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.agregar)
        QtCore.QObject.connect(self.btnVolver, QtCore.SIGNAL(_fromUtf8("clicked()")), self.guardarSalir)
        QtCore.QObject.connect(self.btnQuitar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.remover)
        QtCore.QObject.connect(self.lstFlujo, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), self.limpiarSeleccionNivel)
        QtCore.QObject.connect(self.lstNivel, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), self.limpiarSeleccionFlujo)
        QtCore.QMetaObject.connectSlotsByName(frmCondicionesExternas)

        #self.lstFlujo.clearSelection


        listaFlujo = []
        listaNivel = []
        for i in controlador.dominio.listaCondicionesExternas:
            if i.tipo == 'Flujo':
                listaFlujo.append(str(i.valor))
            else:
                listaNivel.append(str(i.valor))
        modelFlujo=QtGui.QStringListModel(listaFlujo)
        self.lstFlujo.setModel(modelFlujo)
        modelNivel=QtGui.QStringListModel(listaNivel)
        self.lstNivel.setModel(modelNivel)




    def limpiarSeleccionNivel(self,indice):
        self.ultimoSeleccionado = 'Flujo'
        self.lstNivel.clearSelection()

    def limpiarSeleccionFlujo(self,indice):
        self.ultimoSeleccionado = 'Nivel'
        self.lstFlujo.clearSelection()

    def remover(self):
        if self.ultimoSeleccionado == 'Flujo':
            self.lstFlujo.model().removeRow(self.lstFlujo.currentIndex().row())
        else:
            self.lstNivel.model().removeRow(self.lstFlujo.currentIndex().row())

        #print dir(self.lstFlujo)
    def agregar(self):
        if self.cmbTipo.currentText() == 'Flujo':
            listactual = self.lstFlujo.model().stringList()
            listactual.append(self.txtValor.text())
            self.lstFlujo.model().setStringList(listactual)
        else:
            listactual = self.lstNivel.model().stringList()
            listactual.append(self.txtValor.text())
            self.lstNivel.model().setStringList(listactual)


    def retranslateUi(self, frmCondicionesExternas):
        pass

    def guardarSalir(self):
        del controlador.dominio.listaCondicionesExternas[:]

        listafinal = self.lstFlujo.model().stringList()
        for i in listafinal:
            controlador.dominio.listaCondicionesExternas.append(condicionExterna('Flujo',int(str(i))))

        listafinal = self.lstNivel.model().stringList()
        for i in listafinal:
            controlador.dominio.listaCondicionesExternas.append(condicionExterna('Nivel',int(str(i))))

        ventana.close()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    frmCondicionesExternas = QtGui.QWidget()
    ui = Ui_frmCondicionesExternas()
    ui.setupUi(frmCondicionesExternas)
    frmCondicionesExternas.show()
    sys.exit(app.exec_())

