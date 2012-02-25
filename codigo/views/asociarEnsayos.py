# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asociarEnsayos.ui'
#
# Created: Thu Feb 02 18:47:42 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import modelotabla
import controlador

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(QtGui.QDialog):
    def setupUi(self, Asociarensayos, idpozo, cont, demo):
        global ContEnsayo
        ContEnsayo=cont
        self.p=cont.buscarPozo(idpozo)
        self.guardar=Asociarensayos       
        self.demo=demo
        ##Almacenar datos para desacer cambios al dar cancelar

        ContEnsayo.copiarObservacionesEnsayos()
        self.pcopia=self.p.copiaSuperficial()
    
        
        Asociarensayos.setObjectName(_fromUtf8("Asociarensayos"))
        Asociarensayos.resize(692, 295)

        self.model_pe=modelotabla.modelotabla(self.p.ensayos,["Id", "Nombre"])
        self.vistaEnsayos = QtGui.QTableView(Asociarensayos)
        self.vistaEnsayos.setGeometry(QtCore.QRect(280, 50, 181, 191))
        self.vistaEnsayos.setObjectName(_fromUtf8("vistaEnsayos"))
        self.vistaEnsayos.setModel(self.model_pe)
        self.vistaEnsayos.resizeColumnsToContents()

        self.model_po=modelotabla.modelotabla(self.p.observaciones,["Id", "Nombre"]) 
        self.vistaObservaciones = QtGui.QTableView(Asociarensayos)
        self.vistaObservaciones.setGeometry(QtCore.QRect(480, 50, 181, 191))
        self.vistaObservaciones.setObjectName(_fromUtf8("vistaObservaciones"))
        self.vistaObservaciones.setModel(self.model_po)
        self.vistaObservaciones.resizeColumnsToContents()
        
        self.vistaDatosControlador = QtGui.QTableView(Asociarensayos)
        self.vistaDatosControlador.setGeometry(QtCore.QRect(30, 80, 191, 161))
        self.vistaDatosControlador.setObjectName(_fromUtf8("vistaDatosControlador"))
        
        self.btn_Cancelar = QtGui.QPushButton(Asociarensayos)
        self.btn_Cancelar.setGeometry(QtCore.QRect(360, 260, 101, 23))
        self.btn_Cancelar.setObjectName(_fromUtf8("btn_Cancelar"))
        self.btn_Agregar = QtGui.QPushButton(Asociarensayos)
        self.btn_Agregar.setGeometry(QtCore.QRect(230, 120, 41, 23))
        self.btn_Agregar.setObjectName(_fromUtf8("btn_Agregar"))
        self.opcionensayo = QtGui.QRadioButton(Asociarensayos)
        self.opcionensayo.setGeometry(QtCore.QRect(30, 20, 191, 21))
        self.opcionensayo.setObjectName(_fromUtf8("opcionensayo"))
        self.opcionobservacion = QtGui.QRadioButton(Asociarensayos)
        self.opcionobservacion.setGeometry(QtCore.QRect(30, 50, 201, 21))
        self.opcionobservacion.setObjectName(_fromUtf8("opcionobservacion"))
        self.btn_Remover = QtGui.QPushButton(Asociarensayos)
        self.btn_Remover.setGeometry(QtCore.QRect(230, 170, 41, 23))
        self.btn_Remover.setObjectName(_fromUtf8("btn_Remover"))
        self.label = QtGui.QLabel(Asociarensayos)
        self.label.setGeometry(QtCore.QRect(280, 20, 181, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Asociarensayos)
        self.label_2.setGeometry(QtCore.QRect(480, 20, 191, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.btn_Aceptar = QtGui.QPushButton(Asociarensayos)
        self.btn_Aceptar.setGeometry(QtCore.QRect(230, 260, 101, 23))
        self.btn_Aceptar.setObjectName(_fromUtf8("btn_Aceptar"))
        ##Por defecto se eligen ensayos
        self.opcionensayo.setChecked(True)
        self.listarEnsayos()
        self.vistaDatosControlador.resizeColumnsToContents()
        self.tiporem=None
        self.tipo="e"
        self.oe=None
        self.oerem=None

        QtCore.QObject.connect(self.opcionobservacion, QtCore.SIGNAL(_fromUtf8("clicked()")),self.listarObservaciones)
        QtCore.QObject.connect(self.opcionensayo, QtCore.SIGNAL(_fromUtf8("clicked()")),self.listarEnsayos)
        QtCore.QObject.connect(self.vistaDatosControlador, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), self.seleccionarDato)

        QtCore.QObject.connect(self.vistaEnsayos, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), self.seleccionarDatoRemEnsayo)
        QtCore.QObject.connect(self.vistaObservaciones, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), self.seleccionarDatoRemObservacion)
        
        
        QtCore.QObject.connect(self.btn_Agregar, QtCore.SIGNAL(_fromUtf8("clicked()")),self.asociar)
        QtCore.QObject.connect(self.btn_Remover, QtCore.SIGNAL(_fromUtf8("clicked()")),self.desasociar)
        QtCore.QObject.connect(self.btn_Aceptar, QtCore.SIGNAL(_fromUtf8("clicked()")),self.aceptar)
        QtCore.QObject.connect(self.btn_Cancelar, QtCore.SIGNAL(_fromUtf8("clicked()")),self.cancelar)
        #QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")),self.cancelar)        

        self.retranslateUi(Asociarensayos)
        QtCore.QMetaObject.connectSlotsByName(Asociarensayos)

    def retranslateUi(self, Asociarensayos):
        #Asociarensayos.setWindowTitle(QtGui.QApplication.translate("Asociarensayos", u"Pozo n° "+str(self.p.id), None, QtGui.QApplication.UnicodeUTF8))

        Asociarensayos.setWindowTitle( "Pozo n° "+str(self.p.id))
        
        self.btn_Cancelar.setText(QtGui.QApplication.translate("Asociarensayos", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Agregar.setText(QtGui.QApplication.translate("Asociarensayos", ">>", None, QtGui.QApplication.UnicodeUTF8))
        self.opcionensayo.setText(QtGui.QApplication.translate("Asociarensayos", "Asociar Conjunto de bombeos", None, QtGui.QApplication.UnicodeUTF8))
        self.opcionobservacion.setText(QtGui.QApplication.translate("Asociarensayos", "Asociar Conjunto de observaciones", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Remover.setText(QtGui.QApplication.translate("Asociarensayos", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Asociarensayos", "Conj. de bombeos asociados", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Asociarensayos", "Conj. de observaciones asociados", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Aceptar.setText(QtGui.QApplication.translate("Asociarensayos", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))

    def listarObservaciones(self):
##      al clickear en observaciones se va a mostrar el listado
        global ContEnsayo
        #print 'observaciones'
        obss=ContEnsayo.observaciones
        self.model=modelotabla.modelotabla(obss, ["Id", "Nombre"])
        self.vistaDatosControlador.setModel(self.model)
        self.tipo="o"
        self.oe=None

    def listarEnsayos(self):
##      al clickear en ensayos se va a mostrar el listado de ensayos
        global ContEnsayo
#       print 'ensayos'
        enss=ContEnsayo.ensayos
        self.model=modelotabla.modelotabla(enss, ["Id", "Nombre"])
        self.vistaDatosControlador.setModel(self.model)
        self.tipo="e"
        self.oe=None

    def seleccionarDato(self, item):
        global ContEnsayo
        ## Al hacer click en un item del listado se recupera el objeto        
        self.oe=self.model.objeto(item)
        #print 'selecciono un dato'
        #print self.oe

    def seleccionarDatoRemEnsayo(self, item):
        global ContEnsayo
        ## Al hacer click en un item del listado se recupera el objeto        
        self.oerem=self.model_pe.objeto(item)
        #print 'selecciono un dato'
        #print self.oe
        self.tiporem="e"
    def seleccionarDatoRemObservacion(self, item):
        global ContEnsayo
        ## Al hacer click en un item del listado se recupera el objeto        
        self.oerem=self.model_po.objeto(item)
        #print 'selecciono un dato'
        #print self.oe
        self.tiporem="o"           

    def refrescar(self, actualizarControlador):
        self.model_po=modelotabla.modelotabla(self.p.observaciones,["Id", "Nombre"])       
        self.vistaObservaciones.setModel(self.model_po)
        self.model_pe=modelotabla.modelotabla(self.p.ensayos,["Id", "Nombre"])
        self.vistaEnsayos.setModel(self.model_pe)

        self.vistaEnsayos.resizeColumnsToContents()
        self.vistaObservaciones.resizeColumnsToContents()
        self.vistaDatosControlador.resizeColumnsToContents()

        if self.tiporem==self.tipo or actualizarControlador:
            print "dice que ira a actualizar el listado del controlador"
            if self.tipo=="o" :
                print "va a cargar las observaciones"
                self.listarObservaciones()
            else:
                print "va a cargar los bombeos"
                self.listarEnsayos()

    def aceptar(self):
        if self.demo!=True :
            reply = QtGui.QMessageBox.question(self,
                            "Información",
                            "Los datos han sido almacenados")
        self.guardar.close()
    
    def cancelar(self):
        ContEnsayo.restaurarObservacionesEnsayos()
        self.p.restaurarPozo(self.pcopia)
        if self.demo!=True :
            reply = QtGui.QMessageBox.question(self,
                            "Información",
                            "Todas las acciones han sido canceladas")         
        self.guardar.close()

    def asociar(self):
        global ContEnsayo
        ####  mensajito si realmente quiere hacer la asociacion
        ##Si no se ha seleccionado ningún elemento con click no se podrá realizar la asociacion
        if self.oe!=None:
##            print "al final no esta vacio se puede asociar "

            if self.tipo=="o" :
                if len(self.p.observaciones)>0:
                    reply = QtGui.QMessageBox.warning(self,
                            "Advertencia",
                            "Ya existe un conjunto de observaciones asociado al pozo seleccionado. Si lo considera necesario, primero desocie los datos y vuelva a relizar esta operación")
                    return                
            else:
                if len(self.p.ensayos)>0:
                    reply = QtGui.QMessageBox.warning(self,
                            "Advertencia",
                            "Ya existe un conjunto de bombeos asociado al pozo seleccionado. Si lo considera necesario, primero desocie los datos y vuelva a relizar esta operación")                                    
                    return
                
            if self.demo==True :
                reply = QtGui.QMessageBox.Yes
            else:
                reply = QtGui.QMessageBox.question(self,"Confirmación",
                        "¿Realmente desea asociar este ítem al pozo seleccionado?.",
                        QtGui.QMessageBox.Yes | QtGui.QMessageBox.No | QtGui.QMessageBox.Cancel)
                
            if reply == QtGui.QMessageBox.Yes:
                ####  hay que desacioar del controlador el ensayo cargado
                if self.tipo=="o" :
                    self.p.agregarObservaciones(self.oe)
                    ContEnsayo.eliminarObservaciones(self.oe)
                else:
                    self.p.agregarEnsayo(self.oe)
                    ContEnsayo.eliminarEnsayo(self.oe)

                if self.demo==True :
                    reply = QtGui.QMessageBox.Ok
                else:                            
                    reply = QtGui.QMessageBox.information(self,
                            "Información",
                            "La asociación ha sido efectuada satisfactoriamente")
                
                #if reply == QtGui.QMessageBox.Ok:
                #print "asociado"
                self.oe=None
                self.refrescar(True)                
                #else:
                #print "Escape"
        else:            
            reply = QtGui.QMessageBox.warning(self,
                    "Advertencia",
                    "Debe seleccionar un elemento para asociar")

    def desasociar(self):
        global ContEnsayo
        ####  mensajito si realmente quiere hacer la asociacion
        if self.oerem!=None:
##            print "al final no esta vacio se puede asociar"
        
            if self.demo==True :
                reply = QtGui.QMessageBox.Yes
            else:
                reply = QtGui.QMessageBox.question(self,"Confirmación",
                        "¿Realmente desea desasociar este item con el pozo seleccionado?. ",
                        QtGui.QMessageBox.Yes | QtGui.QMessageBox.No | QtGui.QMessageBox.Cancel)
                
            if reply == QtGui.QMessageBox.Yes:
                ####  hay que desacioar del controlador el ensayo cargado
                if self.tiporem=="o" :
                    self.p.eliminarObservaciones(self.oerem)
                    ContEnsayo.restaurarObservacion(self.oerem)
                else:
                    self.p.eliminarEnsayo(self.oerem)
                    ContEnsayo.restaurarEnsayo(self.oerem)

                if self.demo==True :
                    reply = QtGui.QMessageBox.Ok
                else:                            
                    reply = QtGui.QMessageBox.information(self,
                            "Información",
                            "Los datos han sido desasoaciados correctamente")
                
                #if reply == QtGui.QMessageBox.Ok:
                #print "asociado"
                self.oerem=None
                self.refrescar(False)                
                #else:
                #print "Escape"
        else:
            reply = QtGui.QMessageBox.warning(self,
                    "Información",
                    "Debe seleccionar un elemento para desasociar")           

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    frmImpProyecto = QtGui.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(frmImpProyecto)
    frmImpProyecto.show()
    sys.exit(app.exec_())
