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
import controlador
import NuevoProyecto
import ingresarCaudal
import importarObservaciones
import ingresarObservaciones
import verObservaciones
from vistaDominio import  *
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
        self.actionGenerar_graficas2.setText(QtGui.QApplication.translate("MainWindow", u"Generar gráficas2", None, QtGui.QApplication.UnicodeUTF8))
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
        QtCore.QObject.connect(self.actionGenerar_graficas2, QtCore.SIGNAL(_fromUtf8("triggered()")), self.generar_graficas2)
        QtCore.QObject.connect(self.actionGenerar_video, QtCore.SIGNAL(_fromUtf8("triggered()")), self.generar_video)

        QtCore.QObject.connect(self.menuCaudal_de_bombeo, QtCore.SIGNAL(_fromUtf8("hovered()")), self.despliegueCaudal)
        QtCore.QObject.connect(self.menuObservaciones, QtCore.SIGNAL(_fromUtf8("hovered()")), self.despligueObservacion)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Adherimos la vista del dominio
        self.ui = Ui_Form()
        self.ui.setupUi(MainWindow, ContEnsayo)

    def retranslateUi(self, MainWindow):
        pass

    def despliegueCaudal(self):
        print "abre caudal"

    def despligueObservacion(self):
        print "abre observaciones"

    def ventanaNuevoProyecto(self):
        frmNuevoProyecto = QtGui.QDialog()
        ui = NuevoProyecto.Ui_frmNuevoProyecto()
        ui.setupUi(frmNuevoProyecto,ContEnsayo)
        frmNuevoProyecto.exec_()

    def ventanaImportarProyecto(self):
        global ContEnsayo
        frmImpCaudal = QtGui.QDialog()
        ui = importarCaudal.Ui_Dialog()
        ## Se envia al nuevo formulario el controlador instanciado
        ui.setupUi(frmImpCaudal, ContEnsayo)
        self.importar=frmImpCaudal
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

    def ventanaImpoObs(self):
        global ContEnsayo
        frmimpobs=QtGui.QDialog()
        ui= importarObservaciones.Ui_Dialog()
        ui.setupUi(frmimpobs, ContEnsayo)
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

        else:

            ran = random.randint(10, 30)
            print 'ran: ' + str(ran)
            zcol = []

            for i in range(0, ran):
                z = np.random.multivariate_normal((1, 1), [[ran, 0], [0, ran]], ran).T
                z = z**2
                zcol.append(z)

            matrix = [np.arange(0, ran), zcol]
            print '<Matrix>\n' + str(matrix) + '\n</Matrix>'
            self.dibujante = dibujante(self, matrix)#Hay que pasarle la ventana principal
            self.dibujante.show()
            QtCore.QObject.connect(self.dibujante, QtCore.SIGNAL(_fromUtf8("destroyed()")), self.limpiarDibujante)
            print 'Dibujante invocado'


    def generar_graficas2(self):
        global ContEnsayo
        self.dibujante2 = dibujante2(self, ContEnsayo)#Hay que pasarle la ventana principal
        self.dibujante2.show()
        print 'Dibujante invocado'
            

    def limpiarDibujante(self):

        self.dibujante = None

    def generar_video(self):

        print u'Próximamente se exportará un video con esta opción'

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setStartDragDistance(10)
    app.setStyleSheet("QGroupBox{color: green} \n"
                      "QLineEdit{color: blue} \n"
                      "QLabel{color: red} \n"
                      "QPushButton{color: navy}")
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
