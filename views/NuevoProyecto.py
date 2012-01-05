# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NuevoProyecto.ui'
#
# Created: Tue Jan  3 19:43:04 2012
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

        def focusInEvent(self, evento):
            self.setStyleSheet("background-color:  rgb(40, 255, 40)")
            evento.gotFocus()
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

        frmNuevoProyecto.setObjectName(_fromUtf8("frmNuevoProyecto"))
        frmNuevoProyecto.resize(405, 608)
        frmNuevoProyecto.setWindowTitle(QtGui.QApplication.translate("frmNuevoProyecto", "Crear un nuevo proyecto", None, QtGui.QApplication.UnicodeUTF8))
        self.btnNuevo = QtGui.QPushButton(frmNuevoProyecto)
        self.btnNuevo.setGeometry(QtCore.QRect(240, 570, 99, 23))
        self.btnNuevo.setText(QtGui.QApplication.translate("frmNuevoProyecto", "Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.btnNuevo.setObjectName(_fromUtf8("btnNuevo"))
        self.gbDimensionesDominio = QtGui.QGroupBox(frmNuevoProyecto)
        self.gbDimensionesDominio.setGeometry(QtCore.QRect(30, 10, 351, 251))
        self.gbDimensionesDominio.setTitle(QtGui.QApplication.translate("frmNuevoProyecto", "Dimensiones del dominio", None, QtGui.QApplication.UnicodeUTF8))
        self.gbDimensionesDominio.setObjectName(_fromUtf8("gbDimensionesDominio"))
        self.txtAlto = cajaTexto(self.gbDimensionesDominio)
        self.txtAlto.setGeometry(QtCore.QRect(200, 40, 113, 28))
        self.txtAlto.setObjectName(_fromUtf8("txtAlto"))
        self.txtAncho = cajaTexto(self.gbDimensionesDominio)
        self.txtAncho.setGeometry(QtCore.QRect(200, 80, 113, 28))
        self.txtAncho.setObjectName(_fromUtf8("txtAncho"))
        self.lblAlto = QtGui.QLabel(self.gbDimensionesDominio)
        self.lblAlto.setGeometry(QtCore.QRect(80, 50, 70, 18))
        self.lblAlto.setText(QtGui.QApplication.translate("frmNuevoProyecto", "Alto", None, QtGui.QApplication.UnicodeUTF8))
        self.lblAlto.setObjectName(_fromUtf8("lblAlto"))
        self.lblAncho = QtGui.QLabel(self.gbDimensionesDominio)
        self.lblAncho.setGeometry(QtCore.QRect(70, 90, 51, 18))
        self.lblAncho.setText(QtGui.QApplication.translate("frmNuevoProyecto", "Ancho", None, QtGui.QApplication.UnicodeUTF8))
        self.lblAncho.setObjectName(_fromUtf8("lblAncho"))
        self.txtA = cajaTexto(self.gbDimensionesDominio)
        self.txtA.setGeometry(QtCore.QRect(200, 120, 113, 28))
        self.txtA.setObjectName(_fromUtf8("txtA"))
        self.txtB = cajaTexto(self.gbDimensionesDominio)
        self.txtB.setGeometry(QtCore.QRect(200, 160, 113, 28))
        self.txtB.setObjectName(_fromUtf8("txtB"))
        self.txtC = cajaTexto(self.gbDimensionesDominio)
        self.txtC.setGeometry(QtCore.QRect(200, 200, 113, 28))
        self.txtC.setObjectName(_fromUtf8("txtC"))
        self.lblA = QtGui.QLabel(self.gbDimensionesDominio)
        self.lblA.setGeometry(QtCore.QRect(90, 130, 70, 18))
        self.lblA.setText(QtGui.QApplication.translate("frmNuevoProyecto", "a", None, QtGui.QApplication.UnicodeUTF8))
        self.lblA.setObjectName(_fromUtf8("lblA"))
        self.lblB = QtGui.QLabel(self.gbDimensionesDominio)
        self.lblB.setGeometry(QtCore.QRect(90, 170, 70, 18))
        self.lblB.setText(QtGui.QApplication.translate("frmNuevoProyecto", "b", None, QtGui.QApplication.UnicodeUTF8))
        self.lblB.setObjectName(_fromUtf8("lblB"))
        self.lblC = QtGui.QLabel(self.gbDimensionesDominio)
        self.lblC.setGeometry(QtCore.QRect(90, 210, 70, 18))
        self.lblC.setText(QtGui.QApplication.translate("frmNuevoProyecto", "c", None, QtGui.QApplication.UnicodeUTF8))
        self.lblC.setObjectName(_fromUtf8("lblC"))
        self.gbParametrosDominio = QtGui.QGroupBox(frmNuevoProyecto)
        self.gbParametrosDominio.setGeometry(QtCore.QRect(30, 270, 351, 121))
        self.gbParametrosDominio.setTitle(QtGui.QApplication.translate("frmNuevoProyecto", "Parametros del dominio", None, QtGui.QApplication.UnicodeUTF8))
        self.gbParametrosDominio.setObjectName(_fromUtf8("gbParametrosDominio"))
        self.txtTransitividad = cajaTexto(self.gbParametrosDominio)
        self.txtTransitividad.setGeometry(QtCore.QRect(200, 40, 113, 28))
        self.txtTransitividad.setObjectName(_fromUtf8("txtTransitividad"))
        self.txtCoefAlmacenamiento = cajaTexto(self.gbParametrosDominio)
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
        self.gbMetodo.setGeometry(QtCore.QRect(30, 400, 351, 161))
        self.gbMetodo.setTitle(QtGui.QApplication.translate("frmNuevoProyecto", "Metodos de solucion", None, QtGui.QApplication.UnicodeUTF8))
        self.gbMetodo.setObjectName(_fromUtf8("gbMetodo"))
        self.lblTipo = QtGui.QLabel(self.gbMetodo)
        self.lblTipo.setGeometry(QtCore.QRect(60, 40, 70, 18))
        self.lblTipo.setText(QtGui.QApplication.translate("frmNuevoProyecto", "Tipo", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTipo.setObjectName(_fromUtf8("lblTipo"))
        self.lblMetodo = QtGui.QLabel(self.gbMetodo)
        self.lblMetodo.setGeometry(QtCore.QRect(50, 80, 70, 18))
        self.lblMetodo.setText(QtGui.QApplication.translate("frmNuevoProyecto", "Metodo", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMetodo.setObjectName(_fromUtf8("lblMetodo"))
        self.btnCondicionesExternas = QtGui.QPushButton(self.gbMetodo)
        self.btnCondicionesExternas.setGeometry(QtCore.QRect(10, 120, 181, 27))
        self.btnCondicionesExternas.setText(QtGui.QApplication.translate("frmNuevoProyecto", "Condiciones Externas", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCondicionesExternas.setObjectName(_fromUtf8("btnCondicionesExternas"))
        self.cmbMetodo = QtGui.QComboBox(self.gbMetodo)
        self.cmbMetodo.setGeometry(QtCore.QRect(200, 80, 111, 28))
        self.cmbMetodo.setObjectName(_fromUtf8("cmbMetodo"))
        self.cmbTipo = QtGui.QComboBox(self.gbMetodo)
        self.cmbTipo.setGeometry(QtCore.QRect(200, 40, 111, 28))
        self.cmbTipo.setObjectName(_fromUtf8("cmbTipo"))

        tipos = ['Analitico']
        self.cmbTipo.addItems(tipos)
        self.cambioTipo(self.cmbTipo.currentText())
        self.validador = QtGui.QIntValidator(-100, 900, self.gbDimensionesDominio)
        self.txtAlto.setValidator(self.validador)
        self.txtAncho.setValidator(self.validador)
        self.txtA.setValidator(self.validador)
        self.txtB.setValidator(self.validador)
        self.txtC.setValidator(self.validador)
        self.txtCoefAlmacenamiento.setValidator(self.validador)
        self.txtTransitividad.setValidator(self.validador)


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
        controlador.dominio.a = np.int32(self.txtA.text())
        controlador.dominio.b = np.int32(self.txtB.text())
        controlador.dominio.c = np.int32(self.txtC.text())

        ##Como prueba se elijio el metodo Theis de una, esto ya asocia el metodo al dominio
        estring = 'metodo= %s(controlador.dominio, controlador.parametros)' % (self.cmbMetodo.currentText())
        exec(estring)
        metodo.setearValores([float(self.TransitividlineEdit_2txtad.text()),float(self.txtCoefAlmacenamiento.text())])
        controlador.metodo=metodo
        #param1 = parametros.parametros('primerParametro',self.txtParametro1.text(),'pihas')
        #param2 = parametros.parametros('segundoParametro',self.txtParametro2.text(),'pihas')
        ##  controlador.metodoSolucion.listaParametros.insert(1,param1)
        ## controlador.metodoSolucion.listaParametros.insert(2,param2)
        ventana.close()

    def cambioTipo(self, tipo):
        self.cmbMetodo.clear()
        if tipo == 'Numerico':
            metodos = ['Ninguno']
            self.btnCondicionesExternas.setEnabled(True)
        else:
            metodos = ['Theis']
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

