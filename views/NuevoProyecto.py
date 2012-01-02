# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NuevoProyecto.ui'
#
# Created: Sat Dec 17 18:07:26 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import condicionExterna
import metodoSolucion
import parametros
from theis import Theis
import CondicionesExternas
import numpy as np

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_frmNuevoProyecto(object):
    def setupUi(self, frmNuevoProyecto,controlo):
        global controlador
        controlador = controlo

        global ventana
        ventana = frmNuevoProyecto
        frmNuevoProyecto.setObjectName(_fromUtf8("frmNuevoProyecto"))
        frmNuevoProyecto.resize(427, 568)
        frmNuevoProyecto.setWindowTitle(QtGui.QApplication.translate("frmNuevoProyecto", "Crear un nuevo proyecto", None, QtGui.QApplication.UnicodeUTF8))
        self.btnNuevo = QtGui.QPushButton(frmNuevoProyecto)
        self.btnNuevo.setGeometry(QtCore.QRect(240, 530, 99, 23))
        self.btnNuevo.setText(QtGui.QApplication.translate("frmNuevoProyecto", "Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.btnNuevo.setObjectName(_fromUtf8("btnNuevo"))
        self.gbDimensionesDominio = QtGui.QGroupBox(frmNuevoProyecto)
        self.gbDimensionesDominio.setGeometry(QtCore.QRect(30, 10, 361, 121))
        self.gbDimensionesDominio.setTitle(QtGui.QApplication.translate("frmNuevoProyecto", "Dimensiones del dominio", None, QtGui.QApplication.UnicodeUTF8))
        self.gbDimensionesDominio.setObjectName(_fromUtf8("gbDimensionesDominio"))
        self.txtAlto = QtGui.QLineEdit(self.gbDimensionesDominio)
        self.txtAlto.setGeometry(QtCore.QRect(200, 40, 113, 28))
        self.txtAlto.setObjectName(_fromUtf8("txtAlto"))
        self.txtAncho = QtGui.QLineEdit(self.gbDimensionesDominio)
        self.txtAncho.setGeometry(QtCore.QRect(200, 80, 113, 28))
        self.txtAncho.setObjectName(_fromUtf8("txtAncho"))
        self.lblAlto = QtGui.QLabel(self.gbDimensionesDominio)
        self.lblAlto.setGeometry(QtCore.QRect(80, 40, 70, 18))
        self.lblAlto.setText(QtGui.QApplication.translate("frmNuevoProyecto", "Alto", None, QtGui.QApplication.UnicodeUTF8))
        self.lblAlto.setObjectName(_fromUtf8("lblAlto"))
        self.lblAncho = QtGui.QLabel(self.gbDimensionesDominio)
        self.lblAncho.setGeometry(QtCore.QRect(70, 80, 70, 18))
        self.lblAncho.setText(QtGui.QApplication.translate("frmNuevoProyecto", "Ancho", None, QtGui.QApplication.UnicodeUTF8))
        self.lblAncho.setObjectName(_fromUtf8("lblAncho"))
        self.gbParametrosDominio = QtGui.QGroupBox(frmNuevoProyecto)
        self.gbParametrosDominio.setGeometry(QtCore.QRect(30, 140, 361, 121))
        self.gbParametrosDominio.setTitle(QtGui.QApplication.translate("frmNuevoProyecto", "Parametros del dominio", None, QtGui.QApplication.UnicodeUTF8))
        self.gbParametrosDominio.setObjectName(_fromUtf8("gbParametrosDominio"))
        self.TransitividlineEdit_2txtad = QtGui.QLineEdit(self.gbParametrosDominio)
        self.TransitividlineEdit_2txtad.setGeometry(QtCore.QRect(200, 40, 113, 28))
        self.TransitividlineEdit_2txtad.setObjectName(_fromUtf8("TransitividlineEdit_2txtad"))
        self.txtCoefAlmacenamiento = QtGui.QLineEdit(self.gbParametrosDominio)
        self.txtCoefAlmacenamiento.setGeometry(QtCore.QRect(200, 80, 113, 28))
        self.txtCoefAlmacenamiento.setObjectName(_fromUtf8("txtCoefAlmacenamiento"))
        self.lblTransitividad = QtGui.QLabel(self.gbParametrosDominio)
        self.lblTransitividad.setGeometry(QtCore.QRect(40, 40, 101, 18))
        self.lblTransitividad.setText(QtGui.QApplication.translate("frmNuevoProyecto", "Transitividad", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTransitividad.setObjectName(_fromUtf8("lblTransitividad"))
        self.lblCoefAlmacenamiento = QtGui.QLabel(self.gbParametrosDominio)
        self.lblCoefAlmacenamiento.setGeometry(QtCore.QRect(10, 80, 171, 18))
        self.lblCoefAlmacenamiento.setText(QtGui.QApplication.translate("frmNuevoProyecto", "Coef. almacenamiento", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCoefAlmacenamiento.setObjectName(_fromUtf8("lblCoefAlmacenamiento"))
        self.gbMetodo = QtGui.QGroupBox(frmNuevoProyecto)
        self.gbMetodo.setGeometry(QtCore.QRect(30, 280, 361, 241))
        self.gbMetodo.setTitle(QtGui.QApplication.translate("frmNuevoProyecto", "Metodos de solucion", None, QtGui.QApplication.UnicodeUTF8))
        self.gbMetodo.setObjectName(_fromUtf8("gbMetodo"))
        self.txtParametro1 = QtGui.QLineEdit(self.gbMetodo)
        self.txtParametro1.setGeometry(QtCore.QRect(200, 120, 113, 28))
        self.txtParametro1.setObjectName(_fromUtf8("txtParametro1"))
        self.txtParametro2 = QtGui.QLineEdit(self.gbMetodo)
        self.txtParametro2.setGeometry(QtCore.QRect(202, 160, 111, 28))
        self.txtParametro2.setObjectName(_fromUtf8("txtParametro2"))
        self.cmbMetodo = QtGui.QComboBox(self.gbMetodo)
        self.cmbMetodo.setGeometry(QtCore.QRect(200, 80, 111, 28))
        self.cmbMetodo.setObjectName(_fromUtf8("cmbMetodo"))        

        self.lblTipo = QtGui.QLabel(self.gbMetodo)
        self.lblTipo.setGeometry(QtCore.QRect(60, 40, 70, 18))
        self.lblTipo.setText(QtGui.QApplication.translate("frmNuevoProyecto", "Tipo", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTipo.setObjectName(_fromUtf8("lblTipo"))
        self.lblMetodo = QtGui.QLabel(self.gbMetodo)
        self.lblMetodo.setGeometry(QtCore.QRect(50, 80, 70, 18))
        self.lblMetodo.setText(QtGui.QApplication.translate("frmNuevoProyecto", "Metodo", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMetodo.setObjectName(_fromUtf8("lblMetodo"))
        self.lblParametro1 = QtGui.QLabel(self.gbMetodo)
        self.lblParametro1.setGeometry(QtCore.QRect(40, 120, 101, 18))
        self.lblParametro1.setText(QtGui.QApplication.translate("frmNuevoProyecto", "Parametro", None, QtGui.QApplication.UnicodeUTF8))
        self.lblParametro1.setObjectName(_fromUtf8("lblParametro1"))
        self.lblParametro2 = QtGui.QLabel(self.gbMetodo)
        self.lblParametro2.setGeometry(QtCore.QRect(40, 160, 91, 18))
        self.lblParametro2.setText(QtGui.QApplication.translate("frmNuevoProyecto", "Parametro", None, QtGui.QApplication.UnicodeUTF8))
        self.lblParametro2.setObjectName(_fromUtf8("lblParametro2"))
        self.btnCondicionesExternas = QtGui.QPushButton(self.gbMetodo)
        self.btnCondicionesExternas.setGeometry(QtCore.QRect(10, 200, 181, 27))
        self.btnCondicionesExternas.setText(QtGui.QApplication.translate("frmNuevoProyecto", "Condiciones Externas", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCondicionesExternas.setObjectName(_fromUtf8("btnCondicionesExternas"))
        self.cmbTipo = QtGui.QComboBox(self.gbMetodo)
        self.cmbTipo.setGeometry(QtCore.QRect(200, 40, 111, 28))
        self.cmbTipo.setObjectName(_fromUtf8("cmbTipo"))
        tipos = ['Numerico','Analitico']
        self.cmbTipo.addItems(tipos)
        self.cambioTipo(self.cmbTipo.currentText())

        self.retranslateUi(frmNuevoProyecto)
        QtCore.QObject.connect(self.btnNuevo, QtCore.SIGNAL(_fromUtf8("clicked()")), self.guardarSalir)
        QtCore.QObject.connect(self.cmbTipo, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.cambioTipo)
        QtCore.QObject.connect(self.btnCondicionesExternas, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ventanaCondicionesExternas)
        QtCore.QMetaObject.connectSlotsByName(frmNuevoProyecto)

    def ventanaCondicionesExternas(self):
        frmCondicionesExternas = QtGui.QDialog()
        ui = CondicionesExternas.Ui_frmCondicionesExternas()
        ui.setupUi(frmCondicionesExternas,controlador)
        frmCondicionesExternas.exec_()

    def guardarSalir(self):

        controlador.dominio.alto = np.int32(self.txtAlto.text())
        controlador.dominio.ancho = np.int32(self.txtAncho.text())
        #controlador.metodoSolucion = metodoSolucion.metodoNumerico(controlador.dominio)
        ## Como prueba se elijio el metodo Theis de una, esto ya asocia el metodo al dominio
        metodo=Theis(controlador.dominio, controlador.parametros)                
        metodo.setearValores([float(self.TransitividlineEdit_2txtad.text()),float(self.txtCoefAlmacenamiento.text())])
        
        param1 = parametros.parametros('primerParametro',self.txtParametro1.text(),'pihas')
        param2 = parametros.parametros('segundoParametro',self.txtParametro2.text(),'pihas')
        ##  controlador.metodoSolucion.listaParametros.insert(1,param1)
        ## controlador.metodoSolucion.listaParametros.insert(2,param2)
        ventana.close()
	

    def cambioTipo(self, tipo):
        self.cmbMetodo.clear()

        if tipo == 'Numerico':
            metodos = ['Hay uno']
            self.btnCondicionesExternas.setEnabled(True)
        else:
            metodos = ['Ninguno']
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

