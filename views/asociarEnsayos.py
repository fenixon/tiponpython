# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asociarEnsayos.ui'
#
# Created: Mon Dec 26 19:39:44 2011
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog, idpozo, cont):

        print idpozo
        
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(638, 252)
        self.listWidget = QtGui.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(30, 20, 181, 211))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidget_2 = QtGui.QListWidget(Dialog)
        self.listWidget_2.setGeometry(QtCore.QRect(230, 20, 181, 211))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(430, 20, 181, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 50, 181, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.listWidget_3 = QtGui.QListWidget(Dialog)
        self.listWidget_3.setGeometry(QtCore.QRect(430, 80, 181, 121))
        self.listWidget_3.setObjectName(_fromUtf8("listWidget_3"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 210, 91, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(530, 210, 81, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Asociar observacion", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Dialog", "Asociar ensayo de bombeo", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Dialog", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("Dialog", "Agregar", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    frmasociarensayos = QtGui.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(frmasociarensayos)
    frmasociarensayos.show()
    sys.exit(app.exec_())        

