from PyQt4 import QtCore, QtGui
from pozo  import pozo
import numpy as np
import sys
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class formulario(QtCore.QAbstractListModel):

    def __init__(self,opt, parent = None):
        global o
        o=opt
        QtCore.QAbstractListModel.__init__(self,parent)
        self.parametros=[]
        self.valoresparametros=[]
        params=opt.getlistaparametros()
        for p in params:
            self.parametros.append(p.nombre)
            self.valoresparametros.append(p.valoresParametro.valor)
        print "se creo el formulario"

    def headerData(self, section, orientation, role):
            
        if role ==  QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return QtCore.QString("Valor")
            else:
                return QtCore.QString("%1").arg(self.parametros[section])
    
    def rowCount(self,  parent):
        
        return len(self.parametros)
    
    def data(self,index,role):

        if role     ==  QtCore.Qt.EditRole:
            print "se va a editar..."
            return self.valoresparametros[index.row()]

        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            value   =   self.valoresparametros[row]
            return value
    
    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def setData(self, index, value, role = QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:
            row =   index.row()
            self.valoresparametros[row]=value.toString()
            print "cambio el parametro:" + str(self.parametros[row])
            #Seteo el parametro ingresado al objeto optimizacion
            o.setvalor(row,value.toString())
            self.dataChanged.emit(index,index)
        return True

class optimizacion(QtGui.QWidget):
    def __init__(self,cont,Form):
        super(optimizacion, self).__init__()
        global controlador
        global pozosparaoptimizar
        global pozosconfirmados
        self.pozosconfirmados=[]
        controlador=cont
        self.pozosparaoptimizar=controlador.listarPozosParaOptimizar() 
        self.setupUi()
            
    def setupUi(self):
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 20, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setText(QtGui.QApplication.translate("Form", "Optimizacion", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(200, 70, 91, 16))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Metodo a Utilizar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 158, 36))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Pozos Seleccionados", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.cargardatos(self)
        self.line = QtGui.QFrame(self)
        self.line.setGeometry(QtCore.QRect(143, 70, 20, 211))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self)
        self.line_2.setGeometry(QtCore.QRect(30, 80, 261, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))        
        self.setObjectName(_fromUtf8("Form"))
        self.resize(374, 403)
        self.setWindowTitle(QtGui.QApplication.translate("Form", "Optimizacion", None, QtGui.QApplication.UnicodeUTF8))
        self.show()
    def cargardatos(self,formulario):
        #Listo los pozos que se le asociaron metodos de optimizacion
        posiciony=100
        for pozo in self.pozosparaoptimizar:
            #Creo la lista de pozos a optimizar
            #Creo el checkbox
            self.checkBox=QtGui.QCheckBox(str(pozo),self)        
            self.checkBox.stateChanged.connect(self.mensajecheckbox)
            self.checkBox.setGeometry(QtCore.QRect(40, posiciony, 69, 30))
            self.checkBox.toggle()            
            #Creo el combobox con las optimizaciones
            globals()["comboBox"+ str(pozo)]=QtGui.QComboBox(self)
            globals()["comboBox"+ str(pozo)].setGeometry(QtCore.QRect(200, posiciony, 69, 22))
            #Creo el boton para los parametros de la optimizacion
            globals()["parametro"+ str(pozo)]=QtGui.QPushButton("Parametros"+ str(pozo),self)
            globals()["parametro"+ str(pozo)].setGeometry(300,posiciony,69,22)
            globals()["parametro"+ str(pozo)].setToolTip(str(pozo))
            self.connect(globals()["parametro"+ str(pozo)], QtCore.SIGNAL('clicked()'),self.setparametros)        
            posiciony=posiciony+20
            #agrego todas las optimizaciones a combo
            globals()["comboBox"+ str(pozo)].addItem(str(self.pozosparaoptimizar[pozo]), pozo)
            globals()["comboBox"+ str(pozo)].setItemData(0,QtCore.QVariant(pozo))
            globals()["comboBox"+ str(pozo)].addItems(controlador.optimizacioneslistarmenos(str(self.pozosparaoptimizar[pozo])))
            globals()["comboBox"+ str(pozo)].setCurrentIndex(0)
            self.connect(globals()["comboBox"+ str(pozo)], QtCore.SIGNAL('currentIndexChanged(int)'),self.cambiarmetodooptimizacion)
            
        #Boton para confirmar la/s optimizaciones
        accion=QtGui.QPushButton('Procesar ',self)
        accion.setGeometry(200,posiciony + 200,60,35)
        self.connect(accion, QtCore.SIGNAL('clicked()'),self.procesar)        
    def retranslateUi(self, Form):
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        self.listWidget.setSortingEnabled(__sortingEnabled)
    def mensajecheckbox(self,state):
        print  self.checkBox
        if state == QtCore.Qt.Checked:
            #Si esta desactivado lo activo en la coleccion
            self.pozosconfirmados.append(str(self.sender().text()))
        else:
            #Si esta activado lo desactivo en la coleccion
            self.pozosconfirmados.remove(str(self.sender().text()))
    def ejemplo(coso):
        print "ejemplo"
    def setparametros(self):
        pozo=self.sender().toolTip()
        print "listo una ventana con los parametros para:" + str(self.pozosparaoptimizar[int(pozo)])
        model = formulario(self.pozosparaoptimizar[int(pozo)])
        ventana=QtGui.QDialog(self)
        ventana.setWindowTitle(', Parametros de ' + str(self.pozosparaoptimizar[int(pozo)]) )
        tableView = QtGui.QTableView(ventana)
        tableView.show()
        tableView.setModel(model)
        ventana.resize(tableView.width(), tableView.height())
        ventana.show()        
        #self.pozosparaoptimizar[int(pozo)].getparametros()

    def cambiarmetodooptimizacion(self,indice):
        #Obtengo el pozo seleccionado y le cambio el metodo de solucion al elegido
        #print "Pozo:" + str(self.sender().itemData(0).toInt()[0])
        #print "Cambiar a:" +self.sender().currentText()
        #Le asocio el nuevo metodo
        controlador.asociarPozoOptimiazion(self.sender().itemData(0).toInt()[0],self.sender().currentText())              
    def procesar(self):
        print "Proceso la matriz"
        for p in self.pozosconfirmados:
            #obtengo el pozo a optimizar
            #'''pozo=controlador.buscarPozo(p)
            #'''observaciones= pozo.observaciones[0].devolverO()
            #tiempos de las observaciones
            #'''t_obs=[]
            #'''r_obs=[]
            #'''x0=pozo.x
            #'''y0=pozo.y
            #obtengo el pozo de bombeo
            #'''pozoBombeo=controlador.obtenerDominio().obtenerPozoBombeo()
            #'''xb=pozoBombeo.x
            #'''yb=pozoBombeo.y
            #'''print "x0:" + str(x0)
            #'''print "y0:" + str(y0)
            #'''print "xb:" + str(xb)
            #'''print "yb:" + str(yb)            
            """ for o in observaciones:
                t_obs.append(o.tiempo)
                r_obs.append(np.sqrt(np.square(x0-xb) + np.square(y0-yb)))"""
            #print "Se le asigno el Metodo optimizacion:" + str(self.pozosparaoptimizar[int(p)])
            #proceso la optimizacion
            self.pozosparaoptimizar[int(p)].setcontrolador(controlador)

            T, S, f_min,obs_sim=self.pozosparaoptimizar[int(p)].cargar()
            print "Valor optimo de T: " + str(T)
            print "Valor optimo de S: " +str(S)
            print "Valor optimo de f_min: " +str(f_min)
            print "Valor optimo de obs_sim: " +str(obs_sim)
            print "------------------------------------------------"
            #print o.nivelpiezometrico
            #print "tiempo:" + str(t_obs[1])
            print "fin"
