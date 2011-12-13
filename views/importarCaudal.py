# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogo.ui'
#
# Created: Thu Dec 08 19:14:05 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import bombeo
import ensayobombeo
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(QtGui.QDialog):
    def setupUi(self, Dialog, cont):
        ##Se recupera el controlador instanciado en el main
        ##Se usa ContEnsayo(el mismo nombre) para no marear
        ##el nombre del parametro tiene que ser otro sino salta la 3 al ser global y local
        global ContEnsayo
        ContEnsayo=cont
        self.archivo=""
        
        Dialog.setObjectName(_fromUtf8("ImportarCaudalBombeado"))
        Dialog.resize(572, 130)
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Importar Caudal Bombeado", None, QtGui.QApplication.UnicodeUTF8))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 30, 46, 13))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Archivito", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(113, 20, 331, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(460, 20, 75, 23))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Explorar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.aceptar = QtGui.QPushButton(Dialog)
        self.aceptar.setGeometry(QtCore.QRect(200, 70, 75, 23))
        self.aceptar.setText(QtGui.QApplication.translate("Dialog", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.aceptar.setObjectName(_fromUtf8("aceptar"))
        self.cancelar = QtGui.QPushButton(Dialog)
        self.cancelar.setGeometry(QtCore.QRect(290, 70, 75, 23))
        self.cancelar.setText(QtGui.QApplication.translate("Dialog", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelar.setObjectName(_fromUtf8("cancelar"))
        self.guardar=Dialog

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.browse)
        QtCore.QObject.connect(self.aceptar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.accionaceptar)
        QtCore.QObject.connect(self.cancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.accioncancelar) 
        
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        pass

    def browse(self):
        print "navegar"
        self.archivo = QtGui.QFileDialog.getOpenFileName(
                         self,
                         "Elegir un archivo para abrir",
                         "C:\wamp\www\prueba",
                         "Fichero de datos (*.txt *.odg)");
        print self.archivo
        partes=self.archivo.split(".")
        ext=partes[len(partes)-1]
        if ext!="txt" and ext!="odg" :
            self.archivo=""
            self.textEdit.setText("")
            QtGui.QMessageBox.information(self,
                "Informacion",
                "El tipo de archivo ingresado no es correcto")
        else:
            self.textEdit.setText(self.archivo)
            

    def accionaceptar(self):
        print "aceptar"
##      Se abre el archivo
        f=open(self.archivo)
        global ContEnsayo
        
##      contenido=f.read()
##      Lectura del archivo de los bombeos
##      Se dividen las lineas separadas por \n
        contenido=f.readlines()
        bombeos=[]
        idn=0

        print "El id inicial es: " + str(ContEnsayo.traerid())
        
        for linea in contenido:
##          print linea
##          Se separa la linea por el tabulador
            datos=linea.split("\t")
##          Se esa lina tiene dos columnas se procesa si no no
            if (len(datos)>=2):
                t=int(datos[0])
                c=float(datos[1])
                print "tiempo: "+str(t)
                print "caudal: "+str(c)
                b=bombeo.bombeo(t,c)
                bombeos.append(b)

##      Se obtiene el ultimo id de ensayo guardado en el controlador
        idn=ContEnsayo.obtenerIdEns()
##      Se crea un nuevo ensayo de bombeo, con los bombeos y el id
        e=ensayobombeo.ensayobombeo(bombeos, idn)
##      Se agrega el ensayo a la lista de ensayos del controlador
        ContEnsayo.agregarEnsayo(e)                
        print "El nuevo ensayo creado es " + str(ContEnsayo.traerid())
          
        reply = QtGui.QMessageBox.information(self,
                "Informacion",
                "El nuevo ensato de bombeo ha sido almacenado en el sistema")
        if reply == QtGui.QMessageBox.Ok:
            print "OK"
            self.guardar.close()
            
        else:
            print "Escape"
       
 
    def accioncancelar(self):
        print "chau"        

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    frmImpProyecto = QtGui.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(frmImpProyecto)
    frmImpProyecto.show()
    sys.exit(app.exec_())


