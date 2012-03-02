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
# Form implementation generated from reading ui file 'verensayos.ui'
#
# Created: Wed Dec 14 15:17:33 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(576, 276)
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Ver ensayos", None, QtGui.QApplication.UnicodeUTF8))
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(20, 40, 256, 192))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.tableView_2 = QtGui.QTableView(Dialog)
        self.tableView_2.setGeometry(QtCore.QRect(300, 40, 256, 192))
        self.tableView_2.setObjectName(_fromUtf8("tableView_2"))

        model = QtCore.QAbstractListModel([4,5,6])
        self.tableView.setModel(model)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.tableView, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), quit)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        pass


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    frmVerBombeo = QtGui.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(frmVerBombeo)
    frmVerBombeo.show()
    sys.exit(app.exec_())
