# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created: Thu Dec 08 19:29:21 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
sys.path.append("views")
sys.path.append("models")
import importarCaudal
import controlador
import verensayos
import NuevoProyecto
import ingresarCaudal
import importarObservaciones
import ingresarObservaciones
import verObservaciones
import metodoSolucion
import asociarEnsayos
import metodooptimizacion
from theis import *
from vistaDominio import  *
from vistaDominiolaRemodelacion import  *
from views.dibujante import dibujante
from views.dibujante_interpolacion import dibujante2

import random#Solo para pruebas

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(QtGui.QDialog):

    def setupUi(self, MainWindow):
        ##Se instancia el controlador
        global ContEnsayo

        ContEnsayo=controlador.Proyecto()

        self.dibujante = None
        self.dibujaten2=None

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Tipon Python", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuInicio = QtGui.QMenu(self.menubar)
        self.menuInicio.setTitle(QtGui.QApplication.translate("MainWindow", "Inicio", None, QtGui.QApplication.UnicodeUTF8))
        self.menuInicio.setObjectName(_fromUtf8("menuInicio"))
        self.menuAyuda = QtGui.QMenu(self.menubar)
        self.menuAyuda.setTitle(QtGui.QApplication.translate("MainWindow", "Ayuda", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAyuda.setObjectName(_fromUtf8("menuAyuda"))
        self.menuDatos = QtGui.QMenu(self.menubar)
        self.menuDatos.setTitle(QtGui.QApplication.translate("MainWindow", "Datos", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDatos.setObjectName(_fromUtf8("menuDatos"))

        self.menuGraficar = QtGui.QMenu(self.menubar)
        self.menuGraficar.setTitle(QtGui.QApplication.translate("MainWindow", "Graficar", None, QtGui.QApplication.UnicodeUTF8))
        self.menuGraficar.setObjectName(_fromUtf8("menuGraficar"))

        self.menuCaudal_de_bombeo = QtGui.QMenu(self.menuDatos)
        self.menuCaudal_de_bombeo.setTitle(QtGui.QApplication.translate("MainWindow", "Caudal de bombeo", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCaudal_de_bombeo.setObjectName(_fromUtf8("menuCaudal_de_bombeo"))
        self.menuObservaciones = QtGui.QMenu(self.menuDatos)
        self.menuObservaciones.setTitle(QtGui.QApplication.translate("MainWindow", "Observaciones", None, QtGui.QApplication.UnicodeUTF8))
        self.menuObservaciones.setObjectName(_fromUtf8("menuObservaciones"))
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNuevo_Proyecto = QtGui.QAction(MainWindow)
        self.actionNuevo_Proyecto.setText(QtGui.QApplication.translate("MainWindow", "Nuevo Proyecto", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNuevo_Proyecto.setObjectName(_fromUtf8("actionNuevo_Proyecto"))
        self.actionAcerca_de = QtGui.QAction(MainWindow)
        self.actionAcerca_de.setText(QtGui.QApplication.translate("MainWindow", "Acerca de..", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAcerca_de.setObjectName(_fromUtf8("actionAcerca_de"))
        self.actionCerrar = QtGui.QAction(MainWindow)
        self.actionCerrar.setText(QtGui.QApplication.translate("MainWindow", "Cerrar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCerrar.setObjectName(_fromUtf8("actionCerrar"))
        self.actionSalir = QtGui.QAction(MainWindow)
        self.actionSalir.setText(QtGui.QApplication.translate("MainWindow", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))

        self.actionImportar = QtGui.QAction(MainWindow)
        self.actionImportar.setText(QtGui.QApplication.translate("MainWindow", "Importar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImportar.setObjectName(_fromUtf8("actionImportar"))
        self.actionIngresar = QtGui.QAction(MainWindow)
        self.actionIngresar.setText(QtGui.QApplication.translate("MainWindow", "Ingresar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIngresar.setObjectName(_fromUtf8("actionIngresar"))
        self.actionVerBombeo = QtGui.QAction(MainWindow)
        self.actionVerBombeo.setText(QtGui.QApplication.translate("MainWindow", "Ver", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVerBombeo.setObjectName(_fromUtf8("actionVerBombeo"))

        self.actionImpObs = QtGui.QAction(MainWindow)
        self.actionImpObs.setText(QtGui.QApplication.translate("MainWindow", "Importar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImpObs.setObjectName(_fromUtf8("actionImpObs"))
        self.actionIngObs = QtGui.QAction(MainWindow)
        self.actionIngObs.setText(QtGui.QApplication.translate("MainWindow", "Ingresar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIngObs.setObjectName(_fromUtf8("actionIngObs"))
        self.actionVerObs = QtGui.QAction(MainWindow)
        self.actionVerObs.setText(QtGui.QApplication.translate("MainWindow", "Ver", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVerObs.setObjectName(_fromUtf8("actionVerObs"))

        self.actionGenerar_graficas = QtGui.QAction(MainWindow)
        self.actionGenerar_graficas.setText(QtGui.QApplication.translate("MainWindow", u"Generar gráficas", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGenerar_graficas.setObjectName(_fromUtf8("actionGenerar_graficas"))

        self.actionGenerar_graficas2 = QtGui.QAction(MainWindow)
        self.actionGenerar_graficas2.setText(QtGui.QApplication.translate("MainWindow", u"Cargar demo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGenerar_graficas2.setObjectName(_fromUtf8("actionGenerar_graficas2"))


        self.actionGenerar_video = QtGui.QAction(MainWindow)
        self.actionGenerar_video.setText(QtGui.QApplication.translate("MainWindow", "Generar video...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGenerar_video.setObjectName(_fromUtf8("actionGenerar_video"))

        self.menuInicio.addAction(self.actionNuevo_Proyecto)
        self.menuInicio.addAction(self.actionCerrar)
        self.menuInicio.addAction(self.actionSalir)
        self.menuAyuda.addAction(self.actionAcerca_de)

        self.menuCaudal_de_bombeo.addAction(self.actionIngresar)
        self.menuCaudal_de_bombeo.addAction(self.actionImportar)
        self.menuCaudal_de_bombeo.addAction(self.actionVerBombeo)

        self.menuObservaciones.addAction(self.actionIngObs)
        self.menuObservaciones.addAction(self.actionImpObs)
        self.menuObservaciones.addAction(self.actionVerObs)

        self.menuDatos.addAction(self.menuCaudal_de_bombeo.menuAction())
        self.menuDatos.addAction(self.menuObservaciones.menuAction())

        self.menuGraficar.addAction(self.actionGenerar_graficas)
        self.menuGraficar.addAction(self.actionGenerar_graficas2)
        self.menuGraficar.addAction(self.actionGenerar_video)

        self.menubar.addAction(self.menuInicio.menuAction())
        self.menubar.addAction(self.menuDatos.menuAction())
        self.menubar.addAction(self.menuGraficar.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionSalir, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.actionNuevo_Proyecto, QtCore.SIGNAL(_fromUtf8("triggered()")), self.ventanaNuevoProyecto)
        QtCore.QObject.connect(self.actionImportar, QtCore.SIGNAL(_fromUtf8("triggered()")), self.ventanaImportarProyecto)
        QtCore.QObject.connect(self.actionVerBombeo, QtCore.SIGNAL(_fromUtf8("triggered()")), self.ventanaVerBombeo)
        QtCore.QObject.connect(self.actionIngresar, QtCore.SIGNAL(_fromUtf8("triggered()")), self.ventanaIngresarBombeo)
        QtCore.QObject.connect(self.actionImpObs, QtCore.SIGNAL(_fromUtf8("triggered()")), self.ventanaImpoObs)
        QtCore.QObject.connect(self.actionVerObs, QtCore.SIGNAL(_fromUtf8("triggered()")), self.ventanaVerObs)
        QtCore.QObject.connect(self.actionIngObs, QtCore.SIGNAL(_fromUtf8("triggered()")), self.ventanaIngObs)

        QtCore.QObject.connect(self.actionGenerar_graficas, QtCore.SIGNAL(_fromUtf8("triggered()")), self.generar_graficas)
        QtCore.QObject.connect(self.actionGenerar_graficas2, QtCore.SIGNAL(_fromUtf8("triggered()")), self.cargar_demo)
        QtCore.QObject.connect(self.actionGenerar_video, QtCore.SIGNAL(_fromUtf8("triggered()")), self.generar_video)

        QtCore.QObject.connect(self.menuCaudal_de_bombeo, QtCore.SIGNAL(_fromUtf8("hovered()")), self.despliegueCaudal)
        QtCore.QObject.connect(self.menuObservaciones, QtCore.SIGNAL(_fromUtf8("hovered()")), self.despligueObservacion)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ##Leer parametros
        ContEnsayo.leerParametros()

        ####Prueba de instanciar un metodo de solucion
        ####Se le pasa el dominio, los parametros cargados en el sistema        
##        m=Theis(ContEnsayo.dominio, ContEnsayo.parametros)                
##        m.setearValores([500,0.001])


    def retranslateUi(self, MainWindow):
        pass

    def despliegueCaudal(self):
        print "abre caudal"

    def despligueObservacion(self):
        print "abre observaciones"

    def ventanaNuevoProyecto(self):
        frmNuevoProyecto = QtGui.QDialog()
        ui = NuevoProyecto.Ui_frmNuevoProyecto()
        
	#Adherimos la vista del dominio
	self.ui = Ui_Form()
	#self.ui = UiForm()

        ui.setupUi(frmNuevoProyecto,ContEnsayo)
        
        QtCore.QObject.connect(ui.btnNuevo, QtCore.SIGNAL('clicked()'), self.abrirDominio)

        frmNuevoProyecto.exec_()

    def abrirDominio(self):
	self.ui.setupUi(MainWindow, ContEnsayo)


    def ventanaImportarProyecto(self, noexec=None):
        global ContEnsayo
        frmImpCaudal = QtGui.QDialog()
        ui = importarCaudal.Ui_Dialog()
        ## Se envia al nuevo formulario el controlador instanciado
        ui.setupUi(frmImpCaudal, ContEnsayo)
        self.importar=ui
        if noexec==None:
            frmImpCaudal.exec_()

    def ventanaVerBombeo(self):
        global ContEnsayo
        enss=ContEnsayo.ensayos
        if len(enss)<=0 :
            QtGui.QMessageBox.information(self,
                "Informacion",
                "Aún no se ha ingresado ningún ensayo de bombeo")
        else:
            frmVerBombeo = QtGui.QDialog()
            ui = verensayos.Ui_Dialog()
            ## Se envia al nuevo formulario el controlador instanciado
            ui.setupUi(frmVerBombeo, ContEnsayo)
            frmVerBombeo.exec_()

    def ventanaIngresarBombeo(self):
        global ContEnsayo
        frmIngBombeo = QtGui.QDialog()
        ui = ingresarCaudal.Ui_Dialog()
        ui.setupUi(frmIngBombeo, ContEnsayo)
        frmIngBombeo.exec_()

    def ventanaImpoObs(self, noexec=None):
        global ContEnsayo
        frmimpobs=QtGui.QDialog()
        ui= importarObservaciones.Ui_Dialog()
        ui.setupUi(frmimpobs, ContEnsayo)
        self.vimp=ui
        if noexec==None:
            frmimpobs.exec_()
        
    def ventanaVerObs(self):

        global ContEnsayo
        obss=ContEnsayo.observaciones
        if len(obss)<=0 :
            QtGui.QMessageBox.information(self,
                u"Información",
                u"Aún no se ha ingresado ninguna Observación de ensayo")
        else:
            frmverobs=QtGui.QDialog()
            ui= verObservaciones.Ui_Dialog()
            ui.setupUi(frmverobs, ContEnsayo)
            frmverobs.exec_()
        
    def ventanaIngObs(self):
        global ContEnsayo
        frmingobs=QtGui.QDialog()
        ui= ingresarObservaciones.Ui_Dialog()
        ui.setupUi(frmingobs, ContEnsayo)
        frmingobs.exec_()

    def generar_graficas(self):

        if self.dibujante != None:

            print u'Ya hay una instancia corriendo'
            self.dibujante.raise_()#Aca mostramos la ventana si ya existe

        else:
            ##Codigo de alvaro para generar una matriz
            ran = random.randint(10, 30)
            print 'ran: ' + str(ran)
            zcol = []

            for i in range(0, ran):
                z = np.random.multivariate_normal((1, 1), [[ran, 0], [0, ran]], ran).T
                z = z**2
                zcol.append(z)

            #matrix = [np.arange(0, ran), zcol]          
            
            #print '<Matrix>\n' + str(matrix) + '\n</Matrix>'

            global ContEnsayo

            pozo = ContEnsayo.dominio.obtenerPozoBombeo()

            if len(ContEnsayo.dominio.listaPozo) < 1:

                print 'No hay ningun pozo'
                #self.dialogos('No hay ningun pozo')
                QtGui.QMessageBox.information(self,
                    "Error",
                    "No hay ningun pozo")                

            else:

                if pozo != None:
                    
                    if len(pozo.ensayos) > 0:

                        if len(pozo.observaciones) > 0:
                
                            self.dibujante = dibujante(self, ContEnsayo.dominio)#Hay que pasarle la ventana principal
                            self.dibujante.show()
                            QtCore.QObject.connect(self.dibujante, QtCore.SIGNAL(_fromUtf8("destroyed()")), self.limpiarDibujante)
                            print 'Dibujante invocado'

                        else:

                            #print 'No hay observaciones asociadas al pozo'
                            QtGui.QMessageBox.information(self,
                                "Error",
                                "No hay observaciones asociadas al pozo")                             

                    else:

                        #print 'No hay ensayos asociados al pozo'
                        QtGui.QMessageBox.information(self,
                            "Error",
                            "No hay ensayos asociados al pozo")                           

                else:

                    #print 'No hay pozo de bombeo'
                    QtGui.QMessageBox.information(self,
                            "Error",
                            "No hay pozo de bombeo")                       


    def generar_graficas2(self):
        global ContEnsayo
##        self.dibujante2 = dibujante2(self, ContEnsayo)#Hay que pasarle la ventana principal
##        self.dibujante2.show()

        ContEnsayo.dominio.alto = 100
        ContEnsayo.dominio.ancho = 100
        ##Como prueba se elijio el metodo Theis de una, esto ya asocia el metodo al dominio
        m=Theis(ContEnsayo.dominio, ContEnsayo.parametros)                
        m.setearValores([500,0.001])
        #Adherimos la vista del dominio
        self.ui = Ui_Form()
        self.ui.setupUi(MainWindow, ContEnsayo)

        b = boton(QtGui.QIcon("content/images/blackDotIcon.png"), "", self.ui.caja, "pozo")
        b.id = ContEnsayo.agregarPozo(20, 20)   
        b.setStyleSheet("border: none")	
        b.setGeometry(QtCore.QRect(20,20, 24, 24))                 
        self.ui.caja.botones.append(b)
        b.show()

        noexec=1
        
        self.ventanaImpoObs(noexec)
        self.vimp.archivo="ficheros/ensayo_tchicos.ods"
        self.vimp.nombre.setText('obs1')
        self.vimp.ext="ods"
        self.vimp.accionaceptar()
        self.vimp.close()
        
        self.ventanaImportarProyecto(noexec)
        self.importar.archivo="ficheros/ensayo_tchicos.ods"
        self.importar.nombre.setText('ens1')
        self.importar.ext="ods"
        self.importar.accionaceptar()
        self.importar.close()

        
        frmasociar=QtGui.QDialog()
        asoe= asociarEnsayos.Ui_Dialog()
        asoe.setupUi(frmasociar, b.id, ContEnsayo)        
        asoe.oe=ContEnsayo.observaciones[0]
        asoe.tipo="o"
        asoe.asociar()

        asoe.setupUi(frmasociar, b.id, ContEnsayo)        
        asoe.oe=ContEnsayo.ensayos[0]
        asoe.tipo="e"
        asoe.asociar()
        
                
        print 'se carga el demo'


    def cargar_demo(self):
        global ContEnsayo

        ContEnsayo.dominio.alto = 10
        ContEnsayo.dominio.ancho = 10
        ContEnsayo.dominio.a=0
        ContEnsayo.dominio.b=0
        ContEnsayo.dominio.c=10
        ##Como prueba se elijio el metodo Theis de una, esto ya asocia el metodo al dominio
        m=Theis(ContEnsayo.dominio, ContEnsayo.parametros)                
        m.setearValores([1000,0.0001])
        #Adherimos la vista del dominio
        self.ui = Ui_Form()
        self.ui.setupUi(MainWindow, ContEnsayo)

        b = boton(QtGui.QIcon("content/images/blackDotIcon.png"), "", self.ui.caja, "pozo")
        b.id = ContEnsayo.agregarPozo(5, 2)

        b.setStyleSheet("border: none")	
        b.setGeometry(QtCore.QRect(5, 2, 24, 24))                 
        self.ui.caja.botones.append(b)
        b.show()

        noexec=1
        
        self.ventanaImpoObs(noexec)
        self.vimp.archivo="ficheros/ensayo_tchicos.ods"
        self.vimp.nombre.setText('obs1')
        self.vimp.ext="ods"
        self.vimp.accionaceptar()
        self.vimp.close()
        
        self.ventanaImportarProyecto(noexec)
        self.importar.archivo="ficheros/demo.ods"
        self.importar.nombre.setText('ens1')
        self.importar.ext="ods"
        self.importar.accionaceptar()
        self.importar.close()
        
        frmasociar=QtGui.QDialog()
        asoe=asociarEnsayos.Ui_Dialog()
        asoe.setupUi(frmasociar, b.id, ContEnsayo)        
        asoe.oe=ContEnsayo.observaciones[0]
        asoe.tipo="o"
        asoe.asociar()

        asoe.setupUi(frmasociar, b.id, ContEnsayo)        
        asoe.oe=ContEnsayo.ensayos[0]
        asoe.tipo="e"
        asoe.asociar()
        
                
        print 'se carga el demo'
        
            
    def limpiarDibujante(self):

        self.dibujante = None

    def generar_video(self):

        print u'Próximamente se exportará un video con esta opción'

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)

    app.setStyleSheet("QGroupBox{color: green} \n"
                      "QLineEdit{color: blue} \n"
                      "QLabel{color: red} \n"
                      "QPushButton{color: navy}")
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
