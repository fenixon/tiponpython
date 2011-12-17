# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'verensayos.ui'
#
# Created: Wed Dec 14 13:58:11 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import modelotabla
import observacion
import observacionesensayo
import controlador

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog, cont):
        global ContEnsayo
        ContEnsayo=cont        
        
        Dialog.setObjectName(_fromUtf8("verobservacionesensayo"))
        Dialog.resize(576, 276)
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Ver Observaciones del Ensayo", None, QtGui.QApplication.UnicodeUTF8))

## Se obtienen todas las observaciones de ensayo del controlador
        obss=ContEnsayo.observaciones
        
##      Se toma la primer observacion de ensayo
        obse=obss[0]
##      Se instancia un modelo tabla con las observaciones del ensayo y los nombres de los campos a mostrar(id)
        self.model=modelotabla.modelotabla(obss, obse.datosNombre())
        
        self.tablita= QtGui.QTableView(Dialog)
        self.tablita.setGeometry(QtCore.QRect(20, 40, 256, 192))
        self.tablita.setObjectName(_fromUtf8("tablita"))
        self.tablita.setModel(self.model)

        self.tablita2= QtGui.QTableView(Dialog)
        self.tablita2.setGeometry(QtCore.QRect(300, 40, 256, 192))
        self.tablita2.setObjectName(_fromUtf8("tablita2"))     

##      QtCore.QObject.connect(self.tablita, QtCore.SIGNAL(_fromUtf8("cellClicked()")), self.elegirensayo)
        QtCore.QObject.connect(self.tablita, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), self.elegirensayo)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def elegirensayo(self, item):
##      print self.model.data(item,QtCore.Qt.DisplayRole)
##      Se Llama al metodo objeto del modelotabla para retornar el ensayo original asociado
        obse=self.model.objeto(item)
        print "se elijio las observaciones del ensayo nro: "+str(obse.id)        
       
##      Se creo una instancia de una observacion para tomar los nombres de los atributos        
        aux=observacion.observacion(0,0)
##      Se instancia un modelo tabla con las observaciones del ensayo y los atributos a mostrar(tiempo, nivel piezo)
        model2=modelotabla.modelotabla(obse.devolverO(), aux.datosNombre())
##      Se setea el modelo en la tabla 2
        self.tablita2.setModel(model2)  

    def retranslateUi(self, Dialog):
        pass

    

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    frmVerBombeo = QtGui.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(frmVerBombeo)
    frmVerBombeo.show()
    sys.exit(app.exec_())
