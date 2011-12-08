# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogo.ui'
#
# Created: Thu Dec 08 19:14:05 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(QtGui.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Importar Caudal Bombeado"))
        Dialog.resize(572, 130)
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 30, 46, 13))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Archivito", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(113, 20, 331, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(460, 20, 75, 23))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Explorar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.aceptar = QtGui.QPushButton(Dialog)
        self.aceptar.setGeometry(QtCore.QRect(200, 70, 75, 23))
        self.aceptar.setText(QtGui.QApplication.translate("Dialog", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.aceptar.setObjectName(_fromUtf8("aceptar"))
        self.cancelar = QtGui.QPushButton(Dialog)
        self.cancelar.setGeometry(QtCore.QRect(290, 70, 75, 23))
        self.cancelar.setText(QtGui.QApplication.translate("Dialog", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelar.setObjectName(_fromUtf8("cancelar"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.browse)
        QtCore.QObject.connect(self.aceptar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.accionaceptar)
        QtCore.QObject.connect(self.cancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.accioncancelar) 
        
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        pass

    def browse(self):
        print "navegar"
        self.archivo = QtGui.QFileDialog.getOpenFileName(
                         self,
                         "SElegir un archivo para abrir",
                         "C:\wamp\www\prueba",
                         "Images (*.txt)");        
        print self.archivo
        self.textEdit.setText(self.archivo)        

    def accionaceptar(self):
        print "aceptar"
        f=open(self.archivo)
        contenido=f.read()
        print contenido        

    def accioncancelar(self):
        print "chau"
        
  

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    frmImpProyecto = QtGui.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(frmImpProyecto)
    frmImpProyecto.show()
    sys.exit(app.exec_())


