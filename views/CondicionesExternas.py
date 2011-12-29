# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CondicionesExternas.ui'
#
# Created: Tue Dec 20 19:40:57 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_frmCondicionesExternas(object):
    def setupUi(self, frmCondicionesExternas,controlo):
        self.listaCondicionesExternas = []
        global controlador
        controlador = controlo
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
        self.txtValor = QtGui.QLineEdit(frmCondicionesExternas)
        self.txtValor.setGeometry(QtCore.QRect(270, 20, 131, 28))
        self.txtValor.setObjectName(_fromUtf8("txtValor"))
        self.cmbTipo = QtGui.QComboBox(frmCondicionesExternas)
        self.cmbTipo.setGeometry(QtCore.QRect(70, 20, 111, 28))
        self.cmbTipo.setObjectName(_fromUtf8("cmbTipo"))
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
        self.listView = QtGui.QListView(frmCondicionesExternas)
        self.listView.setGeometry(QtCore.QRect(160, 80, 251, 241))
        self.listView.setObjectName(_fromUtf8("listView"))

        self.retranslateUi(frmCondicionesExternas)
        QtCore.QObject.connect(self.btnAgregar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.agregar)
        QtCore.QObject.connect(self.btnVolver, QtCore.SIGNAL(_fromUtf8("clicked()")), frmCondicionesExternas.close)
        QtCore.QMetaObject.connectSlotsByName(frmCondicionesExternas)

    def agregar(self):
        nueva = condicionExterna(self.cmbTipo.currentText(),self.txtValor.text())
        controlador.dominio.listaCondicionesExternas.insert(nueva)

    def retranslateUi(self, frmCondicionesExternas):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    frmCondicionesExternas = QtGui.QWidget()
    ui = Ui_frmCondicionesExternas()
    ui.setupUi(frmCondicionesExternas)
    frmCondicionesExternas.show()
    sys.exit(app.exec_())

