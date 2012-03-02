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
# Form implementation generated from reading ui file 'ingresarCaudal.ui'
#
# Created: Wed Dec 14 21:03:09 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import observacion
import observacionesensayo
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(QtGui.QDialog):
    def setupUi(self, Dialog, cont):
        global ContEnsayo
        ContEnsayo=cont
        self.observaciones=[]
        
        Dialog.setObjectName(_fromUtf8("ingresarobservacionesensayo"))
        Dialog.resize(375, 214)
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Ingresar Observaciones Ensayo", None, QtGui.QApplication.UnicodeUTF8))
        self.txttiempo = QtGui.QTextEdit(Dialog)
        self.txttiempo.setGeometry(QtCore.QRect(170, 40, 101, 31))
        self.txttiempo.setObjectName(_fromUtf8("txttiempo"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 50, 46, 21))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Tiempo", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 100, 46, 13))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Nivel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtcaudal = QtGui.QTextEdit(Dialog)
        self.txtcaudal.setGeometry(QtCore.QRect(170, 90, 101, 31))
        self.txtcaudal.setObjectName(_fromUtf8("txtcaudal"))
        self.btnagregar = QtGui.QPushButton(Dialog)
        self.btnagregar.setGeometry(QtCore.QRect(100, 150, 71, 23))
        self.btnagregar.setText(QtGui.QApplication.translate("Dialog", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnagregar.setObjectName(_fromUtf8("btnagregar"))
        self.btnfinalizar = QtGui.QPushButton(Dialog)
        self.btnfinalizar.setGeometry(QtCore.QRect(200, 150, 71, 23))
        self.btnfinalizar.setText(QtGui.QApplication.translate("Dialog", "Finalizar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnfinalizar.setObjectName(_fromUtf8("btnfinalizar"))
        self.dialogo=Dialog

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.btnagregar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.agregar)
        QtCore.QObject.connect(self.btnfinalizar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.finalizar)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        pass

    def agregar(self):
        global ContEnsayo
        control=True
        
        t=float(self.txttiempo.toPlainText())
        print "tiempo: "+str(t)
##      Se verifica que vengas los datos con sus tiempos ordenados de manera creciente sino salta         
        control=ContEnsayo.verificarFormato(self.observaciones, t)

        if (control==False):
            reply = QtGui.QMessageBox.critical(self,
                "Error",
                "Los datos de bombeo no fueron agregaos. Debe ingresar un valor para el tiempo mayor a los ingresados anteriormente.")
            
        else:  
            n=float(self.txtcaudal.toPlainText())        
            print "caudal: "+str(n)
            o=observacion.observacion(t,n)
            self.observaciones.append(o)

            reply = QtGui.QMessageBox.information(None,
                    "Información",
                    "Se agrego la nueva observacion del ensayo. Presione finalizar para guardar las observaciones")

            self.txttiempo.setText('')
            self.txtcaudal.setText('')        
        

    def finalizar(self):
        global ContEnsayo

        ####Pedir un nombre para el ensayo
        nombre, ok=QtGui.QInputDialog.getText(self,"Finalzar registro ",
                                   "Nombre: ", QtGui.QLineEdit.Normal)  
        
##      Se manda al controlador las observaciones y se retorna el id de las observaciones                           
        obse=ContEnsayo.agregarObservacion(self.observaciones, nombre)        
       
        reply = QtGui.QMessageBox.information(self,
                "Información",
                "Se ha creado un nuevo conjunto de observaciones en el sistema. El id es: "+ str(obse.id))

        if reply == QtGui.QMessageBox.Ok:
            print "OK"
            self.dialogo.close()            
        else:
            print "Escape"
        

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    frmImpProyecto = QtGui.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(frmImpProyecto)
    frmImpProyecto.show()
    sys.exit(app.exec_())
