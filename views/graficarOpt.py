# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graficarOpt.ui'
#
# Created: Tue Jan 31 16:24:14 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_graficarOpt(object):
    def setupUi(self, graficarOpt):
        graficarOpt.setObjectName(_fromUtf8("graficarOpt"))
        graficarOpt.resize(373, 131)
        graficarOpt.setWindowTitle(QtGui.QApplication.translate("graficarOpt", "Graficar Optimizaciones", None, QtGui.QApplication.UnicodeUTF8))
        self.label = QtGui.QLabel(graficarOpt)
        self.label.setGeometry(QtCore.QRect(40, 10, 131, 41))
        self.label.setText(QtGui.QApplication.translate("graficarOpt", "Pozo de observación:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.grafParametros = QtGui.QPushButton(graficarOpt)
        self.grafParametros.setGeometry(QtCore.QRect(40, 70, 131, 31))
        self.grafParametros.setText(QtGui.QApplication.translate("graficarOpt", "Grafica de Parametros", None, QtGui.QApplication.UnicodeUTF8))
        self.grafParametros.setObjectName(_fromUtf8("grafParametros"))
        self.grafObservaciones = QtGui.QPushButton(graficarOpt)
        self.grafObservaciones.setGeometry(QtCore.QRect(200, 70, 131, 31))
        self.grafObservaciones.setText(QtGui.QApplication.translate("graficarOpt", "Graficar observaciones", None, QtGui.QApplication.UnicodeUTF8))
        self.grafObservaciones.setObjectName(_fromUtf8("grafObservaciones"))
        self.pozo = QtGui.QComboBox(graficarOpt)
        self.pozo.setGeometry(QtCore.QRect(200, 20, 131, 21))
        self.pozo.setObjectName(_fromUtf8("pozo"))

        self.retranslateUi(graficarOpt)
        QtCore.QMetaObject.connectSlotsByName(graficarOpt)

    def retranslateUi(self, graficarOpt):
        pass

