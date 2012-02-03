# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graficarOpt.ui'
#
# Created: Tue Jan 31 16:24:14 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

from models.dominio import dominio
from views.dibujanteOpt import dibujanteOpt

import numpy as np

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class graficarOpt(object):

    def setupUi(self, graficarOpt, dominio, ti, tf, nit):

        graficarOpt.setObjectName(_fromUtf8("graficarOpt"))
        graficarOpt.setMinimumSize(373, 131)
        graficarOpt.setMaximumSize(373, 131)
#        graficarOpt.resize(373, 131)
        graficarOpt.setWindowTitle(QtGui.QApplication.translate("graficarOpt", "Graficar Optimizaciones", None, QtGui.QApplication.UnicodeUTF8))
        self.label = QtGui.QLabel(graficarOpt)
        self.label.setGeometry(QtCore.QRect(40, 10, 131, 41))
        self.label.setText(QtGui.QApplication.translate("graficarOpt", "Pozo de observación:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.grafParametros = QtGui.QPushButton(graficarOpt)
        self.grafParametros.setGeometry(QtCore.QRect(40, 70, 131, 31))
        self.grafParametros.setText(QtGui.QApplication.translate("graficarOpt", "Grafica de Parametros", None, QtGui.QApplication.UnicodeUTF8))
        self.grafParametros.setObjectName(_fromUtf8("grafParametros"))

        QtCore.QObject.connect(self.grafParametros, QtCore.SIGNAL(_fromUtf8('clicked()')), self.grafParametrosFunc)
        self.ti=ti
        self.tf=tf
        self.nit=nit
        self.dib = None

        self.grafObservaciones = QtGui.QPushButton(graficarOpt)
        self.grafObservaciones.setGeometry(QtCore.QRect(200, 70, 131, 31))
        self.grafObservaciones.setText(QtGui.QApplication.translate("graficarOpt", "Graficar observaciones", None, QtGui.QApplication.UnicodeUTF8))
        QtCore.QObject.connect(self.grafObservaciones, QtCore.SIGNAL(_fromUtf8('clicked()')), self.grafObservacionesFunc)
        self.grafObservaciones.setObjectName(_fromUtf8("grafObservaciones"))
        self.pozo = QtGui.QComboBox(graficarOpt)
        self.pozo.setGeometry(QtCore.QRect(200, 20, 131, 21))
        self.pozo.setObjectName(_fromUtf8("pozo"))
        self.dominio = dominio
        self.cargarCombo()
        self.retranslateUi(graficarOpt)
        QtCore.QMetaObject.connectSlotsByName(graficarOpt)

    def retranslateUi(self, graficarOpt):
        pass

    def cargarCombo(self):

        lista = self.dominio.listaPozoOptimiza

        for i in lista:

            self.pozo.addItem(QtCore.QString(str(lista[i].pozo.id)), lista[i].pozo.id)

    def grafParametrosFunc(self):

        lista = self.dominio.listaPozoOptimiza
        pozoActual = self.dominio.listaPozoOptimiza[self.pozo.itemData(self.pozo.currentIndex()).toPyObject()]
        self.dib = None

        if self.dib != None:

            self.dib.raise_()

        else:

            tMin = float(pozoActual.listaParametros[0].valoresParametro.valor)
            tMax = float(pozoActual.listaParametros[1].valoresParametro.valor)
            sMin = float(pozoActual.listaParametros[2].valoresParametro.valor)
            sMax = float(pozoActual.listaParametros[3].valoresParametro.valor)

            N_int_T = int(pozoActual.listaParametros[4].valoresParametro.valor)
            N_int_S = int(pozoActual.listaParametros[5].valoresParametro.valor)

            x = np.linspace(tMin, tMax, N_int_T)
            y = np.linspace(sMin, sMax, N_int_S)
            z = pozoActual.obj

            self.dib = dibujanteOpt(x, y, z, [pozoActual.T], [pozoActual.S])
            self.dib.show()
            QtCore.QObject.connect(self.dib, QtCore.SIGNAL(_fromUtf8("destroyed()")), self.limpiarDibujante)

    def grafObservacionesFunc(self):

        pozoActual = self.dominio.listaPozoOptimiza[self.pozo.itemData(self.pozo.currentIndex()).toPyObject()]
        self.dib = None

        if self.dib != None:

            self.dib.raise_()

        else:

            T = float(pozoActual.T)
            S = float(pozoActual.S)
            pozoObservacion=pozoActual.pozo

##            print 'T '+str(T)
##            print 'S '+str(S)
##            print 'timepos '+str(self.dominio.metodo.tiempos)

            self.dominio.metodo.funcionObjetivo(T,S,pozoObservacion)

            h = pozoObservacion.devolverNivelesOptimos()
            print 'h ' + str(h)

            ##discretizacion temporal
            nit=self.nit
            dt=(self.tf-self.ti)/nit
            nit=nit+1
            tiempos=np.zeros((nit),float)
            tiempos[0]=self.ti

            for i in range(1,nit):

                tiempos[i]=tiempos[i-1]+dt

            t = tiempos
            print 'tiempos '+ str(t)
            z=None
            xx=[]
            yy=[]

            for conjob in pozoObservacion.observaciones:

                ##Obtener todas las observacion del conjunto de observaciones
                self.observaciones=conjob.devolverO()

                for ob in self.observaciones:
                    xx.append(ob.tiempo)
                    yy.append(ob.nivelpiezometrico)

            print 'xx '+str(xx)
            print 'yy '+str(yy)

            self.dib = dibujanteOpt(t, h, z, xx, yy)
            self.dib.show()
            QtCore.QObject.connect(self.dib, QtCore.SIGNAL(_fromUtf8("destroyed()")), self.limpiarDibujante)

    def limpiarDibujante(self):

        self.dib = None
