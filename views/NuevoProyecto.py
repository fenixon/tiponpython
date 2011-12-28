# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NuevoProyecto.ui'
#
# Created: Fri Nov 11 15:27:53 2011
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import Proyecto

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_frmNuevoProyecto(object):
    def setupUi(self, frmNuevoProyecto):

        #Indicamos que el dialogo va a ser eliminado en la salida
        #frmNuevoProyecto.setAttribute(QtCore.Qt.WA_DeleteOnClose, on = True)

        
        frmNuevoProyecto.setObjectName(_fromUtf8("frmNuevoProyecto"))
        frmNuevoProyecto.resize(366, 193)
        frmNuevoProyecto.setWindowTitle(QtGui.QApplication.translate("frmNuevoProyecto", "Crear un nuevo proyecto", None, QtGui.QApplication.UnicodeUTF8))
                
        self.btnNuevo = QtGui.QPushButton(frmNuevoProyecto)
        self.btnNuevo.setGeometry(QtCore.QRect(240, 150, 99, 23))
        self.btnNuevo.setText(QtGui.QApplication.translate("frmNuevoProyecto", "Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.btnNuevo.setObjectName(_fromUtf8("btnNuevo"))
        
        self.btnCancelar = QtGui.QPushButton(frmNuevoProyecto)
        self.btnCancelar.setGeometry(QtCore.QRect(120, 150, 99, 23))
        self.btnCancelar.setText(QtGui.QApplication.translate("frmNuevoProyecto", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        
        self.cmbMetodoSolucion = QtGui.QComboBox(frmNuevoProyecto)
        self.cmbMetodoSolucion.setGeometry(QtCore.QRect(120, 10, 221, 23))
        self.cmbMetodoSolucion.setAutoFillBackground(False)
        self.cmbMetodoSolucion.setStyleSheet(_fromUtf8(""))
        self.cmbMetodoSolucion.setEditable(True)
        self.cmbMetodoSolucion.setObjectName(_fromUtf8("cmbMetodoSolucion"))
        
        metodos = ['Metodito Primero', 'Metodito Segundo', 'Metodito Tercero']
        self.cmbMetodoSolucion.addItems(metodos)
                
        self.txtParam1 = QtGui.QLineEdit(frmNuevoProyecto)
        self.txtParam1.setGeometry(QtCore.QRect(120, 50, 113, 22))
        self.txtParam1.setText(QtGui.QApplication.translate("frmNuevoProyecto", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.txtParam1.setObjectName(_fromUtf8("txtParam1"))
        
        self.txtParam2 = QtGui.QLineEdit(frmNuevoProyecto)
        self.txtParam2.setGeometry(QtCore.QRect(120, 100, 113, 22))
        self.txtParam2.setText(QtGui.QApplication.translate("frmNuevoProyecto", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.txtParam2.setObjectName(_fromUtf8("txtParam2"))
        self.retranslateUi(frmNuevoProyecto)
                
        QtCore.QObject.connect(self.btnNuevo, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Nuevo)
                
        QtCore.QObject.connect(self.btnCancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), frmNuevoProyecto.close)
		
        #Conectamos la señal de clickeo de nuevo, con la señal de clickeo de cancelar
        QtCore.QObject.connect(self.btnNuevo, QtCore.SIGNAL(_fromUtf8("clicked()")), self.btnCancelar, QtCore.SIGNAL(_fromUtf8("clicked()")))
 
                
        QtCore.QMetaObject.connectSlotsByName(frmNuevoProyecto)
        
    def Nuevo(self):
        nuevoMetodoSolucion = Proyecto.metodoSolucion(self.cmbMetodoSolucion.lineEdit().text(),self.txtParam1.text(),self.txtParam2.text())
        self.nuevoProyecto = Proyecto.Proyecto(nuevoMetodoSolucion)
        print self.nuevoProyecto.metodoSolucion.nombre
        print self.nuevoProyecto.metodoSolucion.param1
        print self.nuevoProyecto.metodoSolucion.param2
                

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

