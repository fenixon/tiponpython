# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\optimizacion.ui'
#
# Created: Thu Dec 29 19:05:49 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class optimizacion(QtGui.QWidget):
    def __init__(self,cont,Form):
        super(optimizacion, self).__init__()
        global controlador
        global pozosparaoptimizar
        global pozosconfirmados
        self.pozosconfirmados=[]
        controlador=cont
        self.pozosparaoptimizar=controlador.listarPozosParaOptimizar() 
        self.setupUi()
            
    def setupUi(self):
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 20, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setText(QtGui.QApplication.translate("Form", "Optimizacion", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(200, 70, 91, 16))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Metodo a Utilizar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 158, 36))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Pozos Seleccionados", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.cargardatos(self)
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
    def cargardatos(self,formulario):
        #Listo los pozos que se le asociaron metodos de optimizacion
        posiciony=100
        for pozo in self.pozosparaoptimizar:
            #Creo la lista de pozos a optimizar
            #Creo el checkbox
            self.checkBox=QtGui.QCheckBox(str(pozo),self)        
            self.checkBox.stateChanged.connect(self.mensajecheckbox)
            self.checkBox.setGeometry(QtCore.QRect(40, posiciony, 69, 30))
            self.checkBox.toggle()            
            #Creo el combobox con las optimizaciones
            globals()["comboBox"+ str(pozo)]=QtGui.QComboBox(self)
            globals()["comboBox"+ str(pozo)].setGeometry(QtCore.QRect(200, posiciony, 69, 22))
            posiciony=posiciony+20
            #agrego todas las optimizaciones a combo
            globals()["comboBox"+ str(pozo)].addItem(self.pozosparaoptimizar[pozo], pozo)
            globals()["comboBox"+ str(pozo)].setItemData(0,QtCore.QVariant(pozo))
            globals()["comboBox"+ str(pozo)].addItems(controlador.optimizacioneslistarmenos(self.pozosparaoptimizar[pozo]))
            globals()["comboBox"+ str(pozo)].setCurrentIndex(0)
            self.connect(globals()["comboBox"+ str(pozo)], QtCore.SIGNAL('currentIndexChanged(int)'),self.cambiarmetodooptimizacion)
        #Boton para confirmar la/s optimizaciones
        accion=QtGui.QPushButton('Procesar ',self)
        accion.setGeometry(200,posiciony + 200,60,35)
        self.connect(accion, QtCore.SIGNAL('clicked()'),self.procesar)        
    def retranslateUi(self, Form):
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        self.listWidget.setSortingEnabled(__sortingEnabled)
    def mensajecheckbox(self,state):
        print  self.checkBox
        if state == QtCore.Qt.Checked:
            #Si esta desactivado lo activo en la coleccion
            self.pozosconfirmados.append(str(self.sender().text()))
        else:
            #Si esta activado lo desactivo en la coleccion
            self.pozosconfirmados.remove(str(self.sender().text()))
    def ejemplo(coso):
        print "ejemplo"
    def cambiarmetodooptimizacion(self,indice):
        #Obtengo el pozo seleccionado y le cambio el metodo de solucion al elegido
        #print "Pozo:" + str(self.sender().itemData(0).toInt()[0])
        #print "Cambiar a:" +self.sender().currentText()
        #Le asocio el nuevo metodo
        controlador.asociarPozoOptimiazion(self.sender().itemData(0).toInt()[0],self.sender().currentText())              
    def procesar(self):
        print "Proceso la matriz"
        for p in self.pozosconfirmados:
            print "Pozo:" + str(p)
            print "Se le asigno el Metodo optimizacion:" + self.pozosparaoptimizar[int(p)]