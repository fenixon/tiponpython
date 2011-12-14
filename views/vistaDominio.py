# -*- coding: cp1252 -*-
"""
Esta es la vista que definira la GUI del dominio.
Con sus clases, y codigo auxiliar.

Creado por TIPONPYTHON Cooperative

"""

from PyQt4 import QtCore, QtGui
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


"""
La clase elemento dominio contiene código auxiliar. Es una clase
de caracter global.

Sus atributos, a modo de banderas, van a ser aprovechados por las
instancias de la clases boton y box.

Los valores por defecto de estos atributos son

elementoDominio = 0
existe = False
idElemento = 1000

---

Descripcion de elementoDominio

Es una bandera de control, que le dice a la aplicacion que tipo de
elemento se esta arrastrando al dominio para ser creado.

Valores de los elementos actuals

elementoDominio = 0

Es usado para insertar un pozo

elementoDominio = 1

Es usado para insertar una barrera

elementoDominio es cambiado en la funcion mouseMoveEvent de la clase
boton, mientras que es evaluado en la funcion dropEvent de la clase
box.

---

Descripcion de existe

Es una bandera de control binaria que le dice a la aplicacion si el
elemento que esta siendo arrastrado, sobre el dominio, es un nuevo
elemento a crear o si es un elemento que ya existe en el dominio y solo
requiere una nueva ubicacion.

Esta bifurcacion es necesaria para saber si el elemento debe de ser creado
o modificado.

existe es cambiado en la funcion mouseMoveEvent de la clase boton, mientras
que es evaluado en la funcion dropEvent de la clase box.

---

Descripcion de idElemento

Es una bandera de control que le dice a la aplicacion cual es el elemento,
dentro de la lista de elementos, que esta siendo arrastrado sobre
el dominio. Se guarda el identificador del elemento.

idElemento es cambiado en la funcion mouseMoveEvent, y es evaluada en
la funcion dropEvent de la clase box.

"""

class elementoDominio(object):

    elementoDominio = 0

    existe = False

    idElemento = 1000

    listaBH = {}

    reloj = False

    transicion = False

    
    
    def __init__(self):
        super(elementoDominio, self).__init__()
        
"""
Clase boton, hereda de QPushButton elemento del modulo QtGui
basicamente es un boton para presionar y generar acciones.

Contiene una referencia al elemento global elementoDominio.
Por defecto el identificador de toda instancia es 1000

"""
class boton(QtGui.QPushButton):

    global elementoDominio

    id = 1000

    posicion = 0
     
    def __init__(self, icono, texto, padre, tooltip):
        super(boton, self).__init__(icono, texto, padre)
        self.init(tooltip)
        
         

    def init(self, tooltip):

        #Seteo inicial del boton
        self.setAcceptDrops(True)        
        self.tooltip = tooltip       
        self.setGeometry(QtCore.QRect(50, 20, 41, 23))
        self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.setMouseTracking(True)
        self.setToolTip(QtGui.QApplication.translate("Form", tooltip, None, QtGui.QApplication.UnicodeUTF8))
        self.setStyleSheet(_fromUtf8("margin 3px;\n"
                                    "border-top-color: rgb(255, 0, 0);\n"
                                    "border-left-color: rgb(255, 0, 0);\n"
                                    "border-bottom-color: rgb(255, 0, 0);\n"
                                    "border-right-color: rgb(255, 0, 0);"))

    def mousePressEvent(self, e):
        if elementoDominio.reloj == False:
            reloj = QtCore.QTimer()
            reloj.singleShot(800, self.apagar)
            elementoDominio.transicion = True
            elementoDominio.reloj = True
        
    def mouseMoveEvent(self, e):        
        if elementoDominio.reloj == True and elementoDominio.transicion == False:            
            print "ahora pasop por el otro"        
            mimedata = QtCore.QMimeData()                             
            drag = QtGui.QDrag(self)

            #Sentencia que representa en el margen superior
            #izquierdo del mouse al elemento que esta siendo
            #arrastrado por la ventana.
            
            if self.tooltip == "pozo":
                pixmap = QtGui.QPixmap("content/images/DotIcon.png")                                    
                drag.setPixmap(pixmap)
                elementoDominio.elementoDominio = 0                
            else:
                pixmap = QtGui.QPixmap("content/images/barrera.png")                                    
                drag.setPixmap(pixmap)
                elementoDominio.elementoDominio = 1


            #Como se describiese en la enunciacion de la clase elementoDominio
            # se evalua si el elemento es nuevo o ya existe en el dominio.
            #dependiendo de la evaluacion el atrinuto existe sera verdadero o falso
            
            if self.id == 1000 or self.id == 1001:           
                elementoDominio.existe = False
                print (elementoDominio.listaBH['pozo'] - e.pos()).manhattanLength()           
            else:
                elementoDominio.existe = True

                
            elementoDominio.idElemento = self.id

            drag.setMimeData(mimedata)
            drag.setHotSpot(e.pos() - self.rect().topLeft())
            dropAction = drag.start(QtCore.Qt.MoveAction)

    def apagar(self):
        print "se ha apagado"
        elementoDominio.transicion = False

    def mouseReleaseEvent(self, e):
        elementoDominio.transicion = False
        elementoDominio.reloj = False
        
         
    
#Definimos clase que agrupa elementos, junto con la sobreescritura
#de los eventos dragEnterEvent y dropEvent para manejar arrastre y tirada
#sobre el elemento
        
class box(QtGui.QGroupBox):

    global elementoDominio

    global boton

    id = 0
   
    def __init__(self, padre):
        super(box, self).__init__(padre)
        self.init()

    def init(self):

        self.setAcceptDrops(True)       
        self.setGeometry(QtCore.QRect(20, 27, 231, 271))
        
        self.setStyleSheet(_fromUtf8("color: rgb(85, 170, 0);\n"
                                    "background-color: rgb(0, 255, 127);"))
               
        self.setTitle(QtGui.QApplication.translate("Form", "Dominio", None, QtGui.QApplication.UnicodeUTF8))
        self.setObjectName(_fromUtf8("Dominio"))

        self.botones = []

        
    #Sobreescribimos dragEnterEvent para pemitir
    #la accion de este evento.
    def dragEnterEvent(self, e):
        e.accept()
                
    #Evento que es llamado cuando se suelta un elemento
    #dentro del groupbox
    def dropEvent(self, e):
        elementoDominio.reloj = False
        #Obtenemos la posicion relativa del lugar en que el
        #elemento es soltado
        position = e.pos()       

        #Si el elemento no existe creamos uno nuevo, en caso contrario
        #arrastramos el elemento ya existente a una nueva posicion en el
        #dominio.
        if elementoDominio.existe == False:
           
            b = ""        
                    
            if elementoDominio.elementoDominio == 0:        
                b = boton(QtGui.QIcon("content/images/DotIcon.png"), "", self, "pozo")
            else:
                b = boton(QtGui.QIcon("content/images/barrera.png"), "", self, "barrera")
            
            b.setGeometry(QtCore.QRect(position.x(), position.y(), 24, 24))

            b.id = len(self.botones)
                    
            self.botones.append(b)

            b.show()           


        else:
            for x in self.botones:
                if x.id == elementoDominio.idElemento:
                    x.move(position)

        e.setDropAction(QtCore.Qt.MoveAction)
        e.accept()
        

"""
La clase Ui_Form es invocada en el archivo principal de la aplicacion.
su funcion es agregar los elementos correspondientes a la vista de
crear dominio
"""

class Ui_Form(object):

    def setupUi(self, Form):
        
        """
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(552, 460)
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        Form.setStyleSheet(_fromUtf8("QtGui.QPushButton{margin: 8px;}"))
        """

        
        #Seteo del formulario que contendra todos los widgets del dominio
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(100, 40, 471, 351))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame.setEnabled(True)


        #Caja de elementos especifica del dominio
        self.Dominio = box(self.frame)

        
        self.groupBox = QtGui.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(260, 20, 151, 81))
        self.groupBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.groupBox.setStyleSheet(_fromUtf8("border-color: rgb(255, 85, 0);\n"))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Barra Herramientas", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
            
        #Creacion de botones de la barra de herramientas
        self.pozo = boton(QtGui.QIcon("content/images/DotIcon.png"), "", self.groupBox, "pozo")
        
        elementoDominio.listaBH['pozo'] = QtCore.QPoint(self.pozo.pos())

        self.barrera = boton(QtGui.QIcon("content/images/barrera.png"), "", self.groupBox, "barrera")

        self.barrera.setGeometry(QtCore.QRect(50, 50, 41, 20))
        self.barrera.id = 1001
        
        elementoDominio.listaBH['barrera'] = QtCore.QPoint(self.barrera.pos())

        self.groupBox_2 = QtGui.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(260, 110, 151, 181))
        self.groupBox_2.setStyleSheet(_fromUtf8("border-color: rgb(0, 0, 255);"))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Coordenadas", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))

        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label.setText(QtGui.QApplication.translate("Form", "Recta Pozo", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))

        self.lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(40, 50, 61, 20))
        self.lineEdit.setStyleSheet(_fromUtf8("border-color: rgb(255, 0, 0);"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 80, 61, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))

        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 110, 61, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))

        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(40, 140, 61, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))

        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 31, 16))
        self.label_2.setStyleSheet(_fromUtf8("border-top-color: rgb(255, 0, 0);\n"
                                    "border-left-color: rgb(255, 0, 0);\n"
                                    "border-bottom-color: rgb(255, 0, 0);\n"
                                    "border-right-color: rgb(255, 0, 0);"))
        self.label_2.setText(QtGui.QApplication.translate("Form", "X1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 21, 16))
        self.label_3.setStyleSheet(_fromUtf8("border-top-color: rgb(255, 0, 0);\n"
                                   "border-left-color: rgb(255, 0, 0);\n"
                                   "border-bottom-color: rgb(255, 0, 0);\n"
                                   "border-right-color: rgb(255, 0, 0);"))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Y1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 21, 20))
        self.label_4.setStyleSheet(_fromUtf8("border: 3px; \n"
                                    "border-top-color: rgb(255, 0, 0);\n"
                                    "border-left-color: rgb(255, 0, 0);\n"
                                    "border-bottom-color: rgb(255, 0, 0);\n"
                                    "border-right-color: rgb(255, 0, 0);"))
        self.label_4.setText(QtGui.QApplication.translate("Form", "X2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 21, 20))
        self.label_5.setStyleSheet("border-top-color: rgb(255, 0, 0);\n"
                                    "border-left-color: rgb(255, 0, 0);\n"
                                    "border-bottom-color: rgb(255, 0, 0);\n"
                                    "border-right-color: rgb(255, 0, 0);")
        self.label_5.setText(QtGui.QApplication.translate("Form", "Y2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.spinBox = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox.setGeometry(QtCore.QRect(90, 20, 42, 22))
        self.spinBox.setProperty("value", 1)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))

        """
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        """

        self.frame.show()
        
    def retranslateUi(self, Form):
        pass


    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
