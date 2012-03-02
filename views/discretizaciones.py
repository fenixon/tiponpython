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
# Form implementation generated from reading ui file 'discretizaciones.ui'
#
# Created: Tue Jan 31 10:23:13 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
sys.path.append("../models")
from controlador import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class ventanaDiscretizaciones(QtGui.QDialog):
    def setupUi(self, Dialog, cont):
        global ContEnsayo
        ContEnsayo=cont
        
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(372, 305)
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Ingreso de valores para discretizaciones", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 351, 121))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Discretizacion Espacial", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 30, 161, 16))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Número de intervalos para x:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 171, 16))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Número de intervaloes para y:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txt_nix = QtGui.QLineEdit(self.groupBox)
        self.txt_nix.setGeometry(QtCore.QRect(210, 30, 113, 20))
        self.txt_nix.setObjectName(_fromUtf8("txt_nix"))
        self.txt_niy = QtGui.QLineEdit(self.groupBox)
        self.txt_niy.setGeometry(QtCore.QRect(210, 60, 113, 20))
        self.txt_niy.setObjectName(_fromUtf8("txt_niy"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(30, 90, 201, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        
        
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(210, 90, 111, 21))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setEnabled(False)
        if cont.metodo.gettipo()=="numerico":
            self.comboBox.setEnabled(True)
        
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 140, 351, 121))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "Discretizacion Temporal", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(30, 30, 141, 16))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Tiempo inicial de simulación:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(30, 60, 141, 16))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Tiempo final de simulación:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.txt_ti = QtGui.QLineEdit(self.groupBox_2)
        self.txt_ti.setGeometry(QtCore.QRect(210, 30, 113, 20))
        self.txt_ti.setObjectName(_fromUtf8("txt_ti"))
        self.txt_tf = QtGui.QLineEdit(self.groupBox_2)
        self.txt_tf.setGeometry(QtCore.QRect(210, 60, 113, 20))
        self.txt_tf.setObjectName(_fromUtf8("txt_tf"))
        self.txt_nit = QtGui.QLineEdit(self.groupBox_2)
        self.txt_nit.setGeometry(QtCore.QRect(210, 90, 113, 20))
        self.txt_nit.setObjectName(_fromUtf8("txt_nit"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(30, 80, 171, 31))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Número de intervaloes de tiempo:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
##        self.label_6 = QtGui.QLabel(self.groupBox_2)
##        self.label_6.setGeometry(QtCore.QRect(30, 120, 201, 16))
##        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Tiempo final para observaciones:", None, QtGui.QApplication.UnicodeUTF8))
##        self.label_6.setObjectName(_fromUtf8("label_6"))
##        self.txt_tfo = QtGui.QLineEdit(self.groupBox_2)
##        self.txt_tfo.setGeometry(QtCore.QRect(210, 120, 113, 20))
##        self.txt_tfo.setObjectName(_fromUtf8("txt_tfo"))
        self.btn_Aceptar = QtGui.QPushButton(Dialog)
        self.btn_Aceptar.setGeometry(QtCore.QRect(10, 270, 75, 23))
        self.btn_Aceptar.setText(QtGui.QApplication.translate("Dialog", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Aceptar.setObjectName(_fromUtf8("btn_Aceptar"))
        self.btn_Cancelar = QtGui.QPushButton(Dialog)
        self.btn_Cancelar.setGeometry(QtCore.QRect(290, 270, 75, 23))
        self.btn_Cancelar.setText(QtGui.QApplication.translate("Dialog", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cancelar.setObjectName(_fromUtf8("btn_Cancelar"))
        self.dialogo=Dialog

        self.txt_nix.setText("6")
        self.txt_niy.setText("6")
        self.txt_ti.setText("0")
        self.txt_tf.setText("0.18")
        self.txt_nit.setText("10")


        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.btn_Aceptar, QtCore.SIGNAL("clicked()"), self.accionAceptar)
        QtCore.QObject.connect(self.btn_Cancelar, QtCore.SIGNAL("clicked()"), Dialog.close)
        
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "Ingrese el tipo de discretización:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Dialog", "Lineal", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemData(0,"Lineal")
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Dialog", "Logarítmica", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemData(1,"Logaritmica")
        self.comboBox.setCurrentIndex(1)
          

    def accionAceptar(self):
        nix=int(self.txt_nix.text())
        niy=int(self.txt_niy.text())

        ti=float(self.txt_ti.text())
        tf=float(self.txt_tf.text())
        nit=int(self.txt_nit.text())


        print "current ",self.comboBox.currentIndex()
        print "itemdata ", self.comboBox.itemData(self.comboBox.currentIndex())
        print "topyobjetct ", self.comboBox.itemData(self.comboBox.currentIndex()).toPyObject()

        

        if ContEnsayo.metodo.gettipo()=="numerico":
            tipo=self.comboBox.itemData(self.comboBox.currentIndex()).toPyObject().__str__()
        else:
            tipo=None
        
        tfo=10000

        print ti
        print 'tf '+ str(tf)
        print 'nit '+str(nit)

        print "Tipo ", tipo
        
##        tfo=self.txt_tfo.text()

        ContEnsayo.setearValoresDiscretizaciones(nix, niy, ti, tf, nit, tfo, tipo)

        if nix < 0 or niy < 0 or nit < 0  :
            QtGui.QMessageBox.critical(self,
                            "Error",
                            "El numero de intervalos debe ser un valor entero positivo mayor a 0 ")
        else:

            if ti>tf or ti>tfo:
                QtGui.QMessageBox.critical(self,
                                "Error",
                                "El tiempo inicial no debe superar a los tiempos finales. Corrija estos valores ")
            else:
                self.dialogo.close()



if __name__ == "__main__":
    
    p=controlador.Proyecto()
    app = QtGui.QApplication(sys.argv)
    frmImpProyecto = QtGui.QWidget()
    ui = ventanaDiscretizaciones()
    ui.setupUi(frmImpProyecto,p)
    frmImpProyecto.show()
    sys.exit(app.exec_())    


                
