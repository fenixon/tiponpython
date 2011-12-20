# -*- coding: cp1252 -*-
"""
Esta es la vista que definira la GUI del dominio.
Con sus clases, y codigo auxiliar.

Creado por TIPONPYTHON Cooperative

"""

from PyQt4 import QtCore, QtGui
import sys
import numpy as np

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
-----------

Descripcion de  reloj y transicion

Son banderas de control que le dice a la aplicacion, dependiendo de sus
estados, cuando se puede comenzar a arrastrar un boton.

El estado inicial de estos elementos en cada boton es:

reloj = False
transicion = False

Para cada boton, estas banderas comenzaran a cambiar en el momento en
que se presione el boton. En la funcion mousePressEvent.

El estado luego de este evento es:

reloj = True
transicion = True

La funcion apagar, tiene como cometido liberar el bloqueo del arrastre
seteando los siguientes estados:

reloj = True
transicion = False

En la funcion mouseMoveEvent se encuentra el control necesario de dichos estados.
Para que el usuario pueda arrastrar el boton una vez finalizado el tiempo.

Cuando el usuario suelta el boton en el objeto de la clase box, o cuando presiona
y luego libera el boton el estado es el siguiente:

reloj = False
transicion = False

-----

Descripcion de ConEnsayo

Básicamente se guarda la instancia del controlador global creado en
el archivo principal. Este hace las veces de controlador, por ende las
operaciones con los modelos se hacen delegandole dichas tareas a este.

------

Descripcion de menuMouse

Es una instancia global de la clase menu(QtGui.QListView)

En su funcion de inicio se setean las acciones estaticas, como
salir o eliminar.

la funcion selectionChanged es sobre escrita para identificar cual
ha sido la accion seleccionado por el usuario.

----------------

Descripcion de selectedMenuMouse

Contiene una referencia al tipo de elemento en el dominio sobre el cual
el usuario hubo aplicacdo un click derecho.
selectedMenuMouse es un diccionario que contiene las claves/valor:

Tipo = ['Punto' | 'Barrera']
id = Identificador del elemento

Esto permite identificar al elemento del dominio sobe el cual se deben
de efectuar las acciones del menu desplegado.

--------------


"""

class elementoDominio(object):

    elementoDominio = 0

    existe = False

    idElemento = 1000

    reloj = False

    transicion = False

    ContEnsayo = ""

    menuMouse = ""

    selectedMenuMouse = {}

    gbCoord = ""

    Dominio = ""

    #Pozo candidato a ser agregado
    pozoCandidato = ""
    hayPozoCandidato = False

    
    def __init__(self):
        super(elementoDominio, self).__init__()
        

        
"""
Clase boton, hereda de QPushButton elemento del modulo QtGui
basicamente es un boton para presionar y generar acciones.

Contiene una referencia al elemento global elementoDominio.
Por defecto el identificador de toda instancia es 1000

1000 = Boton Pozo
1001 = Boton Recta

"""
class boton(QtGui.QPushButton):

    global elementoDominio

    id = 1000  

    posicion = 0

    accionCoord = {}
    
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
        
       if e.button() == QtCore.Qt.LeftButton:
            
            #Cambiamos el cursor, y luego procedemos a evaluar estado del reloj
            #Si no existe creamos un temporizador, cuando alcanze el tiempo dado
            #el usuario va a poder arrastrar el boton.
            self.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))

            if self.id == 1000:
                elementoDominio.gbCoord.setPozo()
            elif self.id == 1001:
                elementoDominio.gbCoord.setRecta()
            
            if elementoDominio.reloj == False:
                reloj = QtCore.QTimer()
                reloj.singleShot(800, self.apagar)
                elementoDominio.transicion = True
                elementoDominio.reloj = True

       else:
           elementoDominio.selectedMenuMouse["tipo"] = "punto"
           elementoDominio.selectedMenuMouse["id"] = self.id
          
           elementoDominio.menuMouse.move(self.pos())

          
           elementoDominio.menuMouse.show()
           
    def mouseMoveEvent(self, e):
        
        #Evaluacion que se entiende como, 'El usuario puede comenzar a arrastrar el boton'
        if elementoDominio.reloj == True and elementoDominio.transicion == False:
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
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
            else:
                elementoDominio.existe = True

                
            elementoDominio.idElemento = self.id

            drag.setMimeData(mimedata)
            drag.setHotSpot(e.pos() - self.rect().topLeft())
            dropAction = drag.start(QtCore.Qt.MoveAction)

    def apagar(self):
        elementoDominio.transicion = False

    #Cuando se suelta el mouse luego de un arrastre
    #incondicionalmente se setean las banderas globales con los siguientes
    #valores
    def mouseReleaseEvent(self, e):        
        elementoDominio.transicion = False
        elementoDominio.reloj = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))


         
"""    
Definimos clase que agrupa elementos, junto con la sobreescritura
de los eventos dragEnterEvent y dropEvent para manejar arrastre y tirada
sobre el elemento
"""        
class box(QtGui.QGroupBox):

    global elementoDominio

    id = 0
   
    def __init__(self, padre):
        super(box, self).__init__(padre)
        self.init()

    #Propiedades y atributos iniciales del QGroupBox
    def init(self):
        
        self.setAcceptDrops(True)
        self.setMouseTracking(True) 
        self.setGeometry(QtCore.QRect(20, 27, 231, 271))
        self.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 127)"))
        self.setTitle(QtGui.QApplication.translate("Form", "Dominio", None, QtGui.QApplication.UnicodeUTF8))
        self.setObjectName(_fromUtf8("Dominio"))


        self.presionandoRecta = False

        self.idRecta = 1000
        
        self.botones = []

        self.bGiratorios = []
        
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
            if elementoDominio.elementoDominio == 0:        
                b = boton(QtGui.QIcon("content/images/DotIcon.png"), "", self, "pozo")
                b.id = elementoDominio.ContEnsayo.agregarPozo(position.x(), position.y())                
                b.setGeometry(QtCore.QRect(position.x(), position.y(), 24, 24))
                 
                self.botones.append(b)
                b.show()           
            else:
                r = QtCore.QLineF(position.x(), position.y(), (position.x() + 30), (position.y() + 30))
                elementoDominio.ContEnsayo.agregarRecta("Negativo", np.float32(r.x1()), np.float32(r.y1()), np.float32(r.x2()), np.float32(r.y2()))                
        else:
            for x in self.botones:
                if x.id == elementoDominio.idElemento:
                    x.move(position)
                    if x.tooltip == "pozo":
                        elementoDominio.ContEnsayo.moverPozo(x.id, position.x(), position.y())
                        



        elementoDominio.transicion = False
        elementoDominio.reloj = False

        e.setDropAction(QtCore.Qt.MoveAction)
        e.accept()
        
    #Definicion de la funcion para comenzar a dibujar
    def paintEvent(self, e):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setPen(QtCore.Qt.blue)
        painter.setBrush(QtGui.QColor(0, 255, 127))
        painter.setBackground(painter.brush())
        painter.setBackgroundMode(QtCore.Qt.OpaqueMode)
        self.dibujarRectas(painter)
        painter.end()
        
    #Funcion de dibujado de lineas    
    def dibujarRectas(self, painter):
        self.rectas = elementoDominio.ContEnsayo.dibujarRecta()
        for x in self.rectas:  
            painter.drawLine(x.x1, x.y1, x.x2, x.y2)

        

        if elementoDominio.ContEnsayo.hayRectaCandidata():
            #?rc = elementoDominio.ContEnsayo.rectaCandidata
            #painter.drawLine(rc.x1, rc.y1, rc.x2, rc.y2)

            painter.drawLine(elementoDominio.ContEnsayo.rectaCandidata.x1, elementoDominio.ContEnsayo.rectaCandidata.y1,
                             elementoDominio.ContEnsayo.rectaCandidata.x2, elementoDominio.ContEnsayo.rectaCandidata.y2)

        self.update()

    def mouseMoveEvent(self, e):
        #Buscamos si las coordenadas actuales estan cerca de algun punto de alguna recta
        lista = elementoDominio.ContEnsayo.buscarPuntoEnRecta(np.float32(e.pos().x()), np.float32(e.pos().y()))
        
        botonGiratorio = QtGui.QPushButton(self)
        #Si hay puntos entonces cambiamos icono del mouse, y mostramos boton. De lo contrario
        #eliminamos el boton mostrado.
        if  len(lista) > 0:
            if lista['eje'] == "x":
                self.setCursor(QtGui.QCursor(QtCore.Qt.SizeFDiagCursor))
            else:
                self.setCursor(QtGui.QCursor(QtCore.Qt.SizeBDiagCursor))
            botonGiratorio.setGeometry (lista['punto'].x(), lista['punto'].y(), 10, 10)
            self.bGiratorios.append(botonGiratorio)
            botonGiratorio.show()
            self.idRecta = lista['id']
        else:
            if not self.presionandoRecta:
                self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            botonGiratorio.hide()
            self.aEliminar = []
            for x in self.bGiratorios:                
                x.hide()
                self.aEliminar.append(x)

            for x in self.aEliminar:
                try:
                    self.bGiratorios.remove(x)
                    break
                except ValueError:
                    print "Sobrepaso de rangos, advertencia simple"

    def mousePressEvent(self, e):

        if e.button() == QtCore.Qt.RightButton:

            elementoDominio.selectedMenuMouse["tipo"] = "recta"
            elementoDominio.selectedMenuMouse["id"] = 0


            if np.int(self.cursor().shape()) == 8:
                elementoDominio.selectedMenuMouse["id"] = elementoDominio.ContEnsayo.buscarPuntoPorQ(e.pos().x(), e.pos().y())
                 

            if np.int(self.cursor().shape()) == 7:
                elementoDominio.selectedMenuMouse["id"] = elementoDominio.ContEnsayo.buscarPuntoPorR(e.pos().x(), e.pos().y())
                 
            elementoDominio.menuMouse.move(e.pos())                
            elementoDominio.menuMouse.show()

        else:

            #Si el dominio esta comenzado a ser presionado por un cursor que sea
            #utilizado cuando se trabaja con barreras, entonces se setea el atributo
            #self.presionandoRecta a verdadero.
            if np.int(self.cursor().shape()) == 8 or np.int(self.cursor().shape()) == 7:
                self.presionandoRecta = True

    def mouseReleaseEvent(self, e):
        #Dependiendo del tipo de cursos con el que se este modificando la recta
        #se sabra cual es el punto en la misma que hay que modificar
        if e.button() == QtCore.Qt.LeftButton:
            if np.int(self.cursor().shape()) == 8:
                self.presionandoRecta = False
                elementoDominio.ContEnsayo.actualizarRecta(self.idRecta, e.pos().x(), e.pos().y(), "Q")
                self.update()
            if np.int(self.cursor().shape()) == 7:
                self.presionandoRecta = False
                elementoDominio.ContEnsayo.actualizarRecta(self.idRecta, e.pos().x(), e.pos().y(), "R")
                self.update()

"""
Menun utilizado en definir dominio
Brinda opciones de operacion sobre los elementos
cuando se le aplica a los mismos un click derecho
"""
class menu(QtGui.QListView):
    def __init__(self, padre):
        super(menu, self).__init__(padre)
        self.init()

    def init(self):
        #Valores iniciales del menu, incluido el modelo
        self.items = QtCore.QStringList()
        self.items << "MENU" << "Eliminar" << "Salir"    
        modelo = QtGui.QStringListModel(self.items)
        self.setModel(modelo)        
        self.setGeometry(QtCore.QRect(60, 60, 131, 31))
        self.hide()

    def selectionChanged(self, selected,  deselected):
        #indices es un iterador de la lista de QItemSelection que se retorna
        #al momento de una seleccion en la vista.
        #la funcion first del QItemSelection retorna un QModelIndex
        #que es un indice dentro del mapeo del modelo MVC de Qt
        #Los datos son obtenidos a traves de la funcion data, para la secuencial
        #evaluacion.
        
        for indices in selected.first().indexes():
            valor = indices.data()
            if valor.toString() == "Salir":
                self.reset()
                self.hide()
                return
            if valor.toString() == "Eliminar":
                
                if elementoDominio.selectedMenuMouse["tipo"] == "punto":
                    
                    elementoDominio.ContEnsayo.removerPozo(elementoDominio.selectedMenuMouse["id"])

                    self.aEliminar = []
                    
                    for x in self.parent().botones:
                        if x.id == elementoDominio.selectedMenuMouse["id"]:
                            x.hide()
                            self.aEliminar.append(x)

                    for x in self.aEliminar:
                        try:
                            self.parent().botones.remove(x)
                            break
                        except ValueError:
                            print "Punto a eliminar no encontrado, advertencia simple"

                if elementoDominio.selectedMenuMouse["tipo"] == "recta":
                    elementoDominio.ContEnsayo.eliminarRecta(elementoDominio.selectedMenuMouse["id"])
                    self.update()
                    
                elementoDominio.selectedMenuMouse["tipo"] == ""
                elementoDominio.selectedMenuMouse["id"] == -1
                self.reset()
                self.hide()   



"""
Clase que maneja la interfaz de coordenadas
"""
class gbCoordenadas(QtGui.QGroupBox):
    def __init__(self, padre):
        super(gbCoordenadas, self).__init__(padre)
        self.init()

    def init(self):
        self.setGeometry(QtCore.QRect(260, 110, 151, 181))
        self.setTitle("Coordenadas")

        #Etiqueta de Tipo 
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label.setText(QtGui.QApplication.translate("Form", "Recta Pozo", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setVisible(False)

        #X1
        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(40, 50, 25, 20))
        self.lineEdit.setStyleSheet(_fromUtf8("border-color: rgb(255, 0, 0);"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.setVisible(False)

        #Y1
        self.lineEdit_2 = QtGui.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 50, 25, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_2.setVisible(False)

        #X2
        self.lineEdit_3 = QtGui.QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 100, 25, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_3.setVisible(False)

        #Y2
        self.lineEdit_4 = QtGui.QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 100, 25, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_4.setVisible(False)

        #X1
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 25, 20))
        self.label_2.setStyleSheet(_fromUtf8("border-top-color: rgb(255, 0, 0);\n"
                                    "border-left-color: rgb(255, 0, 0);\n"
                                    "border-bottom-color: rgb(255, 0, 0);\n"
                                    "border-right-color: rgb(255, 0, 0);"))
        self.label_2.setText("X1")
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_2.setVisible(False)


        #Y1
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(75, 50, 25, 20))
        self.label_3.setStyleSheet(_fromUtf8("border-top-color: rgb(255, 0, 0);\n"
                                   "border-left-color: rgb(255, 0, 0);\n"
                                   "border-bottom-color: rgb(255, 0, 0);\n"
                                   "border-right-color: rgb(255, 0, 0);"))
        self.label_3.setText("Y1")
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_3.setVisible(False)


        #X2
        self.label_4 = QtGui.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 25, 20))
        self.label_4.setStyleSheet(_fromUtf8("border: 3px; \n"
                                    "border-top-color: rgb(255, 0, 0);\n"
                                    "border-left-color: rgb(255, 0, 0);\n"
                                    "border-bottom-color: rgb(255, 0, 0);\n"
                                    "border-right-color: rgb(255, 0, 0);"))
        self.label_4.setText("X2")
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_4.setVisible(False)

        #Y2
        self.label_5 = QtGui.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(75, 100, 25, 20))
        self.label_5.setStyleSheet("border-top-color: rgb(255, 0, 0);\n"
                                    "border-left-color: rgb(255, 0, 0);\n"
                                    "border-bottom-color: rgb(255, 0, 0);\n"
                                    "border-right-color: rgb(255, 0, 0);")
        self.label_5.setText("Y2")
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_5.setVisible(False)


        #Boton Aceptar
        self.btnAceptar = QtGui.QPushButton(self)
        self.btnAceptar.setGeometry(QtCore.QRect(10, 155, 50, 20))
        self.btnAceptar.setText("Aceptar")
        self.btnAceptar.setVisible(False)
           
        #Boton Cancelar
        self.btnCancelar = QtGui.QPushButton(self)
        self.btnCancelar.setGeometry(QtCore.QRect(80, 155, 50, 20))
        self.btnCancelar.setText("Cancelar")
        self.btnCancelar.setVisible(False)

        #Boton de Vista Previa
        self.btnPrevia = QtGui.QPushButton(self)
        self.btnPrevia.setGeometry(QtCore.QRect(10, 130, 100, 20))
        self.btnPrevia.setText("Vista Previa")
        self.btnPrevia.setVisible(False)


        QtCore.QObject.connect(self.btnAceptar, QtCore.SIGNAL('clicked()'), self.setAceptar)
        QtCore.QObject.connect(self.btnCancelar, QtCore.SIGNAL('clicked()'), self.setCancelar)
        QtCore.QObject.connect(self.btnPrevia, QtCore.SIGNAL('clicked()'), self.setPrevia)

        #Validacion
        self.validador = QtGui.QIntValidator(0, 900, self)

        self.lineEdit.setValidator(self.validador)
        self.lineEdit_2.setValidator(self.validador)
        self.lineEdit_3.setValidator(self.validador)
        self.lineEdit_4.setValidator(self.validador)
        
    def setPozo(self):
        #Etiqueta de Tipo 
        self.label.setText(QtGui.QApplication.translate("Form", "Pozo", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setVisible(True)

        #X1
        self.lineEdit.setText(QtGui.QApplication.translate("Form", "", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setVisible(True)

        #Y1
        self.lineEdit_2.setText(QtGui.QApplication.translate("Form", "", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setVisible(True)

        #X2
        self.lineEdit_3.setVisible(False)

        #Y2
        self.lineEdit_4.setVisible(False)

        #X1
        self.label_2.setVisible(True)


        #Y1
        self.label_3.setVisible(True)


        #X2
        self.label_4.setVisible(False)

        #Y2
        self.label_5.setVisible(False)


        #Boton Aceptar
        self.btnAceptar.setVisible(True)
           
        #Boton Cancelar
        self.btnCancelar.setVisible(True)

        #Vista Previa
        self.btnPrevia.setVisible(True)

    def setRecta(self):
        #Etiqueta de Tipo 
        self.label.setText(QtGui.QApplication.translate("Form", "Recta", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setVisible(True)

        #X1
        self.lineEdit.setText(QtGui.QApplication.translate("Form", "", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setVisible(True)

        #Y1
        self.lineEdit_2.setText(QtGui.QApplication.translate("Form", "", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setVisible(True)

        #X2
        self.lineEdit_3.setText(QtGui.QApplication.translate("Form", "", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_3.setVisible(True)

        #Y2
        self.lineEdit_4.setText(QtGui.QApplication.translate("Form", "", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_4.setVisible(True)

        #X1
        self.label_2.setVisible(True)


        #Y1
        self.label_3.setVisible(True)


        #X2
        self.label_4.setVisible(True)

        #Y2
        self.label_5.setVisible(True)


        #Boton Aceptar
        self.btnAceptar.setVisible(True)
           
        #Boton Cancelar
        self.btnCancelar.setVisible(True)

        #Vista Previa
        self.btnPrevia.setVisible(True)
        
    def setAceptar(self):

        if self.label.text() == "Pozo":

            if self.lineEdit.text() != "" and self.lineEdit_2.text() != "":
                if not elementoDominio.hayPozoCandidato:
                    elementoDominio.pozoCandidato = QtGui.QPushButton(elementoDominio.Dominio)
                    elementoDominio.hayPozoCandidato = True
                    elementoDominio.pozoCandidato.setGeometry(QtCore.QRect(np.int32(self.lineEdit.text()),
                                                                           np.int32(self.lineEdit_2.text()), 25, 20))
                    elementoDominio.pozoCandidato.show()
                            
            
                b = boton(QtGui.QIcon("content/images/DotIcon.png"), "", elementoDominio.Dominio, "pozo")

                b.id = elementoDominio.ContEnsayo.agregarPozo(elementoDominio.pozoCandidato.x(), elementoDominio.pozoCandidato.y())                

                b.setGeometry(QtCore.QRect(elementoDominio.pozoCandidato.x(), elementoDominio.pozoCandidato.y(), 24, 24))
                     
                elementoDominio.Dominio.botones.append(b)

                b.show()
                elementoDominio.pozoCandidato.hide()
                elementoDominio.pozoCandidato = None
                elementoDominio.hayPozoCandidato = False

            

        else:                                   
            if self.lineEdit.text() != "" and self.lineEdit_2.text() != "" and self.lineEdit_3.text()!= "" and self.lineEdit_4.text() != "":
                if not elementoDominio.ContEnsayo.hayRectaCandidata():
                    elementoDominio.ContEnsayo.agregarRecta("Positivo", np.int32(self.lineEdit.text()),
                                                                     np.int32(self.lineEdit_2.text()), np.int32(self.lineEdit_3.text()),
                                                                     np.int32(self.lineEdit_4.text()))
                else:
                    elementoDominio.ContEnsayo.incluirCandidata()
                self.update()

        #Etiqueta de Tipo 
        self.label.setText(QtGui.QApplication.translate("Form", "Recta", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setVisible(False)

        #X1
        self.lineEdit.setVisible(False)

        #Y1
        self.lineEdit_2.setVisible(False)

        #X2
        self.lineEdit_3.setVisible(False)

        #Y2
        self.lineEdit_4.setVisible(False)

        #X1
        self.label_2.setVisible(False)


        #Y1
        self.label_3.setVisible(False)


        #X2
        self.label_4.setVisible(False)

        #Y2
        self.label_5.setVisible(False)


        #Boton Aceptar
        self.btnAceptar.setVisible(False)
           
        #Boton Cancelar
        self.btnCancelar.setVisible(False)

        #Vista Previa
        self.btnPrevia.setVisible(False)

        
    def setCancelar(self):
        
        #Etiqueta de Tipo 
        self.label.setText(QtGui.QApplication.translate("Form", "Recta", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setVisible(False)

        #X1
        self.lineEdit.setVisible(False)

        #Y1
        self.lineEdit_2.setVisible(False)

        #X2
        self.lineEdit_3.setVisible(False)

        #Y2
        self.lineEdit_4.setVisible(False)

        #X1
        self.label_2.setVisible(False)

        #Y1
        self.label_3.setVisible(False)


        #X2
        self.label_4.setVisible(False)

        #Y2
        self.label_5.setVisible(False)


        #Boton Aceptar
        self.btnAceptar.setVisible(False)
           
        #Boton Cancelar
        self.btnCancelar.setVisible(False)

        #Vista Previa
        self.btnPrevia.setVisible(False)


        if elementoDominio.ContEnsayo.hayRectaCandidata:
            elementoDominio.ContEnsayo.eliminarRectaCandidata()
        if elementoDominio.hayPozoCandidato:
            elementoDominio.hayPozoCandidato = False
            elementoDominio.pozoCandidato.hide()
            elementoDominio.pozoCandidato = None

    def setPrevia(self):
        
        if self.label.text() == "Pozo":
            if self.lineEdit.text() != "" and self.lineEdit_2.text() != "":
                if not elementoDominio.hayPozoCandidato:
                    elementoDominio.pozoCandidato = QtGui.QPushButton(elementoDominio.Dominio)
                    elementoDominio.hayPozoCandidato = True
                elementoDominio.pozoCandidato.setGeometry(QtCore.QRect(np.int32(self.lineEdit.text()),
                                                                       np.int32(self.lineEdit_2.text()), 25, 20))
                elementoDominio.pozoCandidato.setStyleSheet(_fromUtf8("background-color: red;\n"))
                elementoDominio.pozoCandidato.show()
                

        else:                                   
            if self.lineEdit.text() != "" and self.lineEdit_2.text() != "" and self.lineEdit_3.text()!= "" and self.lineEdit_4.text() != "":

                elementoDominio.ContEnsayo.agregarRectaCandidata("Positivo", np.int32(self.lineEdit.text()),
                                                                 np.int32(self.lineEdit_2.text()), np.int32(self.lineEdit_3.text()),
                                                                 np.int32(self.lineEdit_4.text()))
            


"""
La clase Ui_Form es invocada en el archivo principal de la aplicacion.
su funcion es agregar los elementos correspondientes a la vista de
crear dominio
"""

class Ui_Form(object):

    def setupUi(self, Form, ContEnsayo):


        elementoDominio.ContEnsayo = ContEnsayo
        
        #Seteo del formulario que contendra todos los widgets del dominio
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(100, 40, 471, 351))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame.setEnabled(True)

        self.groupBoxDominio = QtGui.QGroupBox(self.frame)
        self.groupBoxDominio.setGeometry(QtCore.QRect(20, 27, 231, 271))
        self.groupBoxDominio.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.groupBoxDominio.setStyleSheet(_fromUtf8("border-color: rgb(255, 85, 0);\n"))
        self.groupBoxDominio.setTitle(QtGui.QApplication.translate("Form", "Dominio", None, QtGui.QApplication.UnicodeUTF8))

        #Caja de elementos especifica del dominio
        elementoDominio.Dominio = box(self.groupBoxDominio)

        #Definimos la instancia global del menu y le asociamo
        #un padre.
        elementoDominio.menuMouse = menu(elementoDominio.Dominio)       
        
        self.groupBox = QtGui.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(260, 20, 151, 81))
        self.groupBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.groupBox.setStyleSheet(_fromUtf8("border-color: rgb(255, 85, 0);\n"))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Barra Herramientas", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
            
        #Creacion de botones de la barra de herramientas
        self.pozo = boton(QtGui.QIcon("content/images/DotIcon.png"), "", self.groupBox, "pozo")
        
        self.barrera = boton(QtGui.QIcon("content/images/barrera.png"), "", self.groupBox, "barrera")

        self.barrera.setGeometry(QtCore.QRect(50, 50, 41, 20))
        self.barrera.id = 1001
        

        elementoDominio.gbCoord = gbCoordenadas(self.frame)


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
