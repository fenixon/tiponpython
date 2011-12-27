# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asociarEnsayos.ui'
#
# Created: Mon Dec 26 19:39:44 2011
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import modelotabla
import controlador

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(QtGui.QDialog):
    def setupUi(self, Dialog, idpozo, cont):

        global ContEnsayo
        ContEnsayo=cont
        
        self.p=cont.buscarPozo(idpozo)
####    Poner el titulito con el nombre del pozo        
        Dialog.setObjectName(_fromUtf8("Asociar ensayos"))
        
        Dialog.resize(638, 252)

        self.guardar=Dialog
        self.model_po=modelotabla.modelotabla(self.p.observaciones,["Observaciones"])        
        self.listWidget = QtGui.QTableView(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(30, 20, 181, 211))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidget.setModel(self.model_po)

        self.model_pe=modelotabla.modelotabla(self.p.ensayos,["Ensayos"])  
        self.listWidget_2 = QtGui.QTableView(Dialog)
        self.listWidget_2.setGeometry(QtCore.QRect(230, 20, 181, 211))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.listWidget_2.setModel(self.model_pe)
        
        
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(430, 20, 181, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 50, 181, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        
        self.listado = QtGui.QTableView(Dialog)
        self.listado.setGeometry(QtCore.QRect(430, 80, 181, 121))
        self.listado.setObjectName(_fromUtf8("listado"))

        
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 210, 91, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(530, 210, 81, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))

        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.listarObservaciones)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")),self.listarEnsayos)
        QtCore.QObject.connect(self.listado, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), self.seleccionarDato)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")),self.asociar)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")),self.cancelar)
        
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Pozo n° "+str(self.p.id), None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Asociar observacion", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Dialog", "Asociar ensayo de bombeo", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Dialog", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("Dialog", "Agregar", None, QtGui.QApplication.UnicodeUTF8))


    def listarObservaciones(self):
##      al clickear en observaciones se va a mostrar el listado
        global ContEnsayo
        print 'observaciones'
        obss=ContEnsayo.observaciones
        self.model=modelotabla.modelotabla(obss, ["Lista de observaciones"])
        self.listado.setModel(self.model)
        self.tipo="o"

    def listarEnsayos(self):
##      al clickear en ensayos se va a mostrar el listado de ensayos
        global ContEnsayo
        print 'ensayos'
        enss=ContEnsayo.ensayos
        self.model=modelotabla.modelotabla(enss, ["Lista de ensayos"])
        self.listado.setModel(self.model)
        self.tipo="e"

    def seleccionarDato(self, item):
        global ContEnsayo
        ## Al hacer click en un item del listado se recupera el objeto        
        self.oe=self.model.objeto(item)

    def cancelar(self):
        self.guardar.close()

    def asociar(self):
        global ContEnsayo
        ####  mensajito si realmente quiere hacer la asociacion
        reply = QtGui.QMessageBox.question(self,"Informacion",
                "¿ Realmente desea asociar este item al pozo seleccionado?. ",
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No | QtGui.QMessageBox.Cancel)
        if reply == QtGui.QMessageBox.Yes:
        
            if self.tipo=="o" :
                self.p.agregarObservaciones(self.oe)
                ContEnsayo.eliminarObservaciones(self.oe)
            else:
                self.p.agregarEnsayo(self.oe)
                ContEnsayo.eliminarEnsayo(self.oe)
            
            ####  hay que desacioar del controlador el ensayo cargado            
                
            reply = QtGui.QMessageBox.information(self,
                    "Informacion",
                    "La asociación ha sido efectuada satisfactoriamente")
            if reply == QtGui.QMessageBox.Ok:
                print "asociado"            
            else:
                print "Escape"
            self.guardar.close()
        
            

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    frmasociarensayos = QtGui.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(frmasociarensayos)
    frmasociarensayos.show()
    sys.exit(app.exec_())        

