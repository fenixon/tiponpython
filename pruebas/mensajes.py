
import sys, os
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_MainWindow(QtGui.QDialog):

    def setupUi(self, MainWindow):
    
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



        self.actionGenerar_graficas2 = QtGui.QAction(MainWindow)
        self.actionGenerar_graficas2.setText(QtGui.QApplication.translate("MainWindow", u"Cargar datos de prueba", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGenerar_graficas2.setObjectName(_fromUtf8("actionGenerar_graficas2"))        

        self.actionGenerar_graficas = QtGui.QAction(MainWindow)
        self.actionGenerar_graficas.setText(QtGui.QApplication.translate("MainWindow", u"Graficar niveles calculados", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGenerar_graficas.setObjectName(_fromUtf8("actionGenerar_graficas"))

        self.actionOptimizacion = QtGui.QAction(MainWindow)
        self.actionOptimizacion.setText(QtGui.QApplication.translate("MainWindow", u"Optimizacion", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOptimizacion.setObjectName(_fromUtf8("actionOptimizacion"))


        self.actionGrafOpt = QtGui.QAction(MainWindow)
        self.actionGrafOpt.setText(QtGui.QApplication.translate("MainWindow", u"Graficar optimizaciones", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGrafOpt.setObjectName(_fromUtf8("actionGrafOpt"))



##        self.actionGenerar_video = QtGui.QAction(MainWindow)
##        self.actionGenerar_video.setText(QtGui.QApplication.translate("MainWindow", "Generar video...", None, QtGui.QApplication.UnicodeUTF8))
##        self.actionGenerar_video.setObjectName(_fromUtf8("actionGenerar_video"))

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
        self.menuDatos.addAction(self.actionGenerar_graficas2)
##        self.menuGraficar.addAction(self.actionGenerar_video)
        self.menuGraficar.addAction(self.actionOptimizacion)
        self.menuGraficar.addAction(self.actionGrafOpt)       

        self.menubar.addAction(self.menuInicio.menuAction())
        self.menubar.addAction(self.menuDatos.menuAction())
        self.menubar.addAction(self.menuGraficar.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
        msj=QtGui.QMessageBox()
        msj.addButton('piin', QtGui.QMessageBox.AcceptRole)
        msj.information(self,'titu', 'holita')

        

    def retranslateUi(self, MainWindow):
        pass

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)

    app.setStyleSheet("QLineEdit{color: blue} \n"
                      "QLabel{color: red} \n"
                      "QPushButton{color: navy}")

    # Get the locale settings
    locale = unicode(QtCore.QLocale.system().name())
    print locale
    # This is to make Qt use locale configuration; i.e. Standard Buttons
    # in your system's language.
    qtTranslator=QtCore.QTranslator()
    qtTranslator.load("qt_" + locale,
                    QtCore.QLibraryInfo.location(
                    QtCore.QLibraryInfo.TranslationsPath)
                    )
    app.installTranslator(qtTranslator)
    

    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
