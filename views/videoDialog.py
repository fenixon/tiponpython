# -*- coding: utf-8 -*-
from PyQt4.QtGui import * #Para la interfáz gráfica
from PyQt4.QtCore import * #Para la interfáz gráfica
from PyQt4 import QtCore

class videoDialog(QMainWindow):

    def __init__(self, figura, parent = None):
    
        QMainWindow.__init__(self, parent)

        self.figura = figura
        
        self.setWindowTitle(u'Exportar video...')
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setGeometry(0, 0, 370, 261)
        self.setMinimumSize(370, 261)
        self.setMaximumSize(370, 261)
        self.setWindowTitle(QtCore.QString('Exportar gráficas a video...'))

        vbox = QVBoxLayout()
        
        #Groupbox
        gb = QGroupBox(QtCore.QString('Opciones de video'), self)
        gb.setGeometry(10, 10, 351, 201)

        vbox.addWidget(gb)
        #Labels
        l1 = QLabel(QtCore.QString('Nombre:'), gb)
        l1.setGeometry(20, 30, 46, 13)
        #self.addWidget(l1)

        l2 = QLabel(QtCore.QString('Alto:'), gb)
        l2.setGeometry(20, 60, 46, 13)
        #self.addWidget(l2)

        l3 = QLabel(QtCore.QString('Ancho:'), gb)
        l3.setGeometry(20, 90, 46, 13)
        #self.addWidget(l3)

        l4 = QLabel(QtCore.QString('Cuadros por segundo (FPS):'), gb)
        l4.setGeometry(20, 120, 136, 13)
        l4.setToolTip(u'Cantidad de cuadros mostrados por cada segundo de reproducción')
        #self.addWidget(l4)
        
        l5 = QLabel(QtCore.QString('Directorio destino:'), gb)
        l5.setGeometry(20, 150, 88, 13)
        #self.addWidget(l5)
        #TextBoxes
        self.tb1 = QLineEdit(QtCore.QString('video'), gb)
        self.tb1.setGeometry(200, 30, 133, 20)
        self.tb1.setToolTip(u'Nombre del video')
        #self.addWidget(tb1)

        self.tb2 = QLineEdit(QtCore.QString('25'), gb)
        self.tb2.setGeometry(200, 120, 133, 20)
        self.tb2.setToolTip(u'Cantidad de cuadros mostrados por cada segundo de reproducción')
        #self.addWidget(tb2)

        self.tb3 = QLineEdit(QtCore.QString('default'), gb)
        self.tb3.setGeometry(200, 150, 91, 20)
        self.tb3.setToolTip(u'Ingrese la localización final del video,si deja default, se creará el video en el directorio videos de la aplicación')
        #self.addWidget(tb3)

        self.sb1 = QSpinBox(gb)
        self.sb1.setValue(600)
        self.sb1.setGeometry(200, 60, 133, 20)
        self.sb1.setToolTip(u'Alto del video')
        QtCore.QObject.connect(self.sb1, QtCore.SIGNAL("valueChanged(int)"), self.validatorh)
        #self.addWidget(sb1)

        self.sb2 = QSpinBox(gb)
        self.sb2.setValue(800)
        self.sb2.setGeometry(200, 90, 133, 20)
        self.sb2.setToolTip(u'Ancho del video')
        QtCore.QObject.connect(self.sb2, QtCore.SIGNAL("valueChanged(int)"), self.validatorw)
        #self.addWidget(sb2)
        #PushButtons
        pb1 = QPushButton(QtCore.QString('...'), gb)
        pb1.setGeometry(300, 150, 31, 20)
        #self.addWidget(pb1)

        pb2 = QPushButton(QtCore.QString('Aceptar'))
        pb2.setGeometry(10, 220, 75, 23)
        vbox.addWidget(pb2)
        QtCore.QObject.connect(pb2, QtCore.SIGNAL("clicked()"), self.salvar)

        pb3 = QPushButton(QtCore.QString('Cancelar'))
        pb3.setGeometry(280, 220, 75, 23)
        QtCore.QObject.connect(pb3, QtCore.SIGNAL("clocked()"), self.close)
        vbox.addWidget(pb3)

        self.setLayout(vbox)

    def validatorw(self, i):

        #Controles para mantener proporciones
        w = self.figura.fig.get_figwidth() * self.figura.fig.get_dpi()
        h = self.figura.fig.get_figheight() * self.figura.fig.get_dpi()

        if w > h:

            self.sb1.setValue(h + (i-w))

        else:

            self.sb1.setValue(h - (i-w))

    def validatorh(self, i):

        #Controles para mantener proporciones
        w = self.figura.fig.get_figwidth() * self.figura.fig.get_dpi()
        h = self.figura.fig.get_figheight() * self.figura.fig.get_dpi()

        if h > w:

            self.sb2.setValue(w + (i-h))

        else:

            self.sb2.setValue(w - (i-h))

    def salvar(self):

        #Controles para ver si estan vacios los textboxes
        err = ''
        if len(str(self.tb1.text).strip()) > 0:
            if self.sb1.value > 0:
                if self.sb2.value > 0:
                    if len(str(self.tb2.text).strip()) > 0:
                        if len(str(self.tb3.text).strip()) > 0:
        
                            self.figura.salvar(str(self.tb1.text),
                                str(self.tb3.text),
                                str(self.tb2.text),
                                str(self.tb4.text))

                            self.close()

                        else:

                            err = 'Debe completar el campo directorio.'

                    else:

                        err = 'Debe completar el campo de cuadros por segundo.'

                else:

                    err = 'Debe ingresar el ancho del video.'

            else:

                err = 'Revise el valor del alto del video.'

        else:

            err = 'Ingrese el nombre del archivo.'
