# -*- coding: utf-8 -*-
"""
	tiponpython Simulacion de ensayos de acuiferos
	Copyright 2012 Andres Pias, Mathias Chubrega, Alvaro Correa, Sebastian Daloia, Jesus Guibert
	
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
import sys
sys.path.append("views")
sys.path.append("models")
import importarCaudal
import controlador
import verensayos
import NuevoProyecto
import editarParametros
import ingresarCaudal
import importarObservaciones
import ingresarObservaciones
import verObservaciones
import metodoSolucion
import asociarEnsayos
import metodooptimizacion
from theis import *
from Hantush import *
from DiferenciaFinita import *
from vistaDominiolaRemodelacion import  *
import discretizaciones
from views.dibujante import dibujante
from views.dibujante_interpolacion import dibujante2
from views.graficarOpt import graficarOpt

try:

    _fromUtf8 = QtCore.QString.fromUtf8

except AttributeError:

    _fromUtf8 = lambda s: s

class Ui_MainWindow(QtGui.QDialog):

    def setupUi(self, MainWindow):      

        self.dibujante = None
        self.dibujaten2=None

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)

        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Sistema de interpretación de ensayos de bombeo en acuíferos - TIP' 09", None, QtGui.QApplication.UnicodeUTF8))
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
        self.menuGraficar.setTitle(QtGui.QApplication.translate("MainWindow", "Simular", None, QtGui.QApplication.UnicodeUTF8))
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

        self.actionCerrar_Proyecto = QtGui.QAction(MainWindow)
        self.actionCerrar_Proyecto.setText(QtGui.QApplication.translate("MainWindow", "Cerrar Proyecto", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCerrar_Proyecto.setObjectName(_fromUtf8("actionCerrar_Proyecto"))

        
        self.actionAcerca_de = QtGui.QAction(MainWindow)
        self.actionAcerca_de.setText(QtGui.QApplication.translate("MainWindow", "Acerca de..", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAcerca_de.setObjectName(_fromUtf8("actionAcerca_de"))
        self.actionCerrar = QtGui.QAction(MainWindow)
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

        self.actionGenerar_graficas2 = QtGui.QAction(MainWindow)
        self.actionGenerar_graficas2.setText(QtGui.QApplication.translate("MainWindow", u"Cargar datos de prueba (Theis)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGenerar_graficas2.setObjectName(_fromUtf8("actionGenerar_graficas2"))       
        self.actionGenerar_graficas3 = QtGui.QAction(MainWindow)
        self.actionGenerar_graficas3.setText(QtGui.QApplication.translate("MainWindow", u"Cargar datos de prueba (Hantush)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGenerar_graficas3.setObjectName(_fromUtf8("actionGenerar_graficas3"))  
        self.actionGenerar_graficas4 = QtGui.QAction(MainWindow)
        self.actionGenerar_graficas4.setText(QtGui.QApplication.translate("MainWindow", u"Cargar datos de prueba (Diferencias Finitas)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGenerar_graficas4.setObjectName(_fromUtf8("actionGenerar_graficas4"))

        self.actionEditarParametros = QtGui.QAction(MainWindow)
        self.actionEditarParametros.setText(QtGui.QApplication.translate("MainWindow", "Editar Parametros", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditarParametros.setObjectName(_fromUtf8("EditarParametros"))              

        self.actionGenerar_graficas = QtGui.QAction(MainWindow)
        self.actionGenerar_graficas.setText(QtGui.QApplication.translate("MainWindow", u"Graficar niveles calculados", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGenerar_graficas.setObjectName(_fromUtf8("actionGenerar_graficas"))

        self.actionOptimizacion = QtGui.QAction(MainWindow)
        self.actionOptimizacion.setText(QtGui.QApplication.translate("MainWindow", u"Optimizacion", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOptimizacion.setObjectName(_fromUtf8("actionOptimizacion"))


        self.actionGrafOpt = QtGui.QAction(MainWindow)
        self.actionGrafOpt.setText(QtGui.QApplication.translate("MainWindow", u"Graficar optimizaciones", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGrafOpt.setObjectName(_fromUtf8("actionGrafOpt"))

        self.menuInicio.addAction(self.actionNuevo_Proyecto)
        self.menuInicio.addAction(self.actionCerrar_Proyecto)        
        self.menuInicio.addAction(self.actionSalir)
        self.menuAyuda.addAction(self.actionAcerca_de)

        self.menuCaudal_de_bombeo.addAction(self.actionIngresar)
        self.menuCaudal_de_bombeo.addAction(self.actionImportar)
        self.menuCaudal_de_bombeo.addAction(self.actionVerBombeo)

        self.menuObservaciones.addAction(self.actionIngObs)
        self.menuObservaciones.addAction(self.actionImpObs)
        self.menuObservaciones.addAction(self.actionVerObs)

        self.menuDatos.addAction(self.actionEditarParametros)
        self.menuDatos.addAction(self.menuCaudal_de_bombeo.menuAction())
        self.menuDatos.addAction(self.menuObservaciones.menuAction())        
        self.menuDatos.addAction(self.actionGenerar_graficas2)
        self.menuDatos.addAction(self.actionGenerar_graficas3)
        self.menuDatos.addAction(self.actionGenerar_graficas4)

        self.menuGraficar.addAction(self.actionGenerar_graficas)
        self.menuGraficar.addAction(self.actionOptimizacion)
        self.menuGraficar.addAction(self.actionGrafOpt)
        
        self.menubar.addAction(self.menuInicio.menuAction())
        self.menubar.addAction(self.menuDatos.menuAction())
        self.menubar.addAction(self.menuGraficar.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionSalir, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.actionNuevo_Proyecto, QtCore.SIGNAL(_fromUtf8("triggered()")), self.ventanaNuevoProyecto)
        
        QtCore.QObject.connect(self.actionCerrar_Proyecto, QtCore.SIGNAL(_fromUtf8("triggered()")), self.cerrarProyecto)
        
        QtCore.QObject.connect(self.actionImportar, QtCore.SIGNAL(_fromUtf8("triggered()")), self.ventanaImportarProyecto)
        QtCore.QObject.connect(self.actionVerBombeo, QtCore.SIGNAL(_fromUtf8("triggered()")), self.ventanaVerBombeo)
        QtCore.QObject.connect(self.actionIngresar, QtCore.SIGNAL(_fromUtf8("triggered()")), self.ventanaIngresarBombeo)
        QtCore.QObject.connect(self.actionImpObs, QtCore.SIGNAL(_fromUtf8("triggered()")), self.ventanaImpoObs)
        QtCore.QObject.connect(self.actionVerObs, QtCore.SIGNAL(_fromUtf8("triggered()")), self.ventanaVerObs)
        QtCore.QObject.connect(self.actionIngObs, QtCore.SIGNAL(_fromUtf8("triggered()")), self.ventanaIngObs)


        QtCore.QObject.connect(self.actionEditarParametros, QtCore.SIGNAL(_fromUtf8("triggered()")), self.ventanaEditarParametros)
        QtCore.QObject.connect(self.actionGenerar_graficas, QtCore.SIGNAL(_fromUtf8("triggered()")), self.generar_graficas)
        QtCore.QObject.connect(self.actionGenerar_graficas2, QtCore.SIGNAL(_fromUtf8("triggered()")), self.cargar_demobarrera1000theis)
        QtCore.QObject.connect(self.actionGenerar_graficas3, QtCore.SIGNAL(_fromUtf8("triggered()")), self.cargar_demobarrera1000hantush)
        QtCore.QObject.connect(self.actionGenerar_graficas4, QtCore.SIGNAL(_fromUtf8("triggered()")), self.cargar_demoNumerico)
        QtCore.QObject.connect(self.actionOptimizacion, QtCore.SIGNAL(_fromUtf8("triggered()")), self.Optimizacion)
        QtCore.QObject.connect(self.actionAcerca_de, QtCore.SIGNAL(_fromUtf8("triggered()")), self.acercaDe)


        QtCore.QObject.connect(self.actionGrafOpt, QtCore.SIGNAL(_fromUtf8("triggered()")), self.GraficasOptimizacion)
        QtCore.QObject.connect(self.menuCaudal_de_bombeo, QtCore.SIGNAL(_fromUtf8("hovered()")), self.despliegueCaudal)
        QtCore.QObject.connect(self.menuObservaciones, QtCore.SIGNAL(_fromUtf8("hovered()")), self.despligueObservacion)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.grop = None

        ####Prueba de instanciar un metodo de solucion
        ####Se le pasa el dominio, los parametros cargados en el sistema
##        m=Theis(ContEnsayo.dominio, ContEnsayo.parametros)
##        m.setearValores([500,0.001])

    def retranslateUi(self, MainWindow):
        pass

    def despliegueCaudal(self):

        #print "abre caudal"
        pass

    def despligueObservacion(self):

        #print "abre observaciones"
        pass

    def ventanaNuevoProyecto(self):
        ##Se instancia el controlador
        global ContEnsayo
        ContEnsayo=controlador.Proyecto()
        
        frmNuevoProyecto = QtGui.QDialog()
        ui = NuevoProyecto.Ui_frmNuevoProyecto()

	#Adherimos la vista del dominio
        self.ui = UiForm()
        ui.setupUi(frmNuevoProyecto, ContEnsayo)

        QtCore.QObject.connect(ui.btnNuevo, QtCore.SIGNAL('clicked()'), self.abrirDominio)
        frmNuevoProyecto.exec_()

    def cerrarProyecto(self):
        global ContEnsayo
        self.ui.cerrar()
        self.ui=None
        ContEnsayo.metodo=None
        ContEnsayo.dominio=None
        ContEnsayo=None        

    def ventanaEditarParametros(self):
        frmEditarParametros = QtGui.QDialog()
        ui = editarParametros.UifrmEditarParametros()
        ui.setupUi(frmEditarParametros, ContEnsayo)
        frmEditarParametros.exec_()
        for v in ContEnsayo.dominio.valores:
            print "valor. ",v.valor

    def abrirDominio(self):
        self.ui.setupUi(MainWindow, ContEnsayo, app.desktop().size().width(), app.desktop().size().height())


    def ventanaImportarProyecto(self, noexec=None, demo=None):
        global ContEnsayo
        frmImpCaudal = QtGui.QDialog()
        ui = importarCaudal.Ui_Dialog()
        ## Se envia al nuevo formulario el controlador instanciado
        ui.setupUi(frmImpCaudal, ContEnsayo, demo)
        self.importar=ui
        if noexec==None:
            frmImpCaudal.exec_()

    def ventanaVerBombeo(self):
        global ContEnsayo
        enss=ContEnsayo.ensayos
        if len(enss)<=0 :
            QtGui.QMessageBox.information(self,
                u"Información",
                u"No existe ningún conjunto de bombeos cargado en el sistema y sin asociar")
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

    def ventanaImpoObs(self, noexec=None, demo=None):
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
                u"No existe ningún conjunto de observaciones cargado en el sistema y sin asociar")

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

    def Optimizacion(self):

        global ContEnsayo
        diccionario=elementoDominio.ContEnsayo.listarPozosObsParaOptimizar()
        claves=diccionario.keys()

        if (claves!=[]):

            frmopt=QtGui.QWidget()
            ui= vistaoptimizacion.optimizacion(elementoDominio.ContEnsayo,frmopt)
            frmopt.show()
            self.widget = ui
            #print "muestro la opt"

        else:

            #Si no existen asociaciones doy error
            reply = QtGui.QMessageBox.warning(self,
                            "Error",
                            "No se realizaron asociaciones desde el dominio.") 

    def limpiarDibujante(self):

        self.dibujante = None

    def generar_graficas(self):

        if self.dibujante != None:

            #print u'Ya hay una instancia corriendo'
            self.dibujante.raise_()#Aca mostramos la ventana si ya existe

        else:

            global ContEnsayo

            pozo = ContEnsayo.dominio.obtenerPozoBombeo()

            if len(ContEnsayo.dominio.listaPozo) < 1:

                #print 'No hay ningun pozo'
                QtGui.QMessageBox.information(self,
                    "Error",
                    "No hay ningun pozo")

            else:

                if pozo != None:

                    if len(pozo.ensayos) > 0:

                        poz = ContEnsayo.dominio.obtenerPozoObservacion()

                        ##formulario de discretizacion temporal
                        frmDiscretizaciones=QtGui.QDialog()
                        ui= discretizaciones.ventanaDiscretizaciones()
                        ui.setupUi(frmDiscretizaciones, ContEnsayo)
                        frmDiscretizaciones.exec_()

                        self.dia = QtGui.QDialog()
                        hbox1 = QtGui.QHBoxLayout()
                        self.dia.setGeometry(QtCore.QRect(500, 50, 200, 50))
                        msgLabel = QtGui.QLabel(QtCore.QString(u'Generando gráficas, espere un momento...'))
                        hbox1.addWidget(msgLabel)
                        self.dia.setLayout(hbox1)
                        self.dia.setWindowTitle(QtCore.QString(u'Calculando...'))
                        self.dia.setModal(True)
                        self.dia.show()

                        #print 'Formulario de discretizaciones se cerro ' 
                        nix, niy, ti, tf, nit, tfo=ContEnsayo.devolverValoresDiscretizaciones()
                        X, Y,xx, yy, tiempos,tiemposobs, dt, tipodis=ContEnsayo.devolverDiscretizaciones()

                        self.dibujante = dibujante(self, ContEnsayo.obtenerDominio(), tipodis, X,Y, xx, yy,nix,niy, tiempos,tiemposobs, ti, tf, dt, self.dia)#Hay que pasarle la ventana principal
                        self.dibujante.show()
                        QtCore.QObject.connect(self.dibujante, QtCore.SIGNAL(_fromUtf8("destroyed()")), self.limpiarDibujante)
                        #print 'Dibujante invocado'

                        if self.dia!=None:
                            self.dia.close()
                            self.dia = None

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

    def GraficasOptimizacion(self):

        if self.grop != None:

            #print u'Ya hay una instancia corriendo'
            self.frm.raise_()#Aca mostramos la ventana si ya existe

        else:

            global ContEnsayo
            pozo = ContEnsayo.dominio.obtenerPozoBombeo()

            if len(ContEnsayo.dominio.listaPozo) < 1:

                QtGui.QMessageBox.information(self,
                    "Error",
                    "No hay ningun pozo")
            else:

                if pozo != None:

                    if len(pozo.ensayos) > 0:

                        poz = ContEnsayo.dominio.obtenerPozoObservacion()

                        if len(poz.observaciones) > 0:

                            ##formulario de discretizacion temporal
                            ####aca cambiar todo para mandar al formulario del pozo

                            nix, niy, ti, tf, nit, tfo=ContEnsayo.devolverValoresDiscretizaciones()
                            self.frm=QtGui.QWidget()
                            self.grop = graficarOpt()
                            self.grop.setupUi(self.frm, ContEnsayo.obtenerDominio(), ti, tf,nit)
                            self.frm.show()

                            #print 'Dibujante invocado'

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
        ContEnsayo=controlador.Proyecto()  

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

        #print 'se carga el demo'


    def cargar_demo(self):

        global ContEnsayo
        ContEnsayo=controlador.Proyecto()  
        ContEnsayo.dominio.alto = 1000
        ContEnsayo.dominio.ancho = 1000
        ContEnsayo.dominio.a=0
        ContEnsayo.dominio.b=0
        ContEnsayo.dominio.c=10

        ##Como prueba se elijio el metodo Theis de una, esto ya asocia el metodo al dominio
        m=Theis(ContEnsayo.dominio, ContEnsayo.parametros)
        m.setearValores([1000,0.0001])

        #Adherimos la vista del dominio
        self.ui = UiForm()
        self.ui.setupUi(MainWindow, ContEnsayo, app.desktop().size().width(), app.desktop().size().height())

        b = vistaPozo(QtGui.QPixmap("content/images/blackDotIcon.png"),  "pozo", self.ui.caja.scene())

        b.setX(500)
        b.setY(250)

        b.id = elementoDominio.ContEnsayo.agregarPozo(500, 250) 

        self.ui.caja.botones.append(b)

        poe = vistaPozo(QtGui.QPixmap("content/images/blackDotIcon.png"),  "pozo", self.ui.caja.scene())

        poe.setX(600)
        poe.setY(250)

        poe.id = elementoDominio.ContEnsayo.agregarPozo(600, 250) 

        self.ui.caja.botones.append(poe)

        noexec=1

        self.ventanaImpoObs(noexec)
        self.vimp.archivo="ficheros/demoobs.ods"
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
        asoe.setupUi(frmasociar, poe.id, ContEnsayo)
        asoe.oe=ContEnsayo.observaciones[0]
        asoe.tipo="o"
        asoe.asociar()

        asoe.setupUi(frmasociar, b.id, ContEnsayo)
        asoe.oe=ContEnsayo.ensayos[0]
        asoe.tipo="e"
        asoe.asociar()

        #print 'se carga el demo'

    def cargar_demobarrera1000(self):

        global ContEnsayo
        ContEnsayo=controlador.Proyecto()  

        ContEnsayo.dominio.alto = 1000
        ContEnsayo.dominio.ancho = 1000
        ContEnsayo.dominio.a=0
        ContEnsayo.dominio.b=0
        ContEnsayo.dominio.c=10

        ##Como prueba se elijio el metodo Theis de una, esto ya asocia el metodo al dominio
        m=Theis(ContEnsayo.dominio, ContEnsayo.parametros)
        m.setearValores([1000,0.0001])

        #Adherimos la vista del dominio
        self.ui = UiForm()
        self.ui.setupUi(MainWindow, ContEnsayo, app.desktop().size().width(), app.desktop().size().height())

        b = vistaPozo(QtGui.QPixmap("content/images/blackDotIcon.png"),  "pozo", self.ui.caja.scene())

        b.setX(500)
        b.setY(250)

        b.id = elementoDominio.ContEnsayo.agregarPozo(500, 250)

        self.ui.caja.botones.append(b)

        poe = vistaPozo(QtGui.QPixmap("content/images/blackDotIcon.png"),  "pozo", self.ui.caja.scene())

        poe.setX(750)
        poe.setY(250)

        poe.id = elementoDominio.ContEnsayo.agregarPozo(750, 250) 

        self.ui.caja.botones.append(poe)

        x0=1
        y0=0
        x1=2
        y1=4
        r = QtCore.QLineF(x0, y0, x1, y1)
        barrera = vistaBarrera(x0, y0, x1, y1, "barrera", self.ui.caja.scene())
        barrera.id = ContEnsayo.agregarRecta("positivo", x0, y0, x1, y1, ContEnsayo.dominio.alto, ContEnsayo.dominio.ancho)
        self.ui.caja.rectas.append(barrera)

        poz2 = vistaPozo(QtGui.QPixmap("content/images/blackDotIcon.png"),  "pozo", self.ui.caja.scene())

        poz2.setX(250)
        poz2.setY(100)

        poz2.id = elementoDominio.ContEnsayo.agregarPozo(250, 100) 

        self.ui.caja.botones.append(poz2)

        pobs2 = vistaPozo(QtGui.QPixmap("content/images/blackDotIcon.png"),  "pozo", self.ui.caja.scene())

        pobs2.setX(500)
        pobs2.setY(500)

        pobs2.id = elementoDominio.ContEnsayo.agregarPozo(500, 500)

        self.ui.caja.botones.append(pobs2)

        noexec=1

        self.ventanaImpoObs(noexec, True)
        self.vimp.archivo="ficheros/observaciones.txt"
        self.vimp.nombre.setText('obs1')
        self.vimp.ext="txt"
        self.vimp.accionaceptar()
        self.vimp.close()

        self.ventanaImpoObs(noexec, True)
        self.vimp.archivo="ficheros/demoobs.ods"
        self.vimp.nombre.setText('obs2')
        self.vimp.ext="ods"
        self.vimp.accionaceptar()
        self.vimp.close()

        self.ventanaImportarProyecto(noexec, True)
        self.importar.archivo="ficheros/demo1pozo.ods"
        self.importar.nombre.setText('ens1')
        self.importar.ext="ods"
        self.importar.accionaceptar()
        self.importar.close()

        self.ventanaImportarProyecto(noexec, True)
        self.importar.archivo="ficheros/demo2pozo.ods"
        self.importar.nombre.setText('ens2')
        self.importar.ext="ods"
        self.importar.accionaceptar()
        self.importar.close()

        frmasociar=QtGui.QDialog()
        asoe=asociarEnsayos.Ui_Dialog()
        asoe.setupUi(frmasociar, poe.id, ContEnsayo, True)
        asoe.oe=ContEnsayo.observaciones[0]
        asoe.tipo="o"
        asoe.asociar()

        asoe.setupUi(frmasociar, pobs2.id, ContEnsayo, True)
        asoe.oe=ContEnsayo.observaciones[0]
        asoe.tipo="o"
        asoe.asociar()

        asoe.setupUi(frmasociar, b.id, ContEnsayo, True)
        asoe.oe=ContEnsayo.ensayos[0]
        asoe.tipo="e"
        asoe.asociar()

        asoe.setupUi(frmasociar, poz2.id, ContEnsayo, True)
        asoe.oe=ContEnsayo.ensayos[0]
        asoe.tipo="e"
        asoe.asociar()

        #print 'se carga el demo'

    def cargar_demoNumerico(self):

        global ContEnsayo
        ContEnsayo=controlador.Proyecto()  

        ContEnsayo.dominio.alto = 3000
        ContEnsayo.dominio.ancho = 3000

        ContEnsayo.dominio.a=0
        ContEnsayo.dominio.b=0
        ContEnsayo.dominio.c=10

        ##Como prueba se elijio el metodo Theis de una, esto ya asocia el metodo al dominio
        m=DiferenciaFinita(ContEnsayo.dominio, ContEnsayo.parametros, True)
        m.setearValores([850,1.3e-4])
        ContEnsayo.metodo=m

        #Adherimos la vista del dominio
        self.ui = UiForm()
        self.ui.setupUi(MainWindow, ContEnsayo, app.desktop().size().width(), app.desktop().size().height())

        #b = vistaPozo(QtGui.QPixmap("content/images/blackDotIcon.png"),  "pozo", self.ui.caja.scene())
        #b.setX(1500)
        #b.setY(1500)
        #b.id = elementoDominio.ContEnsayo.agregarPozo(1500, 1500)
        #self.ui.caja.botones.append(b)
        b=self.agregarPozo(1500, 1500)

        #pob = vistaPozo(QtGui.QPixmap("content/images/blackDotIcon.png"),  "pozo", self.ui.caja.scene())
        #pob.setX(1600)
        #pob.setY(1500)
        #pob.id = elementoDominio.ContEnsayo.agregarPozo(1600,1500) 
        #self.ui.caja.botones.append(pob)
        pob=self.agregarPozo(1600,1500)

        #pinbi = vistaPozo(QtGui.QPixmap("content/images/blackDotIcon.png"),  "pozo", self.ui.caja.scene())
        #pinbi.setX(250)
        #pinbi.setY(100)
        #pinbi.id = elementoDominio.ContEnsayo.agregarPozo(250, 100) 
        #self.ui.caja.botones.append(pinbi)
##        pinbi=self.agregarPozo(250, 100)

        ##No hay barrera en dif finita
        #x0=250
        #y0=0
        #x1=500
        #y1=1000
        #r = QtCore.QLineF(x0, y0, x1, y1)
        #barrera = vistaBarrera(x0, y0, x1, y1, "barrera", self.ui.caja.scene())
        #barrera.id = ContEnsayo.agregarRecta("positivo", x0, y0, x1, y1, ContEnsayo.dominio.alto, ContEnsayo.dominio.ancho)
        #self.ui.caja.rectas.append(barrera)

        noexec=1

        self.ventanaImpoObs(noexec, True)
        #self.vimp.archivo="ficheros/obsTheiscnbarrera.ods"
        self.vimp.archivo="ficheros/obsdiferenciaf.ods"
        self.vimp.nombre.setText('obs1')
        self.vimp.ext="ods"
        self.vimp.accionaceptar()
        self.vimp.close()

        self.ventanaImportarProyecto(noexec, True)
        self.importar.archivo="ficheros/bombeos.txt"
        self.importar.nombre.setText('ens1')
        self.importar.ext="txt"
        self.importar.accionaceptar()
        self.importar.close()

##        self.ventanaImportarProyecto(noexec, True)
##        self.importar.archivo="ficheros/demo1pozo.ods"
##        self.importar.nombre.setText('ens2')
###        self.importar.ext="ods"
##        self.importar.accionaceptar()
###        self.importar.close()

        frmasociar=QtGui.QDialog()
        asoe=asociarEnsayos.Ui_Dialog()
        asoe.setupUi(frmasociar, b.id, ContEnsayo, True)
        asoe.oe=ContEnsayo.ensayos[0]
        asoe.tipo="e"
        asoe.asociar()

        asoe.setupUi(frmasociar, pob.id, ContEnsayo, True)
        asoe.oe=ContEnsayo.observaciones[0]
        asoe.tipo="o"
        asoe.asociar()

##        asoe.setupUi(frmasociar, pinbi.id, ContEnsayo, True)
##        asoe.oe=ContEnsayo.ensayos[0]
##        asoe.tipo="e"
##        asoe.asociar()

        #print 'se carga el demo'

    def cargar_demobarrera1000hantush(self):

        global ContEnsayo
        ContEnsayo=controlador.Proyecto()  

        ContEnsayo.dominio.alto = 1000
        ContEnsayo.dominio.ancho = 1000

        ContEnsayo.dominio.a=0
        ContEnsayo.dominio.b=0
        ContEnsayo.dominio.c=10

        ##Como prueba se elijio el metodo Theis de una, esto ya asocia el metodo al dominio
        m=Hantush(ContEnsayo.dominio, ContEnsayo.parametros, True) 

        #m=Theis(ContEnsayo.dominio, ContEnsayo.parametros, True)
        m.setearValores([1000,1.e-4,676.7])
        #m.setearValores([700,1.1e-4])

        #print "c ",ContEnsayo.metodo.dominio.c
        ContEnsayo.metodo=m

        #Adherimos la vista del dominio
        self.ui = UiForm()
        self.ui.setupUi(MainWindow, ContEnsayo, app.desktop().size().width(), app.desktop().size().height())

        #b = vistaPozo(QtGui.QPixmap("content/images/blackDotIcon.png"),  "pozo", self.ui.caja.scene())
        #b.setX(500)
        #b.setY(250)
        #b.id = elementoDominio.ContEnsayo.agregarPozo(500, 250)
        #self.ui.caja.botones.append(b)
        b=self.agregarPozo(500, 250)

        #pob = vistaPozo(QtGui.QPixmap("content/images/blackDotIcon.png"),  "pozo", self.ui.caja.scene())
        #pob.setX(600)
        #pob.setY(250)
        #pob.id = elementoDominio.ContEnsayo.agregarPozo(600, 250)
        #self.ui.caja.botones.append(pob)
        pob=self.agregarPozo(600, 250)

        x0=250
        y0=0
        x1=500
        y1=1000
        #r = QtCore.QLineF(x0, y0, x1, y1)
        #barrera = vistaBarrera(x0, y0, x1, y1, "barrera", self.ui.caja.scene())
        #barrera.id = ContEnsayo.agregarRecta("positivo", x0, y0, x1, y1, ContEnsayo.dominio.alto, ContEnsayo.dominio.ancho)
        #self.ui.caja.rectas.append(barrera)
        #barrera=self.agregarRecta(x0, y0, x1, y1, "positivo")

        noexec=1

        self.ventanaImpoObs(noexec, True)
        #self.vimp.archivo="ficheros/obsTheiscnbarrera.ods"
        self.vimp.archivo="ficheros/obsHantush.ods"
        self.vimp.nombre.setText('obs1')
        self.vimp.ext="ods"
        self.vimp.accionaceptar()
        self.vimp.close()

        self.ventanaImportarProyecto(noexec, True)
        #self.importar.archivo="ficheros/bombeos.txt"
        self.importar.archivo="ficheros/haintush.txt"

        self.importar.nombre.setText('ens1')
        self.importar.ext="txt"
        self.importar.accionaceptar()
        self.importar.close()

        frmasociar=QtGui.QDialog()
        asoe=asociarEnsayos.Ui_Dialog()
        asoe.setupUi(frmasociar, b.id, ContEnsayo, True)
        asoe.oe=ContEnsayo.ensayos[0]
        asoe.tipo="e"
        asoe.asociar()

        asoe.setupUi(frmasociar, pob.id, ContEnsayo, True)
        asoe.oe=ContEnsayo.observaciones[0]
        asoe.tipo="o"
        asoe.asociar()

        #print 'se carga el demo'

    def agregarPozo(self,x,y):

        b = vistaPozo(QtGui.QPixmap("content/images/blackDotIcon.png"), "pozo", self.ui.caja.scene())
        b.id = ContEnsayo.agregarPozo(np.int(x), np.int(y))
        self.ui.caja.transformarCoordenada(QtCore.QPoint(np.int32(x), np.int32(y)))

        if np.int32(x) == 0:

            b.setX(0 - 5)

        else:

            b.setX(self.ui.caja.a1 - 15)

        if np.int32(y) == 0:

            b.setY(self.ui.caja.alto - 10)

        else:

            b.setY(self.ui.caja.a2 - 10)

        self.ui.caja.botones.append(b)
        return b

    def agregarRecta(self,x1,y1,x2,y2,tipo):

        #print "x no se q ",self.ui.caja.ejeEscena.x()
        #print "y no se q ",self.ui.caja.ejeEscena.y()

        ident = ContEnsayo.agregarRecta(tipo, np.int32(x1), self.ui.caja.ejeEscena.y() - np.int32(y1),
            np.int32(x2), self.ui.caja.ejeEscena.y() - np.int32(y2),
            self.ui.caja.alto, self.ui.caja.ancho)

        r = ContEnsayo.buscarRecta(ident)
        barrera = vistaBarrera(r.x1, r.y1, r.x2, r.y2, "barrera", self.ui.caja.scene())
        barrera.id = ident
        self.ui.caja.rectas.append(barrera)

        #print "cordenadas reales como quedaron ",x1,y1,x2,y2
        #print "cordenadas de la recta ",r.x1, r.y1, r.x2, r.y2

        r.setearCoef(x1, x2, y1, y2)
        return barrera

    def cargar_demobarrera1000theis(self):

        global ContEnsayo
        ContEnsayo=controlador.Proyecto()  

        ContEnsayo.dominio.alto = 3000
        ContEnsayo.dominio.ancho = 3000

        ContEnsayo.dominio.a=0
        ContEnsayo.dominio.b=0
        ContEnsayo.dominio.c=10

        ##Como prueba se elijio el metodo Theis de una, esto ya asocia el metodo al dominio
        #m=Hantush(ContEnsayo.dominio, ContEnsayo.parametros, True) 
        m=Theis(ContEnsayo.dominio, ContEnsayo.parametros, True)
        #m.setearValores([1000,1.e-4,676.7])
        m.setearValores([1000,1.e-4])

        #print "c ",ContEnsayo.metodo.dominio.c
        ContEnsayo.metodo=m

        #Adherimos la vista del dominio
        self.ui = UiForm()
        self.ui.setupUi(MainWindow, ContEnsayo, app.desktop().size().width(), app.desktop().size().height())

        #b = vistaPozo(QtGui.QPixmap("content/images/blackDotIcon.png"),  "pozo", self.ui.caja.scene())
        #b.setX(500)
        #b.setY(750)
        #b.id = elementoDominio.ContEnsayo.agregarPozo(500, 250) 
        #self.ui.caja.botones.append(b)
        b=self.agregarPozo(1500, 1500) 

        #pob = vistaPozo(QtGui.QPixmap("content/images/blackDotIcon.png"),  "pozo", self.ui.caja.scene())
        #pob.setX(600)
        #pob.setY(750)
        #pob.id = elementoDominio.ContEnsayo.agregarPozo(600, 250)
        #self.ui.caja.botones.append(pob)
        pob=self.agregarPozo(1600, 1500)

        x0=1200
        y0=550
        x1=1300
        y1=950

        #r = QtCore.QLineF(x0, y0, x1, y1)
        #barrera = vistaBarrera(x0, y0, x1, y1, "barrera", self.ui.caja.scene())
        #barrera.id = ContEnsayo.agregarRecta("positivo", x0, y0, x1, y1, ContEnsayo.dominio.alto, ContEnsayo.dominio.ancho)
        #self.ui.caja.rectas.append(barrera)

        barrera=self.agregarRecta(x0, y0, x1, y1, "Positivo")

        noexec=1

        self.ventanaImpoObs(noexec, True)
        self.vimp.archivo="ficheros/obsTheiscnbarrera.ods"
        #self.vimp.archivo="ficheros/obsHantush.ods"
        self.vimp.nombre.setText('obs1')
        self.vimp.ext="ods"
        self.vimp.accionaceptar()
        self.vimp.close()

        self.ventanaImportarProyecto(noexec, True)
        self.importar.archivo="ficheros/bombeos.txt"
        #self.importar.archivo="ficheros/haintush.txt"
        self.importar.nombre.setText('ens1')
        self.importar.ext="txt"
        self.importar.accionaceptar()
        self.importar.close()
 
        frmasociar=QtGui.QDialog()
        asoe=asociarEnsayos.Ui_Dialog()
        asoe.setupUi(frmasociar, b.id, ContEnsayo, True)
        asoe.oe=ContEnsayo.ensayos[0]
        asoe.tipo="e"
        asoe.asociar()

        asoe.setupUi(frmasociar, pob.id, ContEnsayo, True)
        asoe.oe=ContEnsayo.observaciones[0]
        asoe.tipo="o"
        asoe.asociar()

        #print 'se carga el demo'

    def cargar_demobarrera(self):

        global ContEnsayo
        ContEnsayo=controlador.Proyecto()  

        ContEnsayo.dominio.alto = 10
        ContEnsayo.dominio.ancho = 10
        ContEnsayo.dominio.a=0
        ContEnsayo.dominio.b=0
        ContEnsayo.dominio.c=10
        ##Como prueba se elijio el metodo Theis de una, esto ya asocia el metodo al dominio
        m=Theis(ContEnsayo.dominio, ContEnsayo.parametros)
        m.setearValores([1000,0.0001])
        ContEnsayo.metodo=m 
        #Adherimos la vista del dominio
        self.ui = UiForm()

        self.ui.setupUi(MainWindow, ContEnsayo, app.desktop().size().width(), app.desktop().size().height())

        b = vistaPozo(QtGui.QPixmap("content/images/blackDotIcon.png"),  "pozo", self.ui.caja.scene())

        b.setX(5)
        b.setY(2.5)

        b.id = elementoDominio.ContEnsayo.agregarPozo(5, 2.5)

        self.ui.caja.botones.append(b)

        x0=1
        y0=0
        x1=2
        y1=4
        r = QtCore.QLineF(x0, y0, x1, y1)
        ContEnsayo.agregarRecta("positivo", x0, y0, x1, y1)

        poz2 = vistaPozo(QtGui.QPixmap("content/images/blackDotIcon.png"),  "pozo", self.ui.caja.scene())

        poz2.setX(2.5)
        poz2.setY(1)

        poz2.id = elementoDominio.ContEnsayo.agregarPozo(2.5, 1)

        self.ui.caja.botones.append(poz2)

        poe = vistaPozo(QtGui.QPixmap("content/images/blackDotIcon.png"),  "pozo", self.ui.caja.scene())

        poe.setX(7.5)
        poe.setY(2.5)

        poe.id = elementoDominio.ContEnsayo.agregarPozo(7.5, 2.5)

        self.ui.caja.botones.append(poe)

        pobs2 = vistaPozo(QtGui.QPixmap("content/images/blackDotIcon.png"),  "pozo", self.ui.caja.scene())

        pobs2.setX(5)
        pobs2.setY(5)

        pobs2.id = elementoDominio.ContEnsayo.agregarPozo(5, 5) 

        self.ui.caja.botones.append(pobs2)

        noexec=1

        self.ventanaImpoObs(noexec)
##        self.vimp.archivo="ficheros/demoobs.ods"
        self.vimp.archivo="ficheros/observaciones.txt"
        self.vimp.nombre.setText('obs1')
        self.vimp.ext="txt"
        self.vimp.accionaceptar()
        self.vimp.close()

        self.ventanaImpoObs(noexec)
        self.vimp.archivo="ficheros/demoobs.ods"
        self.vimp.nombre.setText('obs2')
        self.vimp.ext="ods"
        self.vimp.accionaceptar()
        self.vimp.close()

        self.ventanaImportarProyecto(noexec)
        self.importar.archivo="ficheros/demo1pozo.ods"
        self.importar.nombre.setText('ens1')
        self.importar.ext="ods"
        self.importar.accionaceptar()
        self.importar.close()

        self.ventanaImportarProyecto(noexec)
        self.importar.archivo="ficheros/demo2pozo.ods"
        self.importar.nombre.setText('ens1')
        self.importar.ext="ods"
        self.importar.accionaceptar()
        self.importar.close()

        frmasociar=QtGui.QDialog()
        asoe=asociarEnsayos.Ui_Dialog()
        asoe.setupUi(frmasociar, poe.id, ContEnsayo)
        asoe.oe=ContEnsayo.observaciones[0]
        asoe.tipo="o"
        asoe.asociar()

        asoe.setupUi(frmasociar, pobs2.id, ContEnsayo)
        asoe.oe=ContEnsayo.observaciones[0]
        asoe.tipo="o"
        asoe.asociar()

        asoe.setupUi(frmasociar, b.id, ContEnsayo)
        asoe.oe=ContEnsayo.ensayos[0]
        asoe.tipo="e"
        asoe.asociar()

        asoe.setupUi(frmasociar, poz2.id, ContEnsayo)
        asoe.oe=ContEnsayo.ensayos[0]
        asoe.tipo="e"
        asoe.asociar()

    def acercaDe(self):
        dialogoAcerca = QtGui.QDialog(self)
        dialogoAcerca.setWindowTitle("Acerca de...")
        dialogoAcerca.setGeometry(QtCore.QRect(320, 127, 500, 335))
        etiqueta = QtGui.QLabel(dialogoAcerca)
        etiqueta.setStyleSheet("color: black")
        etiqueta.setText("tiponpython Desarrollado por: \n\n        *Mathias Chubrega \n\n        *Alvaro Correa \n\n        *Jesus Guibert \n\n        *Sebastian Daloia \n\n        *Andres Pias\n\ntiponpython 1.0 es software libre: Tu puedes distribuirlo \ny/o modficarlo de acuerdo a los terminos de GNU\nGeneral Public License, publicada por la Free Software Foundation, \ntanto en su tercera version como en versiones anteriores.\ntiponpythos es distribuido con la esperanza de que sera de utilidad\npero sin ninguna garantia de ello. Sin siquiera la garantia implicita \nde mercantibilidad o de idoneidad para cualquier negocio.")
        dialogoAcerca.show()

if __name__ == "__main__":

    import sys
    app = QtGui.QApplication(sys.argv)

    app.setStyleSheet("QLineEdit{color: blue} \n"
                      "QLabel{color: red} \n"
                      "QPushButton{color: navy}")

    # Get the locale settings
    locale = unicode(QtCore.QLocale.system().name())
    # This is to make Qt use locale configuration; i.e. Standard Buttons
    # in your system's language.
    qtTranslator=QtCore.QTranslator()
    qtTranslator.load("qt_" + locale,
                    "idiomas"
                    )
    print "archivo idioma  qt_", locale
    #print "ruta idioma ",QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath)

    #QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath)

    app.installTranslator(qtTranslator)

    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
