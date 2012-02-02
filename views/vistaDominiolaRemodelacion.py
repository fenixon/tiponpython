# -*- coding: cp1252 -*-
"""
Esta es la vista que definira la GUI del dominio.
Con sus clases, y codigo auxiliar.

Creado por TIPONPYTHON Cooperative

"""

from PyQt4 import QtCore, QtGui
import sys
import numpy as np
import asociarEnsayos
import vistaoptimizacion
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


"""
La clase elemento dominio contiene codigo auxiliar. Es una clase
de caracter global.

Sus atributos, a modo de banderas, van a ser aprovechados por las
instancias de la clases boton y box, gbCoordenadas y menu.

Los valores por defecto de estos atributos sonfocusOutEvent

elementoDominio = 0
existe = False
idElemento = 1000

---

Descripcion de elementoDominio

Es una bandera de control, que le dice a la aplicacion que tipo de
elemento se esta arrastrando al dominio para ser creado.

Valores de los elementos actuales

elementoDominio = 0

Es usado para insertar un pozo

elementoDominio = 1

Es usado para insertar una barrera

elementoDominio es cambiado en la funcion mouseMoveEvent de la clase
boton, mientras que es evaluado en la funcion dropEvent de la clase
box.

---

Descripcion de  reloj y transicion

Son banderas de control que le dice a la aplicacion, dependiendo de sus
estados, cuando se puede comenzar a arrastrar un boton de la barra de herramientas,
tipicamente un pozo o una barrera.

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

Descripcion de ContEnsayo

Basicamente se guarda la instancia del controlador global creado en
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

    acepto = True

    elementoDominio = 0

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

    pozoSeleccionado = 0


    def __init__(self):
        super(elementoDominio, self).__init__()


#Vista de las graficas
class vistaGrafica(QtGui.QGraphicsView):

	global elementoDominio
	id = 0

	def __init__(self, escena, parent, anchoView, altoView):
		super(vistaGrafica, self).__init__(escena, parent)
		self.anchoView=anchoView
		self.altoView=altoView
		self.init()

	def init(self):

		self.setGeometry(0, 30, self.anchoView+30, self.altoView+20)

		self.setSceneRect(0, 0, elementoDominio.ContEnsayo.dominio.ancho, elementoDominio.ContEnsayo.dominio.alto)


		self.setAcceptDrops(True)
		self.setObjectName(_fromUtf8("Dominio"))
		self.setMouseTracking(True)

		#Variables a considerar
		self.presionandoRecta = False

		self.idRecta = 1000

		self.botones = []

		self.rectas = []

		self.bGiratorios = []

		self.rectaSeleccionada = {}

		self.rectaSeleccionada['id'] = 0

		self.rectaCandidata = ""

		self.moviendo = False

		self.movido = ""

		self.eje = QtGui.QGraphicsPixmapItem(QtGui.QPixmap(""), None, self.scene())
		self.eje.setX(5)
		self.eje.setY(elementoDominio.ContEnsayo.dominio.alto)


		self.ejeX = QtGui.QGraphicsLineItem(QtCore.QLineF(self.eje.x(), self.eje.y(), elementoDominio.ContEnsayo.dominio.ancho + 5, self.eje.y()), None, self.scene())

		self.ejeY = QtGui.QGraphicsLineItem(QtCore.QLineF(self.eje.x(), self.eje.y(), self.eje.x(), 0), None,
self.scene())

		self.ejeXopuesto = QtGui.QGraphicsLineItem(QtCore.QLineF(self.eje.x(), 0, elementoDominio.ContEnsayo.dominio.ancho + 5, 0), None, self.scene())


		self.ejeYopuesto = QtGui.QGraphicsLineItem(QtCore.QLineF(elementoDominio.ContEnsayo.dominio.ancho + 5, self.eje.y(), elementoDominio.ContEnsayo.dominio.ancho + 5, 0), None,
self.scene())

		self.ejeEscena = self.mapToScene(self.eje.x(), self.eje.y())

		self.a1 = 0

		self.a2 = 0

		self.b1 = 0

		self.b2 = 0

		self.alto = elementoDominio.ContEnsayo.dominio.alto

		self.ancho = elementoDominio.ContEnsayo.dominio.ancho



	#Sobreescribimos dragEnterEvent para pemitir
	#la accion de este evento.
	def dragEnterEvent(self, e):
		e.accept()

	#Evento que es llamado cuando se suelta un elemento
	#dentro del groupbox
	def dropEvent(self, e):

		elementoDominio.transicion = False
		elementoDominio.reloj = False
		self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))

		#Obtenemos la posicion relativa del lugar en que el
		#elemento es soltado
		position = self.mapToScene(QtCore.QPoint(e.pos().x(), e.pos().y()))

		self.transformarCoordenada(position)


		if self.a1 < 0 or self.a2 < 0 or self.a1 > self.ancho or self.a2 > self.alto:
			return

		if elementoDominio.elementoDominio == 0:
			b = vistaPozo(QtGui.QPixmap("content/images/blackDotIcon.png"), "pozo", elementoDominio.Dominio.scene())

			b.id = elementoDominio.ContEnsayo.agregarPozo(elementoDominio.Dominio.a1, elementoDominio.Dominio.a2)

			self.transformarCoordenada(QtCore.QPoint( elementoDominio.Dominio.a1, elementoDominio.Dominio.a2))

			b.setX(elementoDominio.Dominio.a1 - 15)

			b.setY(elementoDominio.Dominio.a2 -10)

			self.botones.append(b)

			elementoDominio.gbCoord.setPozoExistente(b.id)



		else:

			#barrera = vistaBarrera(position.x(), position.y(), (position.x() + 350), (position.y() + 350), "barrera", elementoDominio.Dominio.scene())

			self.transformarCoordenada(QtCore.QPoint(position.x(), position.y()))
			self.transformarCoordenadaY(QtCore.QPoint((position.x() - 35), (position.y() - 35)))


			barrera = vistaBarrera(self.a1, self.a2, self.b1, self.b2, "barrera", elementoDominio.Dominio.scene())

			self.transformarCoordenada(QtCore.QPoint(barrera.line().x1(), barrera.line().y1()))
			self.transformarCoordenadaY(QtCore.QPoint(barrera.line().x2(), barrera.line().y2()))

			barrera.id = elementoDominio.ContEnsayo.agregarRecta(elementoDominio.gbCoord.cbTipo.currentText(), self.a1, self.a2, self.b1, self.b2)

			elementoDominio.gbCoord.setRectaExistente(barrera.id, 0)

			self.rectas.append(barrera)

		e.setDropAction(QtCore.Qt.MoveAction)
		e.accept()


	def mouseMoveEvent(self, e):
		e.accept()

		punto = self.mapToScene(QtCore.QPoint(e.pos().x(), e.pos().y()))

		self.transformarCoordenada(punto)

		elementoDominio.coordenadas.setText("x ->" + QtCore.QString.number(self.a1, 10) + " y -> " + QtCore.QString.number(self.a2, 10) )

		if self.moviendo:

			if self.movido.tooltip == "pozo":

				if self.a1 > 0 and punto.y() > 0 and punto.y() < self.ejeEscena.y() - 10 and self.a1 < self.ancho - 5:

					self.movido.setPixmap(QtGui.QPixmap("content/images/redDotIcon.png"))
					self.movido.setX(punto.x())
					self.movido.setY(punto.y() - 10)

					for x in elementoDominio.Dominio.botones:
						if x.id == self.movido.id:
							x = self.movido

					elementoDominio.gbCoord.actualizarCoordenadasPozo(self.movido.id)
					elementoDominio.ContEnsayo.moverPozo(self.movido.id, self.a1, self.a2)

				elif self.a1 <= 0:
					if self.a2 > 0 and self.a2 < self.alto:
						self.movido.setPixmap(QtGui.QPixmap("content/images/redDotIcon.png"))
						self.movido.setX(0)
						self.movido.setY(punto.y() - 10)

						elementoDominio.gbCoord.actualizarCoordenadasPozo(self.movido.id)
						elementoDominio.ContEnsayo.moverPozo(self.movido.id, 0, self.a2)
					elif self.a2 <= 0:
						self.movido.setPixmap(QtGui.QPixmap("content/images/redDotIcon.png"))
						self.movido.setX(0)
						self.movido.setY(self.alto - 10)

						elementoDominio.gbCoord.actualizarCoordenadasPozo(self.movido.id)
						elementoDominio.ContEnsayo.moverPozo(self.movido.id, 0,0)
					elif self.a2 >= self.alto:
						self.movido.setPixmap(QtGui.QPixmap("content/images/redDotIcon.png"))
						self.movido.setX(0)
						self.movido.setY(0 - 10)

						elementoDominio.gbCoord.actualizarCoordenadasPozo(self.movido.id)
						elementoDominio.ContEnsayo.moverPozo(self.movido.id, 0, self.alto)



				elif self.a1 >= self.ancho:
						if self.a2 > 0 and self.a2 < self.alto:
							self.movido.setPixmap(QtGui.QPixmap("content/images/redDotIcon.png"))
							self.movido.setX(self.ancho)
							self.movido.setY(punto.y() - 10)

							elementoDominio.gbCoord.actualizarCoordenadasPozo(self.movido.id)
							elementoDominio.ContEnsayo.moverPozo(self.movido.id, self.ancho, self.a2)
						elif self.a2 <= 0:
							self.movido.setPixmap(QtGui.QPixmap("content/images/redDotIcon.png"))
							self.movido.setX(self.ancho)
							self.movido.setY(self.alto - 10)

							elementoDominio.gbCoord.actualizarCoordenadasPozo(self.movido.id)
							elementoDominio.ContEnsayo.moverPozo(self.movido.id, self.ancho, 0)
						elif self.a2 >= self.alto:
							self.movido.setPixmap(QtGui.QPixmap("content/images/redDotIcon.png"))
							self.movido.setX(self.ancho)
							self.movido.setY(0 - 10)

							elementoDominio.gbCoord.actualizarCoordenadasPozo(self.movido.id)
							elementoDominio.ContEnsayo.moverPozo(self.movido.id, self.ancho, self.alto)


				elif self.a2 <= 0:
					self.movido.setPixmap(QtGui.QPixmap("content/images/redDotIcon.png"))
					self.movido.setX(punto.x())
					self.movido.setY(self.alto  - 10)

					elementoDominio.gbCoord.actualizarCoordenadasPozo(self.movido.id)
					elementoDominio.ContEnsayo.moverPozo(self.movido.id, self.a1, 0)

				elif self.a2 >= self.alto:
					if self.a1 > 0 and self.a1 < self.ancho:
						self.movido.setPixmap(QtGui.QPixmap("content/images/redDotIcon.png"))
						self.movido.setX(punto.x())
						self.movido.setY(0 - 10)

						elementoDominio.gbCoord.actualizarCoordenadasPozo(self.movido.id)
						elementoDominio.ContEnsayo.moverPozo(self.movido.id, self.a1, self.alto)


			elif self.movido.tooltip == "barrera":

				recta = self.movido.line()

				puntoP = QtCore.QPointF(punto.x(), punto.y())
				puntoQ = QtCore.QPointF(recta.x1(), recta.y1())

				rectay = QtCore.QLineF(puntoP, puntoQ)

				puntoR = QtCore.QPointF(recta.x2(), recta.y2())

				rectaw = QtCore.QLineF(puntoP, puntoR)

				valor1 = np.absolute(recta.dx() /2)
				valor2 = np.absolute(recta.dy() /2)

				self.transformarCoordenada(QtCore.QPoint(punto.x(), punto.y()))

				self.transformarCoordenadaY(QtCore.QPoint(punto.x(), punto.y()))

				#Recta proxima a las x
				if np.absolute(rectay.dx()) < np.absolute(recta.dx() /2) and  np.absolute(rectay.dy()) < np.absolute((recta.dy() / 2)):
					self.setCursor(QtGui.QCursor(QtCore.Qt.SizeFDiagCursor))
					if self.a2 >= self.alto:
						if self.a1 <= 0:
							self.movido.setLine(0, 0, self.movido.line().x2(), self.movido.line().y2())
						elif self.a1 >= self.ancho:
							self.movido.setLine(self.ancho, 0, self.movido.line().x2(), self.movido.line().y2())
						else:
							self.movido.setLine(punto.x(), 0, self.movido.line().x2(), self.movido.line().y2())

					elif self.a2 <= 0:
						if self.a1 <= 0:
							self.movido.setLine(0, self.alto, self.movido.line().x2(), self.movido.line().y2())
						elif self.a1 >= self.alto:
							self.movido.setLine(self.ancho, self.alto, self.movido.line().x2(), self.movido.line().y2())
						else:
							self.movido.setLine(punto.x(), self.alto, self.movido.line().x2(), self.movido.line().y2())
					elif self.a1 <= 0:
						self.movido.setLine(0, punto.y(), self.movido.line().x2(), self.movido.line().y2())
					elif self.a1 >= self.ancho :
						self.movido.setLine(self.ancho, punto.y(), self.movido.line().x2(), self.movido.line().y2())
					else:
						self.movido.setLine(punto.x(), punto.y(), self.movido.line().x2(), self.movido.line().y2())

					self.movido.eje = "x"

				#Recta proxima a las y
				elif np.absolute(rectaw.dx()) < np.absolute(recta.dx() /2) and  np.absolute(rectaw.dy()) < np.absolute((recta.dy() / 2)):
 
					if self.b2 >= self.alto:
						if self.b1 <= 0:
							self.movido.setLine(self.movido.line().x1(), self.movido.line().y1(), 0, 0)

						elif self.b1 >= self.ancho:
							self.movido.setLine(self.movido.line().x1(), self.movido.line().y1(), self.ancho, 0)

						else:
							self.movido.setLine(self.movido.line().x1(), self.movido.line().y1(), punto.x(), 0)


					elif self.b2 <= 0:
						if self.b1 <= 0:
							self.movido.setLine(self.movido.line().x1(), self.movido.line().y1(), 0, self.alto)
						elif self.b1 >= self.alto:
							self.movido.setLine(self.movido.line().x1(), self.movido.line().y1(), self.ancho, self.alto)
						else:
							self.movido.setLine(self.movido.line().x1(), self.movido.line().y1(), punto.x(), self.alto)

					elif self.b1 <= 0:
						self.movido.setLine(self.movido.line().x1(), self.movido.line().y1(), 0, punto.y())
					elif self.b1 >= self.ancho :
						self.movido.setLine(self.movido.line().x1(), self.movido.line().y1(), self.ancho, punto.y())
					else:
						self.movido.setLine(self.movido.line().x1(), self.movido.line().y1(), punto.x(), punto.y())

 
					self.movido.eje = "y"
					self.setCursor(QtGui.QCursor(QtCore.Qt.SizeBDiagCursor))

				elif  self.movido.eje == "x":
					if self.a2 >= self.alto:
						if self.a1 <= 0:
							self.movido.setLine(0, 0, self.movido.line().x2(), self.movido.line().y2())
						elif self.a1 >= self.ancho:
							self.movido.setLine(self.ancho, 0, self.movido.line().x2(), self.movido.line().y2())
						else:
							self.movido.setLine(punto.x(), 0, self.movido.line().x2(), self.movido.line().y2())


					elif self.a2 <= 0:
						if self.a1 <= 0:
							self.movido.setLine(0, self.alto, self.movido.line().x2(), self.movido.line().y2())
						elif self.a1 >= self.alto:
							self.movido.setLine(self.ancho, self.alto, self.movido.line().x2(), self.movido.line().y2())
						else:
							self.movido.setLine(punto.x(), self.alto, self.movido.line().x2(), self.movido.line().y2())
					elif self.a1 <= 0:
						self.movido.setLine(0, punto.y(), self.movido.line().x2(), self.movido.line().y2())
					elif self.a1 >= self.ancho:
						self.movido.setLine(self.ancho, punto.y(), self.movido.line().x2(), self.movido.line().y2())
					else:
						self.movido.setLine(punto.x(), punto.y(), self.movido.line().x2(), self.movido.line().y2())

					self.setCursor(QtGui.QCursor(QtCore.Qt.SizeFDiagCursor))
				elif self.movido.eje == "y":
 
					if self.b2 >= self.alto:
						if self.b1 <= 0:
							self.movido.setLine(self.movido.line().x1(), self.movido.line().y1(), 0, 0)

						elif self.b1 >= self.ancho:
							self.movido.setLine(self.movido.line().x1(), self.movido.line().y1(), self.ancho, 0)

						else:
							self.movido.setLine(self.movido.line().x1(), self.movido.line().y1(), punto.x(), 0)


					elif self.b2 <= 0:
						if self.b1 <= 0:
							self.movido.setLine(self.movido.line().x1(), self.movido.line().y1(), 0, self.alto)
						elif self.b1 >= self.alto:
							self.movido.setLine(self.movido.line().x1(), self.movido.line().y1(), self.ancho, self.alto)
						else:
							self.movido.setLine(self.movido.line().x1(), self.movido.line().y1(), punto.x(), self.alto)

					elif self.b1 <= 0:
						self.movido.setLine(self.movido.line().x1(), self.movido.line().y1(), 0, punto.y())
					elif self.b1 >= self.ancho :
						self.movido.setLine(self.movido.line().x1(), self.movido.line().y1(), self.ancho, punto.y())
					else:
						self.movido.setLine(self.movido.line().x1(), self.movido.line().y1(), punto.x(), punto.y())
 

					self.setCursor(QtGui.QCursor(QtCore.Qt.SizeBDiagCursor))

				self.transformarCoordenada(QtCore.QPoint(self.movido.line().x1(), self.movido.line().y1()))

				self.transformarCoordenadaY(QtCore.QPoint(self.movido.line().x2(), self.movido.line().y2()))

				elementoDominio.ContEnsayo.actualizarRectaCoordenada(self.movido.id, self.movido.line().x1(), self.a2, self.movido.line().x2(), self.b2)

				elementoDominio.gbCoord.setRectaExistente(self.movido.id, 0)


	def mousePressEvent(self, e):

		item = self.itemAt(e.pos().x(), e.pos().y())

		if item != None:

			try:
				posicion = self.mapToScene(QtCore.QPoint(e.pos().x(), e.pos().y()))
				self.transformarCoordenada(posicion)
				if item.tooltip == "pozo" and e.button() == QtCore.Qt.LeftButton:
					item.setPixmap(QtGui.QPixmap("content/images/redDotIcon.png"))
					self.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))

					#Se muestran sus coordenadas
					#elementoDominio.gbCoord.setPozoExistente(item.id)
					elementoDominio.pozoSeleccionado = item.id

					#elementoDominio.ContEnsayo.moverPozo(item.id, self.a1, self.a2)

					elementoDominio.gbCoord.actualizarCoordenadasPozo(item.id)

					self.rectaSeleccionada['id'] = 0

					for pozo in elementoDominio.Dominio.botones:
						if pozo.id != item.id:
							pozo.setPixmap(QtGui.QPixmap("content/images/blackDotIcon.png"))

					for r in elementoDominio.Dominio.rectas:
						r.setPen(QtCore.Qt.black)

					self.moviendo = True

					self.movido = item

				elif item.tooltip == "pozo" and e.button() == QtCore.Qt.RightButton:
					item.setPixmap(QtGui.QPixmap("content/images/redDotIcon.png"))

					for pozo in elementoDominio.Dominio.botones:
						if pozo.id != item.id:
							pozo.setPixmap(QtGui.QPixmap("content/images/blackDotIcon.png"))


					for r in elementoDominio.Dominio.rectas:
						r.setPen(QtCore.Qt.black)

					elementoDominio.selectedMenuMouse["tipo"] = "punto"
					elementoDominio.selectedMenuMouse["id"] = item.id

					elementoDominio.menuMouse.modelo.removeRows(0, elementoDominio.menuMouse.modelo.rowCount())
                                        
                                        
					elementoDominio.menuMouse.modelo.insertRows(0, 5)

					modelo3 = elementoDominio.menuMouse.modelo.createIndex(0, 0)
					elementoDominio.menuMouse.modelo.setData(modelo3, "MENU")


                                        ## Averiguar si un pozo tiene observaciones
                                        if len(elementoDominio.ContEnsayo.buscarPozo(item.id).observaciones)>0:

                                            modelo = elementoDominio.menuMouse.modelo.createIndex(1, 0)
                                            elementoDominio.menuMouse.modelo.setData(modelo, "Asociar")

                                            modelo = elementoDominio.menuMouse.modelo.createIndex(2, 0)
                                            elementoDominio.menuMouse.modelo.setData(modelo, "Optimizar")                                        

                                            modelo = elementoDominio.menuMouse.modelo.createIndex(3, 0)
                                            elementoDominio.menuMouse.modelo.setData(modelo, "Eliminar")

                                            modelo = elementoDominio.menuMouse.modelo.createIndex(4, 0)
                                            elementoDominio.menuMouse.modelo.setData(modelo, "Salir")

                                        else:                                     

                                            modelo = elementoDominio.menuMouse.modelo.createIndex(1, 0)
                                            elementoDominio.menuMouse.modelo.setData(modelo, "Asociar")

                                            modelo = elementoDominio.menuMouse.modelo.createIndex(2, 0)
                                            elementoDominio.menuMouse.modelo.setData(modelo, "Eliminar")

                                            modelo = elementoDominio.menuMouse.modelo.createIndex(3, 0)
                                            elementoDominio.menuMouse.modelo.setData(modelo, "Salir")                                            
                                        
					elementoDominio.menuMouse.move(np.int(e.pos().x()), np.int(e.pos().y()))
					elementoDominio.menuMouse.show()

				elif item.tooltip == "barrera" and e.button() == QtCore.Qt.LeftButton:
					item.setPen(QtCore.Qt.red)
					self.moviendo = True
					self.movido = item
					self.rectaSeleccionada['id'] = item.id

					elementoDominio.gbCoord.setRectaExistente(item.id, 0)

					for pozo in elementoDominio.Dominio.botones:
						pozo.setPixmap(QtGui.QPixmap("content/images/blackDotIcon.png"))

					for r in elementoDominio.Dominio.rectas:
						if r.id != item.id:
							r.setPen(QtCore.Qt.black)

				elif item.tooltip == "barrera" and e.button() == QtCore.Qt.RightButton:

					for pozo in elementoDominio.Dominio.botones:
						pozo.setPixmap(QtGui.QPixmap("content/images/blackDotIcon.png"))

					for r in elementoDominio.Dominio.rectas:
						if r.id != item.id:
							r.setPen(QtCore.Qt.black)

					self.rectaSeleccionada['id'] = item.id
					item.setPen(QtCore.Qt.red)
					elementoDominio.selectedMenuMouse["tipo"] = "recta"
					elementoDominio.selectedMenuMouse["id"] = item.id


					elementoDominio.menuMouse.modelo.removeRows(0, elementoDominio.menuMouse.modelo.rowCount())


					elementoDominio.menuMouse.modelo.insertRows(0, 3)


					modelo3 = elementoDominio.menuMouse.modelo.createIndex(0, 0)
					elementoDominio.menuMouse.modelo.setData(modelo3, "MENU")


					modelo = elementoDominio.menuMouse.modelo.createIndex(1, 0)
					elementoDominio.menuMouse.modelo.setData(modelo, "Eliminar")

					modelo2 = elementoDominio.menuMouse.modelo.createIndex(2, 0)
					elementoDominio.menuMouse.modelo.setData(modelo2, "Salir")


					elementoDominio.menuMouse.move(np.int(e.pos().x()), np.int(e.pos().y()))

					elementoDominio.menuMouse.show()
			except:
				print "No es pozo ni barrera."



	def mouseReleaseEvent(self, e):

		self.moviendo = False
		self.movido = None
		self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))


	def transformarCoordenada(self, punto):

		if punto.x() == self.ejeEscena.x() and  punto.y() == self.ejeEscena.y():
			self.a1 = 0
			self.a2 = 0

		elif punto.x() == self.ejeEscena.x() and  punto.y() > self.ejeEscena.y():
			self.a1 = 0
			self.a2 = - np.absolute(punto.y() - self.ejeEscena.y())

		elif punto.x() == self.ejeEscena.x() and  punto.y() < self.ejeEscena.y():
			self.a1 = 0
			self.a2 = np.absolute(punto.y() - self.ejeEscena.y())

		elif punto.x() > self.ejeEscena.x() and  punto.y() == self.ejeEscena.y():
			self.a1 = np.absolute(punto.x() - self.ejeEscena.x())
			self.a2 = 0

		elif punto.x() < self.ejeEscena.x() and  punto.y() == self.ejeEscena.y():
			self.a1 = - np.absolute(punto.x() - self.ejeEscena.x())
			self.a2 = 0

		elif punto.x() > self.ejeEscena.x() and punto.y() < self.ejeEscena.y():
			self.a1 = np.absolute(punto.x() - self.ejeEscena.x())
			self.a2 = np.absolute(punto.y() - self.ejeEscena.y())


		elif punto.x() > self.ejeEscena.x() and punto.y() > self.ejeEscena.y():
			self.a1 = np.absolute(punto.x() - self.ejeEscena.x())
			self.a2 = - np.absolute(punto.y() - self.ejeEscena.y())

		elif punto.x() < self.ejeEscena.x() and punto.y() < self.ejeEscena.y():
			self.a1 = - np.absolute(punto.x() - self.ejeEscena.x())
			self.a2 = np.absolute(punto.y() - self.ejeEscena.y())

		elif punto.x() < self.ejeEscena.x() and punto.y() > self.ejeEscena.y():
			self.a1 = - np.absolute(punto.x() - self.ejeEscena.x())
			self.a2 = - np.absolute(punto.y() - self.ejeEscena.y())


	def transformarCoordenadaY(self, punto):
		if punto.x() == self.ejeEscena.x() and  punto.y() == self.ejeEscena.y():
			self.b1 = 0
			self.b2 = 0

		elif punto.x() == self.ejeEscena.x() and  punto.y() > self.ejeEscena.y():
			self.b1 = 0
			self.b2 = - np.absolute(punto.y() - self.ejeEscena.y())

		elif punto.x() == self.ejeEscena.x() and  punto.y() < self.ejeEscena.y():
			self.b1 = 0
			self.b2 = np.absolute(punto.y() - self.ejeEscena.y())

		elif punto.x() > self.ejeEscena.x() and  punto.y() == self.ejeEscena.y():
			self.b1 = np.absolute(punto.x() - self.ejeEscena.x())
			self.b2 = 0

		elif punto.x() < self.ejeEscena.x() and  punto.y() == self.ejeEscena.y():
			self.b1 = - np.absolute(punto.x() - self.ejeEscena.x())
			self.b2 = 0

		elif punto.x() > self.ejeEscena.x() and punto.y() < self.ejeEscena.y():
			self.b1 = np.absolute(punto.x() - self.ejeEscena.x())
			self.b2 = np.absolute(punto.y() - self.ejeEscena.y())

		elif punto.x() > self.ejeEscena.x() and punto.y() > self.ejeEscena.y():
			self.b1 = np.absolute(punto.x() - self.ejeEscena.x())
			self.b2 = - np.absolute(punto.y() - self.ejeEscena.y())

		elif punto.x() < self.ejeEscena.x() and punto.y() < self.ejeEscena.y():
			self.b1 = - np.absolute(punto.x() - self.ejeEscena.x())
			self.b2 = np.absolute(punto.y() - self.ejeEscena.y())

		elif punto.x() < self.ejeEscena.x() and punto.y() > self.ejeEscena.y():
			self.b1 = - np.absolute(punto.x() - self.ejeEscena.x())
			self.b2 = - np.absolute(punto.y() - self.ejeEscena.y())


	def modificarTamDominio(self):


		if self.a2 < 0:

			aumento = self.scene().height() + np.absolute( self.a2 ) + 20

			self.ejeEscena.setY(self.ejeEscena.y() +  np.absolute( self.a2 ) )


			self.ejeX.setLine(self.ejeX.line().x1(), self.ejeEscena.y(), self.ejeX.line().x2(), self.ejeEscena.y())

			self.ejeY.setLine(self.ejeY.line().x1(), self.ejeEscena.y(),self.ejeY.line().x2(),self.ejeY.line().y2())

			self.transformarCoordenada(QtCore.QPointF(np.int32(elementoDominio.gbCoord.lineEdit.text()), np.int32(elementoDominio.gbCoord.lineEdit_2.text())))


			self.setSceneRect(QtCore.QRectF(0, 0, self.scene().width(), aumento) )
			self.ancho = self.scene().width()
			self.alto = self.scene().height() - (self.scene().height() - self.ejeEscena.y())
			self.setSceneRect(QtCore.QRectF(0, 0, self.scene().width(), self.scene().height() - (self.scene().height() - self.ejeEscena.y()) ) )


		if self.a1 > self.scene().width():

			aumento = self.scene().width() + np.absolute( self.a1 - self.scene().width()) + 20


			self.setSceneRect(QtCore.QRectF(0, 0, aumento, self.scene().height()))
			self.ancho = aumento
			self.alto = self.scene().height()


	def dibujarRecta(self, bid):
		for x in self.rectas:
			if bid == x.id:
				r = elementoDominio.ContEnsayo.buscarRecta(x.id)
				print "x1 ", r.x1, " y1 ", r.y1, " x3 ", r.x3, " y3 ", r.y3
				print "x4 ", r.x4, " y4 ", r.y4, " x2 ", r.x2, " y2 ", r.y2
				x.setPen(QtCore.Qt.red)
				if r.x1 < r.x2 :
					x.setLine(QtCore.QLineF( r.x4, r.y4, r.x3, r.y3))
				else:
					x.setLine(QtCore.QLineF( r.x3, r.y3, r.x4, r.y4))

		"""
			else:
				painter.setPen(QtCore.Qt.blue)
				painter.drawLine(QtCore.QLineF( x.x1, x.y1, x.x2, x.y2))
				if x.x1 < x.x2 :
					painter.drawLine(QtCore.QLineF( x.x1, x.y1, x.x3, x.y3))
					painter.drawLine(QtCore.QLineF( x.x4, x.y4, x.x2, x.y2))
				else:
					painter.drawLine(QtCore.QLineF( x.x1, x.y1, x.x4, x.y4))
					painter.drawLine(QtCore.QLineF( x.x3, x.y3, x.x2, x.y2))
		
		else:
			painter.setPen(QtCore.Qt.blue)
			painter.drawLine(QtCore.QLineF( x.x1, x.y1, x.x2, x.y2))
			if x.x1 < x.x2 :
				painter.drawLine(QtCore.QLineF( x.x1, x.y1, x.x3, x.y3))
				painter.drawLine(QtCore.QLineF( x.x4, x.y4, x.x2, x.y2))
			else:
				painter.drawLine(QtCore.QLineF( x.x1, x.y1, x.x4, x.y4))
				painter.drawLine(QtCore.QLineF( x.x3, x.y3, x.x2, x.y2))
		"""

#Escena contenedora de los items graficos
class escenaGrafica(QtGui.QGraphicsScene):
	def __init__(self):
		super(escenaGrafica, self).__init__()
		self.init()
	def __init__(self, parent):
		super(escenaGrafica, self).__init__(parent)
		self.init()

	def init(self):
		pass

	#Sobreescribimos dragEnterEvent para pemitir
	#la accion de este evento.
	def dragEnterEvent(self, e):
		e.accept()

	def dropEvent(self, e):
		e.accept()

	def dragMoveEvent(self, event):
		event.accept()



#Clase para los items pozo
class vistaPozo(QtGui.QGraphicsPixmapItem):

	global elementoDominio

	id = 1000

	posicion = 0

	accionCoord = {}


	def __init__(self, icono, tooltip, escena):
		super(vistaPozo, self).__init__(icono, None, escena)
		self.init(tooltip)

	def init(self, tooltip):
		self.setAcceptDrops(True)
		self.tooltip = tooltip
		self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
		self.setToolTip(QtGui.QApplication.translate("Form", tooltip, None, QtGui.QApplication.UnicodeUTF8))



	#Cuando se suelta el mouse luego de un arrastre
	#incondicionalmente se setean las banderas globales con los siguientes
	#valores
	def mouseReleaseEvent(self, e):
		self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
		for x in elementoDominio.Dominio.botones:

			if x.id == self.id:

				posicion = e.scenePos()

				if x.tooltip == "pozo":

					elementoDominio.ContEnsayo.moverPozo(x.id, posicion.x(), posicion.y())
					elementoDominio.gbCoord.actualizarCoordenadasPozo(x.id)



#Clase para los items barrera
class vistaBarrera(QtGui.QGraphicsLineItem):

	rotacion = False
	contador = 0
	fuePrimeraRotacion = False
	eje = ""

	def __init__(self, x1, y1, x2, y2, tooltip, escena):

		elementoDominio.Dominio.transformarCoordenada(QtCore.QPoint(x1, y1))

		elementoDominio.Dominio.transformarCoordenadaY(QtCore.QPoint(x2, y2))

		super(vistaBarrera, self).__init__(QtCore.QLineF(elementoDominio.Dominio.a1 - 15, elementoDominio.Dominio.a2 - 10, elementoDominio.Dominio.b1 - 15, elementoDominio.Dominio.b2 - 10), None, escena)
		self.init(tooltip)

	def init(self, tooltip):
		self.tooltip = tooltip


	def mouseReleaseEvent(self, e):
		elementoDominio.gbCoord.setRectaExistente(self.id, 0)



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
        self.setGeometry(QtCore.QRect(15, 20, 41, 23))
        self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.setMouseTracking(True)
        self.setToolTip(QtGui.QApplication.translate("Form", tooltip, None, QtGui.QApplication.UnicodeUTF8))


    def mousePressEvent(self, e):

       if e.button() == QtCore.Qt.LeftButton:

            elementoDominio.pozoSeleccionado = 0

            #Cambiamos el cursor, y luego procedemos a evaluar estado del reloj
            #Si no existe creamos un temporizador, cuando alcanze el tiempo dado
            #el usuario va a poder arrastrar el boton.
            self.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))

            if self.id == 1000:
                elementoDominio.gbCoord.setPozo()

            elif self.id == 1001:
                elementoDominio.gbCoord.setRecta()

            #Volvemos al color normal del pozo seleccionado
            for boton in elementoDominio.Dominio.botones:
                boton.setPixmap(QtGui.QPixmap("content/images/blackDotIcon.png"))


            for recta in elementoDominio.Dominio.rectas:
                recta.setPen(QtCore.Qt.black)


            if elementoDominio.reloj == False:
                reloj = QtCore.QTimer()
                reloj.singleShot(600, self.apagar)
                elementoDominio.transicion = True
                elementoDominio.reloj = True

            #Reseteo de recta seleccionada
            elementoDominio.Dominio.rectaSeleccionada['id'] = 0
            self.update()
            elementoDominio.gbCoord.eliminarPlacebos()
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
                pixmap = QtGui.QPixmap("content/images/blackDotIcon.png")
                drag.setPixmap(pixmap)
                elementoDominio.elementoDominio = 0
            else:
                pixmap = QtGui.QPixmap("content/images/blackBarrera.png")
                drag.setPixmap(pixmap)
                elementoDominio.elementoDominio = 1



            elementoDominio.idElemento = self.id

            drag.setMimeData(mimedata)
            drag.setHotSpot(e.pos() - self.rect().topLeft())
            dropAction = drag.start(QtCore.Qt.MoveAction)


    def apagar(self):
        elementoDominio.transicion = False



class lista(QtGui.QStringListModel):
	def __init__(self, cadenaCar):
		super(lista, self).__init__(cadenaCar)

	#def removeRows (fila, cantidad)

"""
Menu utilizado en definir dominio
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
        self.items << "MENU" << "Optimizar" << "Asociar" << "Eliminar" << "Salir"
        self.modelo = lista(self.items)
        self.setModel(self.modelo)
        self.setGeometry(QtCore.QRect(60, 60, 131, 131))
        self.hide()
    def leaveEvent(self,coso):

        self.reset()
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

                elementoDominio.gbCoord.ocultarFormulario()

                if elementoDominio.selectedMenuMouse["tipo"] == "punto":

                    elementoDominio.ContEnsayo.removerPozo(elementoDominio.selectedMenuMouse["id"])

                    self.aEliminar = []

                    for x in elementoDominio.Dominio.botones:
                        if x.id == elementoDominio.selectedMenuMouse["id"]:
                            x.hide()
                            self.aEliminar.append(x)

                    for x in self.aEliminar:
                        try:
                            elementoDominio.Dominio.botones.remove(x)
                            break
                        except ValueError:
                            print "Punto a eliminar no encontrado, advertencia simple"

                if elementoDominio.selectedMenuMouse["tipo"] == "recta":
                    elementoDominio.ContEnsayo.eliminarRecta(elementoDominio.selectedMenuMouse["id"])

                    self.aEliminar = []

                    for x in elementoDominio.Dominio.rectas:
                        if x.id == elementoDominio.selectedMenuMouse["id"]:
                            x.hide()
                            self.aEliminar.append(x)

                    for x in self.aEliminar:
                        try:
                            elementoDominio.Dominio.rectas.remove(x)
                            break
                        except ValueError:
                            print "Recta a eliminar no encontrado, advertencia simple"


                elementoDominio.selectedMenuMouse["tipo"] == ""
                elementoDominio.selectedMenuMouse["id"] == -1
                self.reset()
                self.hide()

            if valor.toString() == "Asociar":

	  	frmasociar=QtGui.QDialog()
                ui= asociarEnsayos.Ui_Dialog()
                ui.setupUi(frmasociar, elementoDominio.selectedMenuMouse["id"], elementoDominio.ContEnsayo)
                frmasociar.exec_()
                elementoDominio.widget = frmasociar
                self.hide()
            if valor.toString() == "Optimizar":
                i = QtCore.QStringList()
                i << elementoDominio.ContEnsayo.optimizacioneslistar() << "Salir"
                m = QtGui.QStringListModel(i)
                #Listo los metodos de optimizacion
                menusito=menu(elementoDominio.Dominio)
                menusito.setModel(m)
                menusito.move(self.pos().x()+30,self.pos().y())
                menusito.show()
                #Cierro el menu contextual
                self.reset()
                self.hide()
                return
            #Si no es ninguna opcion predeterminada, las opcoines son para elegir metodos de optimizacion
            if valor.toString() != "Optimizar" and valor.toString() != "Salir" and valor.toString() != "Eliminar" and valor.toString() != "Asociar" :
                print "valor es optimizar"
                #Agrego ala coleccion de pozos para optimizar
                print "Agrego para optimizar el pozo "
                print elementoDominio.selectedMenuMouse["id"]
                elementoDominio.ContEnsayo.asociarPozoOptimiazion(elementoDominio.selectedMenuMouse["id"],valor.toString())
                frmopt=QtGui.QDialog()
                ui= vistaoptimizacion.optimizacion(elementoDominio.ContEnsayo,frmopt)
                #ui.setupUi(frmopt,elementoDominio.ContEnsayo)
                #frmopt.show()
                elementoDominio.widget = ui
                getattr(self,'reset')()
                getattr(self,'hide')()
                return

"""
Clase que maneja la interfaz de coordenadas
"""
class gbCoordenadas(QtGui.QGroupBox):

    def __init__(self, padre, posicionBarraTareas, anchoBarraTareas, segundaColY):
        super(gbCoordenadas, self).__init__(padre)
        self.posicionBarraTareas=posicionBarraTareas
        self.anchoBarraTareas=anchoBarraTareas
        self.segundaColY=segundaColY
        self.init()

    def init(self):
        self.setGeometry(QtCore.QRect(self.posicionBarraTareas, 140, self.anchoBarraTareas, 181))
        self.setTitle("Coordenadas")

        #Etiqueta de Tipo
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label.setText(QtGui.QApplication.translate("Form", "Recta Pozo", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setVisible(False)

        #X1
        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(40, 50, 40, 25))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.setVisible(False)

        #Y1
        self.lineEdit_2 = QtGui.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(self.segundaColY+25, 50, 40, 25))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_2.setVisible(False)

        #X2
        self.lineEdit_3 = QtGui.QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 100, 40, 25))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_3.setVisible(False)

        #Y2
        self.lineEdit_4 = QtGui.QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(self.segundaColY+25, 100, 40, 25))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_4.setVisible(False)

        #X1
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 25, 20))
        self.label_2.setText("X1")
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_2.setVisible(False)


        #Y1
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(self.segundaColY, 50, 25, 20))
        self.label_3.setText("Y1")
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_3.setVisible(False)


        #X2
        self.label_4 = QtGui.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 25, 20))
        self.label_4.setText("X2")
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_4.setVisible(False)

        #Y2
        self.label_5 = QtGui.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(self.segundaColY, 100, 25, 20))
        self.label_5.setText("Y2")
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_5.setVisible(False)

        #Combo box
        self.cbTipo = QtGui.QComboBox( self )
        self.cbTipo.setGeometry(QtCore.QRect(60,20, 60, 20))
        listaStrings = QtCore.QStringList()
        listaStrings << "Negativo" << "Positivo"

        self.cbTipo.addItems(listaStrings)
        self.cbTipo.setVisible(False)



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

        #Boton Actualizar
        self.btnActualizar = QtGui.QPushButton(self)
        self.btnActualizar.setGeometry(QtCore.QRect(10,130, 100, 20))
        self.btnActualizar.setText("Actualizar")
        self.btnActualizar.setVisible(False)

        QtCore.QObject.connect(self.btnAceptar, QtCore.SIGNAL('clicked()'), self.setAceptar)
        QtCore.QObject.connect(self.btnCancelar, QtCore.SIGNAL('clicked()'), self.setCancelar)
        QtCore.QObject.connect(self.btnPrevia, QtCore.SIGNAL('clicked()'), self.setPrevia)
        QtCore.QObject.connect(self.btnActualizar, QtCore.SIGNAL('clicked()'), self.setActualizar)

	#Validacion
	self.validadorAncho = QtGui.QIntValidator(0, elementoDominio.Dominio.ancho, self)
	self.validadorAlto = QtGui.QIntValidator(0, elementoDominio.Dominio.alto, self)


	self.lineEdit.setValidator(self.validadorAncho)
	self.lineEdit_2.setValidator(self.validadorAlto)
	self.lineEdit_3.setValidator(self.validadorAncho)
	self.lineEdit_4.setValidator(self.validadorAlto)

    def setPozo(self):

	elementoDominio.transicion = False
	elementoDominio.reloj = False

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

        #Combo
        self.cbTipo.setVisible(False)

        #Boton Aceptar
        self.btnAceptar.setVisible(True)

        #Boton Cancelar
        self.btnCancelar.setVisible(True)

        #Vista Previa
        self.btnPrevia.setVisible(True)

        #Boton Actualizar
        self.btnActualizar.setVisible(False)

    def setRecta(self):

	elementoDominio.transicion = False
	elementoDominio.reloj = False

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

        #Combo
        self.cbTipo.setVisible(True)


        #Boton Aceptar
        self.btnAceptar.setVisible(True)

        #Boton Cancelar
        self.btnCancelar.setVisible(True)

        #Vista Previa
        self.btnPrevia.setVisible(True)

        #Boton Actualizar
        self.btnActualizar.setVisible(False)

    def setAceptar(self):

	elementoDominio.transicion = False
	elementoDominio.reloj = False

	if self.label.text() == "Pozo":

            if self.lineEdit.text() != "" and self.lineEdit_2.text() != "":

                if not elementoDominio.hayPozoCandidato:

                    elementoDominio.pozoCandidato = QtGui.QGraphicsPixmapItem(QtGui.QPixmap("content/images/blackkDotIcon.png"), None, elementoDominio.Dominio.scene())

                    elementoDominio.hayPozoCandidato = True

                    elementoDominio.Dominio.transformarCoordenada(QtCore.QPoint( np.int32(self.lineEdit.text()), np.int32(self.lineEdit_2.text())))

		    if np.int32(self.lineEdit.text()) == 0:
		        elementoDominio.pozoCandidato.setX(0 - 5)
		    else:
		        elementoDominio.pozoCandidato.setX(elementoDominio.Dominio.a1 - 15)
		    if np.int32(self.lineEdit_2.text()) == 0:
		        elementoDominio.pozoCandidato.setY(elementoDominio.Dominio.alto - 10)
		    else:
		        elementoDominio.pozoCandidato.setY(elementoDominio.Dominio.a2 - 10)


                elementoDominio.pozoCandidato.show()


                b = vistaPozo(QtGui.QPixmap("content/images/blackDotIcon.png"), "pozo", elementoDominio.Dominio.scene())

                b.id = elementoDominio.ContEnsayo.agregarPozo(np.int(self.lineEdit.text()), np.int(self.lineEdit_2.text()))

		elementoDominio.Dominio.transformarCoordenada(QtCore.QPoint( np.int32(self.lineEdit.text()), np.int32(self.lineEdit_2.text())))


		if np.int32(self.lineEdit.text()) == 0:
		    b.setX(0 - 5)
		else:
		    b.setX(elementoDominio.Dominio.a1 - 15)
		if np.int32(self.lineEdit_2.text()) == 0:
		    b.setY(elementoDominio.Dominio.alto - 10)
		else:
		    b.setY(elementoDominio.Dominio.a2 - 10)


                elementoDominio.Dominio.botones.append(b)

                b.show()

                elementoDominio.pozoCandidato.hide()
                elementoDominio.pozoCandidato = None
                elementoDominio.hayPozoCandidato = False

        else:
            if self.lineEdit.text() != "" and self.lineEdit_2.text() != "" and self.lineEdit_3.text()!= "" and self.lineEdit_4.text() != "":

		if not elementoDominio.ContEnsayo.hayRectaCandidata():
		    print "PASAMOS POR ACA"

                    elementoDominio.Dominio.transformarCoordenada(QtCore.QPointF(np.int32(self.lineEdit.text()), np.int32(self.lineEdit_2.text())))

                    elementoDominio.Dominio.transformarCoordenadaY(QtCore.QPointF(np.int32(self.lineEdit_3.text()),
np.int32(self.lineEdit_4.text())))


                    barrera = vistaBarrera(np.int32(self.lineEdit.text()), np.int32(self.lineEdit_2.text()), np.int32(self.lineEdit_3.text()),
np.int32(self.lineEdit_4.text()), "barrera", elementoDominio.Dominio.scene())


                    barrera.id = elementoDominio.ContEnsayo.agregarRecta(self.cbTipo.currentText(), np.int32(self.lineEdit.text()), np.int32(self.lineEdit_2.text()), np.int32(self.lineEdit_3.text()),
np.int32(self.lineEdit_4.text()))

                    elementoDominio.Dominio.rectas.append(barrera)

		    print "Coordenadas con las que se guarda x1 ", elementoDominio.Dominio.a1, " Y1 ",elementoDominio.Dominio.a2, " x2 ", elementoDominio.Dominio.b1, " y2 ",elementoDominio.Dominio.b2

		else:
                    elementoDominio.Dominio.transformarCoordenada(QtCore.QPointF(elementoDominio.Dominio.rectaCandidata.line().x1(), elementoDominio.Dominio.rectaCandidata.line().y1()))

                    elementoDominio.Dominio.transformarCoordenadaY(QtCore.QPointF(elementoDominio.Dominio.rectaCandidata.line().x2(), elementoDominio.Dominio.rectaCandidata.line().y2()))

                    barrera = vistaBarrera(elementoDominio.Dominio.a1, elementoDominio.Dominio.a2, elementoDominio.Dominio.b1, elementoDominio.Dominio.b2, "barrera", elementoDominio.Dominio.scene())


                    #elementoDominio.ContEnsayo.agregarRecta(self.cbTipo.currentText(), elementoDominio.Dominio.a1 - 15, elementoDominio.Dominio.a2 - 10, elementoDominio.Dominio.b1 - 15, elementoDominio.Dominio.b2 - 10)

                    barrera.id = elementoDominio.ContEnsayo.incluirCandidata(self.cbTipo.currentText())

		    print "Coordenadas con las que se guarda con vista previa x1 ", barrera.line().x1(), " Y1 ",barrera.line().y1(), " x2 ", barrera.line().x2(), " y2 ",barrera.line().y2()

		    self.setRectaExistente(barrera.id, 0)

                    elementoDominio.Dominio.rectas.append(barrera)
                    elementoDominio.Dominio.rectaCandidata.hide()
                    elementoDominio.Dominio.rectaCandidata = None


        #Reseteo de recta seleccionada
        elementoDominio.Dominio.rectaSeleccionada['id'] = 0

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

        #Combo
        self.cbTipo.setVisible(False)

        #Boton Aceptar
        self.btnAceptar.setVisible(False)

        #Boton Cancelar
        self.btnCancelar.setVisible(False)

        #Vista Previa
        self.btnPrevia.setVisible(False)

        self.btnActualizar.setVisible(False)

    def setCancelar(self):

	elementoDominio.transicion = False
	elementoDominio.reloj = False

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

        #Combo
        self.cbTipo.setVisible(False)

        #Boton Aceptar
        self.btnAceptar.setVisible(False)

        #Boton Cancelar
        self.btnCancelar.setVisible(False)

        #Vista Previa
        self.btnPrevia.setVisible(False)


        if elementoDominio.ContEnsayo.hayRectaCandidata():
            elementoDominio.ContEnsayo.eliminarRectaCandidata()
            elementoDominio.Dominio.rectaCandidata.hide()
        if elementoDominio.hayPozoCandidato:
            elementoDominio.hayPozoCandidato = False
            elementoDominio.pozoCandidato.hide()
            elementoDominio.pozoCandidato = None

    def setPrevia(self):

	elementoDominio.transicion = False
	elementoDominio.reloj = False

        if self.label.text() == "Pozo":
            if self.lineEdit.text() != "" and self.lineEdit_2.text() != "":
                if not elementoDominio.hayPozoCandidato:
                    elementoDominio.pozoCandidato = QtGui.QGraphicsPixmapItem(QtGui.QPixmap("content/images/redDotIcon.png"), None, elementoDominio.Dominio.scene())

                    elementoDominio.hayPozoCandidato = True

		elementoDominio.Dominio.transformarCoordenada(QtCore.QPoint( np.int32(self.lineEdit.text()), np.int32(self.lineEdit_2.text())))


		if np.int32(self.lineEdit.text()) == 0:
		    elementoDominio.pozoCandidato.setX(0 - 5)
		else:
		    elementoDominio.pozoCandidato.setX(elementoDominio.Dominio.a1 - 15)
		if np.int32(self.lineEdit_2.text()) == 0:
		    elementoDominio.pozoCandidato.setY(elementoDominio.Dominio.alto - 10)
		else:
		    elementoDominio.pozoCandidato.setY(elementoDominio.Dominio.a2 - 10)


        else:
            if self.lineEdit.text() != "" and self.lineEdit_2.text() != "" and self.lineEdit_3.text()!= "" and self.lineEdit_4.text() != "":
	        if not elementoDominio.ContEnsayo.hayRectaCandidata():
		    elementoDominio.ContEnsayo.agregarRectaCandidata(self.cbTipo.currentText(),
np.int32(self.lineEdit.text()), np.int32(self.lineEdit_2.text()), np.int32(self.lineEdit_3.text()),np.int32(self.lineEdit_4.text()))

		    elementoDominio.Dominio.transformarCoordenada(QtCore.QPoint( elementoDominio.Dominio.ejeEscena.x() + np.int32( np.int32(self.lineEdit.text()) ), np.int32(self.lineEdit_2.text())))

		    elementoDominio.Dominio.transformarCoordenadaY(QtCore.QPoint( elementoDominio.Dominio.ejeEscena.x() + np.int32( np.int32(self.lineEdit_3.text()) ), np.int32(self.lineEdit_4.text())))


		    elementoDominio.Dominio.rectaCandidata = QtGui.QGraphicsLineItem(QtCore.QLineF(elementoDominio.Dominio.a1, elementoDominio.Dominio.a2, elementoDominio.Dominio.b1, elementoDominio.Dominio.b2), None, elementoDominio.Dominio.scene())
		else:
		    elementoDominio.Dominio.transformarCoordenada(QtCore.QPoint( elementoDominio.Dominio.ejeEscena.x() + np.int32( np.int32(self.lineEdit.text()) ), np.int32(self.lineEdit_2.text())))

		    elementoDominio.Dominio.transformarCoordenadaY(QtCore.QPoint( elementoDominio.Dominio.ejeEscena.x() + np.int32( np.int32(self.lineEdit_3.text()) ), np.int32(self.lineEdit_4.text())))

		    elementoDominio.Dominio.rectaCandidata.setLine(QtCore.QLineF(elementoDominio.Dominio.a1, elementoDominio.Dominio.a2, elementoDominio.Dominio.b1, elementoDominio.Dominio.b2))

		    elementoDominio.ContEnsayo.actualizarRectaCandidata(np.int32(self.lineEdit.text()), np.int32(self.lineEdit_2.text()), np.int32(self.lineEdit_3.text()),
np.int32(self.lineEdit_4.text()))





    def setPozoExistente(self, idPozo):

        if elementoDominio.Dominio.rectaSeleccionada['id'] == 0:

            coordenadas = elementoDominio.ContEnsayo.retornarCoordenadas(idPozo)


            if elementoDominio.pozoSeleccionado == 0:
                self.lineEdit.setText(QtCore.QString.number(coordenadas['x'], 10))
                self.lineEdit_2.setText(QtCore.QString.number(coordenadas['y'], 10))

            self.idElemento = idPozo
            self.tipoElemento = "pozo"

            if not self.btnActualizar.isVisible():
                self.btnActualizar.setVisible(True)
                self.btnAceptar.setVisible(False)
                self.btnCancelar.setVisible(False)
                self.btnPrevia.setVisible(False)

                #Etiqueta de Tipo
                self.label.setText(QtGui.QApplication.translate("Form", "Pozo", None, QtGui.QApplication.UnicodeUTF8))
                self.label.setVisible(True)

                self.label_2.setVisible(True)
                self.label_3.setVisible(True)

                self.lineEdit.setVisible(True)
                self.lineEdit_2.setVisible(True)

                self.eliminarPlacebos()

            self.lineEdit_3.setVisible(False)
            self.lineEdit_4.setVisible(False)
            self.label_4.setVisible(False)
            self.label_5.setVisible(False)
            self.cbTipo.setVisible(False)


            self.label.setText(QtGui.QApplication.translate("Form", "Pozo", None, QtGui.QApplication.UnicodeUTF8))

    def setActualizar(self):

        elementoDominio.Dominio.rectaSeleccionada['id'] = 0

        if elementoDominio.pozoSeleccionado != 0:
            elementoDominio.ContEnsayo.moverPozo(elementoDominio.pozoSeleccionado, np.int32(self.lineEdit.text()), np.int32(self.lineEdit_2.text()))

            for pozo in elementoDominio.Dominio.botones:
                if pozo.id == elementoDominio.pozoSeleccionado:
                    pozo.setPixmap(QtGui.QPixmap("content/images/blackDotIcon.png"))

		    elementoDominio.Dominio.transformarCoordenada(QtCore.QPoint( np.int32(self.lineEdit.text()), np.int32(self.lineEdit_2.text())))

		    if np.int32(self.lineEdit.text()) == 0:
		        pozo.setX(0 - 5)
		    else:
		        pozo.setX(elementoDominio.Dominio.a1 - 15)
		    if np.int32(self.lineEdit_2.text()) == 0:
		        pozo.setY(elementoDominio.Dominio.alto - 10)
		    else:
		        pozo.setY(elementoDominio.Dominio.a2 - 10)

                    elementoDominio.pozoSeleccionado = 0
                    return

        if self.tipoElemento == "pozo":

            elementoDominio.ContEnsayo.moverPozo(self.idElemento, np.int32(self.lineEdit.text()), np.int32(self.lineEdit_2.text()))

            for pozo in elementoDominio.Dominio.botones:
                if pozo.id == self.idElemento:
			elementoDominio.Dominio.transformarCoordenada(QtCore.QPoint( np.int32(self.lineEdit.text()), np.int32(self.lineEdit_2.text())))

			if np.int32(self.lineEdit.text()) == 0:
				pozo.setX(0 - 5)
			else:
				pozo.setX(elementoDominio.Dominio.a1 - 15)
			if np.int32(self.lineEdit_2.text()) == 0:
				pozo.setY(elementoDominio.Dominio.alto - 10)
			else:
				pozo.setY(elementoDominio.Dominio.a2 - 10)

			elementoDominio.pozoSeleccionado = 0
			return


        if self.tipoElemento == "barrera":
            elementoDominio.ContEnsayo.actualizarRectaCoord(self.idElemento, np.int32(self.lineEdit.text()), np.int32(self.lineEdit_2.text()),
np.int32(self.lineEdit_3.text()),np.int32(self.lineEdit_4.text()), self.cbTipo.currentText())
            for recta in elementoDominio.Dominio.rectas:
                if recta.id == self.idElemento:
                    elementoDominio.Dominio.transformarCoordenada(QtCore.QPoint(np.int32(self.lineEdit.text()), np.int32(self.lineEdit_2.text())))

                    elementoDominio.Dominio.transformarCoordenadaY(QtCore.QPoint(np.int32(self.lineEdit_3.text()), np.int32(self.lineEdit_4.text())))

                    recta.setLine(elementoDominio.Dominio.a1, elementoDominio.Dominio.a2, elementoDominio.Dominio.b1, elementoDominio.Dominio.b2)

                    #elementoDominio.ContEnsayo.actualizarRectaCoordenada(recta.id, elementoDominio.Dominio.a1, elementoDominio.Dominio.a2, elementoDominio.Dominio.b1, elementoDominio.Dominio.b2)

                    recta.setPen(QtCore.Qt.black)
		    elementoDominio.Dominio.rectaSeleccionada['id'] = 0
		    return


    def setRectaExistente(self, idElemento, irRE):

        if elementoDominio.pozoSeleccionado == 0:
            self.tipoElemento = "barrera"
            self.idElemento = idElemento

        recta = elementoDominio.ContEnsayo.buscarRecta(self.idElemento)

        if irRE == 0:
	    if recta.x1 <= 0:
                self.lineEdit.setText(QtCore.QString.number(0, 10))
	    elif recta.x1 >= elementoDominio.Dominio.ancho:
                self.lineEdit.setText(QtCore.QString.number(elementoDominio.Dominio.ancho, 10))
	    else:
                self.lineEdit.setText(QtCore.QString.number(recta.x1, 10))

	    if recta.y1 <= 0:
                self.lineEdit_2.setText(QtCore.QString.number(0, 10))
	    elif recta.y1 >= elementoDominio.Dominio.alto:
                self.lineEdit_2.setText(QtCore.QString.number(elementoDominio.Dominio.alto, 10))
	    else:
                self.lineEdit_2.setText(QtCore.QString.number(recta.y1, 10))

	    if recta.x2 <= 0:
                self.lineEdit_3.setText(QtCore.QString.number(0, 10))
	    elif recta.x2 >= elementoDominio.Dominio.ancho:
                self.lineEdit_3.setText(QtCore.QString.number(elementoDominio.Dominio.ancho, 10))
	    else:
                self.lineEdit_3.setText(QtCore.QString.number(recta.x2, 10))
	    if recta.y2 <= 0:
                self.lineEdit_4.setText(QtCore.QString.number(0, 10))
	    elif recta.y2 >= elementoDominio.Dominio.alto:
                self.lineEdit_4.setText(QtCore.QString.number(elementoDominio.Dominio.alto, 10))
	    else:
                self.lineEdit_4.setText(QtCore.QString.number(recta.y2, 10))

	    if recta.tipo == "Positivo":
	        self.cbTipo.setCurrentIndex(1)
	    else:
	        self.cbTipo.setCurrentIndex(0)

        else:

            recta = elementoDominio.ContEnsayo.buscarRecta(irRE)
	    if recta.x1 <= 0:
                self.lineEdit.setText(QtCore.QString.number(0, 10))
	    elif recta.x1 >= elementoDominio.Dominio.ancho:
                self.lineEdit.setText(QtCore.QString.number(elementoDominio.Dominio.ancho, 10))
	    else:
                self.lineEdit.setText(QtCore.QString.number(recta.x1, 10))

	    if recta.y1 <= 0:
                self.lineEdit_2.setText(QtCore.QString.number(0, 10))
	    elif recta.y1 >= elementoDominio.Dominio.alto:
                self.lineEdit_2.setText(QtCore.QString.number(elementoDominio.Dominio.alto, 10))
	    else:
                self.lineEdit_2.setText(QtCore.QString.number(recta.y1, 10))

	    if recta.x2 <= 0:
                self.lineEdit_3.setText(QtCore.QString.number(0, 10))
	    elif recta.x2 >= elementoDominio.Dominio.ancho:
                self.lineEdit_3.setText(QtCore.QString.number(elementoDominio.Dominio.ancho, 10))
	    else:
                self.lineEdit_3.setText(QtCore.QString.number(recta.x2, 10))
	    if recta.y2 <= 0:
                self.lineEdit_4.setText(QtCore.QString.number(0, 10))
	    elif recta.y2 >= elementoDominio.Dominio.alto:
                self.lineEdit_4.setText(QtCore.QString.number(elementoDominio.Dominio.alto, 10))
	    else:
                self.lineEdit_4.setText(QtCore.QString.number(recta.y2, 10))

	    if recta.tipo == "Positivo":
	        self.cbTipo.setCurrentIndex(1)
	    else:
	        self.cbTipo.setCurrentIndex(0)



	    if recta.tipo == "Positivo":
	        self.cbTipo.setCurrentIndex(1)
	    else:
	        self.cbTipo.setCurrentIndex(0)


        if not self.btnActualizar.isVisible():

            self.btnActualizar.setVisible(True)

            self.btnAceptar.setVisible(False)
            self.btnCancelar.setVisible(False)
            self.btnPrevia.setVisible(False)

            self.lineEdit.setVisible(True)
            self.lineEdit_2.setVisible(True)
            self.eliminarPlacebos()

        self.label.setText(QtGui.QApplication.translate("Form", "Recta", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_3.setVisible(True)
        self.lineEdit_4.setVisible(True)
        self.label_5.setVisible(True)
        self.label_4.setVisible(True)
        self.label_3.setVisible(True)
	self.label_2.setVisible(True)
        self.label.setVisible(True)
        self.cbTipo.setVisible(True)

    def actualizarCoordenadasPozo(self, idPozo):
        pozo = elementoDominio.ContEnsayo.buscarPozo(idPozo)
        self.lineEdit.setText(QtCore.QString.number(pozo.x, 10))
        self.lineEdit_2.setText(QtCore.QString.number(pozo.y, 10))
        elementoDominio.Dominio.rectaSeleccionada['id'] = 0
        self.setPozoExistente(idPozo)

    def ocultarFormulario ( self ):
        #Etiqueta de Tipo
        self.label.setText(QtGui.QApplication.translate("Form", "Recta", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setVisible(False)

        #X1
        self.lineEdit.setText(QtGui.QApplication.translate("Form", "", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setVisible(False)

        #Y1
        self.lineEdit_2.setText(QtGui.QApplication.translate("Form", "", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setVisible(False)

        #X2
        self.lineEdit_3.setText(QtGui.QApplication.translate("Form", "", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_3.setVisible(False)

        #Y2
        self.lineEdit_4.setText(QtGui.QApplication.translate("Form", "", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_4.setVisible(False)

        #X1
        self.label_2.setVisible(False)


        #Y1
        self.label_3.setVisible(False)

        #X2
        self.label_4.setVisible(False)

        #Y2
        self.label_5.setVisible(False)

        #Combo
        self.cbTipo.setVisible(False)


        #Boton Aceptar
        self.btnAceptar.setVisible(False)

        #Boton Cancelar
        self.btnCancelar.setVisible(False)

        #Vista Previa
        self.btnPrevia.setVisible(False)

        #Boton Actualizar
        self.btnActualizar.setVisible(False)


    def eliminarPlacebos(self):
        if elementoDominio.ContEnsayo.hayRectaCandidata():
            elementoDominio.ContEnsayo.eliminarRectaCandidata()

        if elementoDominio.hayPozoCandidato:
            elementoDominio.pozoCandidato.hide()
            elementoDominio.pozoCandidato = None
            elementoDominio.hayPozoCandidato = False



class gbox(QtGui.QGroupBox):
	def __init__(self, parent):
		super(gbox, self).__init__(parent)

	def mouseReleaseEvent(self, e):
		elementoDominio.transicion = False
		elementoDominio.reloj = False
		self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))


class scrollArea(QtGui.QScrollArea):
	def __init__(self, parent):
		super(scrollArea, self).__init__(parent)
		self.setAcceptDrops(True)

	#Sobreescribimos dragEnterEvent para pemitir
	#la accion de este evento.
	def dragEnterEvent(self, e):
		e.accept()

"""
La clase Ui_Form es invocada en el archivo principal de la aplicacion.
su funcion es agregar los elementos correspondientes a la vista de
crear dominio
"""

class UiForm(object):

	def setupUi(self, Form, ContEnsayo, appalto, appancho):

		elementoDominio.ContEnsayo = ContEnsayo

		resolucionX=appalto
		resolucionY=appancho
		anchomaximo=resolucionX
		altomaximo=resolucionY-100

		alto=ContEnsayo.dominio.alto
		altoView=alto
		if alto<350:
			alto=350
		if alto+100>altomaximo:
			alto=altomaximo-100
			altoView=alto

		ancho=ContEnsayo.dominio.ancho
		anchoView=ancho

		if ancho<50:
			ancho=50
		if ancho+300>anchomaximo:
			ancho=anchomaximo-300
			anchoView=ancho

		principalAncho=ancho+300
		principalAlto=alto+100
		principaly=altomaximo/2-principalAlto/2

		if principaly>80:
			principaly=80
		else:
			if  principaly<=20:
				principaly=20
		principalx=anchomaximo/2-principalAncho/2

		if principalx>200:
			principalx=200
		else:
			if principalx<=0:
				principalx=0

		contenedorDominioAncho=ancho+30
		contenedorDominioAlto=alto+50

		posicionBarraTareas=ancho+100
		anchoBarraTareas=165

		segundaColY=anchoBarraTareas/2 +1



		#Seteo del formulario que contendra todos los widgets del dominio
		self.frame = QtGui.QFrame(Form) 
		self.frame.setGeometry(QtCore.QRect(principalx, principaly,principalAncho ,principalAlto))



		self.frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtGui.QFrame.Raised)
		self.frame.setObjectName(_fromUtf8("frame"))
		self.frame.setEnabled(True)

		self.frame.setStyleSheet("QFrame{border: 2px solid; }")

		self.groupBoxDominio = QtGui.QGroupBox(self.frame)
		self.groupBoxDominio.setGeometry(QtCore.QRect(20, 27, contenedorDominioAncho, contenedorDominioAlto))
		self.groupBoxDominio.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.groupBoxDominio.setTitle(QtGui.QApplication.translate("Form", "Dominio", None, QtGui.QApplication.UnicodeUTF8))

		self.groupBoxDominio.setStyleSheet("QGroupBox{background-color: white; \n"
						" border: 2px solid;}")


		#Definimos la instancia global del menu y le asociamos
		#un padre.
		elementoDominio.menuMouse = menu(self.frame)

		#Barra de Herramientas
		self.groupBox = gbox(self.frame)
		self.groupBox.setGeometry(QtCore.QRect(posicionBarraTareas, 30, anchoBarraTareas, 81))
		self.groupBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Barra Herramientas", None, QtGui.QApplication.UnicodeUTF8))

		self.groupBox.setStyleSheet("QGroupBox{border: 2px solid; border-radius: 25px;} \n"
					"QPushButton{border: 2px solid red;}")

		self.groupBox.setObjectName(_fromUtf8("groupBox"))

		#Creacion de botones de la barra de herramientas
		self.pozo = boton(QtGui.QIcon("content/images/blackDotIcon.png"), "", self.groupBox, "pozo")
		self.barrera = boton(QtGui.QIcon("content/images/blackBarrera.png"), "", self.groupBox, "barrera")
		self.zoomIn = QtGui.QPushButton(QtGui.QIcon("content/images/zoomIn.png"), "", self.groupBox)
		self.zoomOut = QtGui.QPushButton(QtGui.QIcon("content/images/zoomOut.png"), "", self.groupBox)
		self.zoomIn.setGeometry(QtCore.QRect(80, 20, 41, 23))

		self.zoomOut.setGeometry(QtCore.QRect(80, 50, 41, 23))

		self.barrera.setGeometry(QtCore.QRect(15, 50, 41, 23))

		self.barrera.id = 1001

		#coordenadas que se muestran 
		self.coordenadas = QtGui.QLabel(self.frame)
		self.coordenadas.setGeometry(QtCore.QRect(posicionBarraTareas, 375, anchoBarraTareas, 20))
		elementoDominio.coordenadas = self.coordenadas

		#Creacion de Graficas
		escena = escenaGrafica(None)

		vista = vistaGrafica(escena, self.groupBoxDominio, anchoView, altoView)
		elementoDominio.Dominio = vista

		#Caja de elementos especifica del dominio
		self.caja=elementoDominio.Dominio

		#Barra de Coordenadas
		elementoDominio.gbCoord = gbCoordenadas(self.frame, posicionBarraTareas, anchoBarraTareas, segundaColY)
		elementoDominio.gbCoord.setStyleSheet("QGroupBox{border: 2px solid; border-radius: 25px;} \n"
							"QLabel, QPushButton{border: 2px solid red;}")


		vista.show()

		QtCore.QObject.connect(self.zoomIn, QtCore.SIGNAL('clicked()'), self.clickZoomIn)
		QtCore.QObject.connect(self.zoomOut, QtCore.SIGNAL('clicked()'), self.clickZoomOut)


		self.frame.show()

	def retranslateUi(self, Form):
		pass

	def clickZoomIn(self):
		elementoDominio.Dominio.scale(2, 2)

	def clickZoomOut(self):
		elementoDominio.Dominio.scale(0.5, 0.5)
