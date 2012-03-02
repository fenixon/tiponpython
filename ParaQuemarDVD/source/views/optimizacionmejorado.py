"""
	tiponpython Simulacion de ensayos de acuiferos
	Copyright 2012 Jesus Guibert
	
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

from PyQt4 import QtCore, QtGui
import numpy as np
import sys
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
class optimizacion(QtGui.QWidget):
    def __init__(self,Form):
        QtGui.QWidget.__init__(self)
        self.setupUi()
            
    def setupUi(self):
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 20, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setText(QtGui.QApplication.translate("Form", "Problema Inverso - Optimizacion", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(200, 70, 91, 16))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Metodo a Utilizar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 158, 36))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Pozos Seleccionados", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line = QtGui.QFrame(self)
        self.line.setGeometry(QtCore.QRect(143, 70, 20, 211))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self)
        self.line_2.setGeometry(QtCore.QRect(30, 80, 261, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))        
        self.setObjectName(_fromUtf8("Form"))
        self.resize(374, 403)
        self.setWindowTitle(QtGui.QApplication.translate("Form", "Optimizacion", None, QtGui.QApplication.UnicodeUTF8))
        self.show()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    print "hola"
    frmopt=QtGui.QDialog()
    opt= optimizacion(frmopt)
    sys.exit(app.exec_())
