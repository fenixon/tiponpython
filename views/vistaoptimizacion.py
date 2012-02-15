# -*- coding: utf-8 -*-

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
    
class arraymodel(QtCore.QAbstractListModel):

    def __init__(self,metodo,cont, parent = None):
        global o
        global m
        global controlador
        controlador=cont
        m=metodo
        QtCore.QAbstractListModel.__init__(self,parent)
        self.parametros=[]
        pozosobs=controlador.listarPozosObsParaOptimizar()[m]
        for p in pozosobs:
            self.parametros.append(int(p))
        print "se creo el arraymodel"

    def rowCount(self,  parent):
        
        return len(self.parametros)
    
    def data(self,index,role):

        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            value   =   self.parametros[row]
            return value
    
    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def agregar(self,nropozo):
        print "inserto"
        self.existe(nropozo)
        self.beginInsertRows(QtCore.QModelIndex(),0,5)

        self.parametros.insert(len(self.parametros),nropozo)
        controlador.asociarPozoOptimiazion(nropozo,m)
        self.endInsertRows()
        print "queda:" + str(self.parametros)
        return True
    
    def quitar(self,indice):
        print "quito:" + str(self.parametros[indice])
        self.beginRemoveRows(QtCore.QModelIndex(),0,5)
        controlador.quitarPozoOptimizacion(self.parametros[indice],m)
        self.parametros.remove(self.parametros[indice])
        self.endRemoveRows()

    def existe(self,valor):
        #Compruebo si el pozo ya existe en la lista
        if ((int(valor) in self.parametros) == True):
                #print "El valor existe"
                return True
        else:
                return False
                #print "El valor no existe"

class optimizacion(QtGui.QWidget):
    def __init__(self,cont,Formulario):
        global Form
        Form=Formulario
        super(optimizacion, self).__init__()
        global model
        global controlador
        global opt
        controlador=cont
        #Obtengo el diccionario de las asociaciones
        diccionario=controlador.listarPozosObsParaOptimizar()
        claves=diccionario.keys()
        print "claves:" + str(claves)
        if (claves!=[]):
            for clave in claves:
                print str(clave)
                self.metodoactual=str(clave)
                opt=controlador.instanciaoptimizacion(clave)
                self.modelmetodo = formulario(opt)
                model=arraymodel(clave,controlador)
                self.setupUi()
        else:
            #Si no existen asociaciones doy error
            reply = QtGui.QMessageBox.warning(self,
                            "Error",
                            "No se realizaron asociaciones desde el dominio.")
        self.padre=Formulario

    def setupUi(self):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(483, 537)
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Problema Inverso - Optimizacion", None, QtGui.QApplication.UnicodeUTF8))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 30, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setText(QtGui.QApplication.translate("Form", "Metodo", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(190, 40, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setText(QtGui.QApplication.translate("Form", self.metodoactual, None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(340, 30, 75, 23))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Parametros", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(60, 110, 201, 16))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Pozos de Observaciones involucrados:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(60, 80, 401, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        
        self.listView = QtGui.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(60, 150, 201, 192))
        self.listView.setObjectName(_fromUtf8("listView"))

        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(350, 90, 21, 321))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(70, 370, 131, 16))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Incluir ala coleccion pozo:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 370, 75, 23))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(344, 462, 111, 41))
        self.pushButton_3.setText(QtGui.QApplication.translate("Form", "Procesar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(200, 370, 31, 22))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.connect(self.pushButton, QtCore.SIGNAL('clicked()'),self.setparametros)
        self.connect(self.pushButton_2, QtCore.SIGNAL('clicked()'),self.agregarpozo)
        self.connect(self.pushButton_3, QtCore.SIGNAL('clicked()'),self.procesar)
        self.listView.setModel(model)
        QtCore.QObject.connect(self.listView, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), self.quitarPozoObs)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.ventana=QtGui.QDialog(self)
        self.ventana.setWindowTitle('Parametros - Ajustes')
        tableView = QtGui.QTableView(self.ventana)
        tableView.show()
        tableView.setModel(self.modelmetodo)
        self.ventana.resize(tableView.width(), tableView.height())

    def retranslateUi(self, Form):
        pass

    def agregarpozo(self):
        #al hacer click en el boton agrego el pozo que se ingreso en la cajita de texto
        #Verifico si ya existe el pozo
        if (model.existe(int(self.lineEdit.text()))==False):
            #Busco si el pozo ingresado existe en el dominio
            existe=controlador.buscarPozo(int(self.lineEdit.text()))
            if (existe!=None):
                #Busco si es un pozo que tiene observaciones
                if len(controlador.buscarPozo(int(self.lineEdit.text())).observaciones)>0:
                    #Si tiene observaciones lo agrego
                    model.agregar(int(self.lineEdit.text()))
                else:
                    #Si no tiene observaciones mando error
                    reply = QtGui.QMessageBox.warning(self,
                            "Error",
                            "El pozo ingresado, NO tiene observaciones asociadas.")                
            else:
                #Si no existe en el dominio doy error
                reply = QtGui.QMessageBox.warning(self,
                            "Error",
                            "El pozo ingresado no existe en el dominio.") 
        else:
                #Si ya existe muestro error
                reply = QtGui.QMessageBox.warning(self,
                            "Error",
                            "Ya se ha agregado el pozo de observacion") 
    def quitarPozoObs(self,item):
        #al hacer click en un elemento(pozo de la lista) solicito confirmacion para eliminarlo
        reply = QtGui.QMessageBox.question(self,"Confirmacion",
                            "Realmente desea quitar el pozo seleccionado?. ",
                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)        
        if reply == QtGui.QMessageBox.Yes:
                model.quitar(item.row())

    def setparametros(self):
        #Muestro la ventana para editar los parametros
        self.ventana.show()

    def procesar(self):
        print "Proceso Calitheis2"
        opt.setcontrolador(controlador)
        opt.setpozos(controlador.listarPozosObsParaOptimizar()[m])
        T, S, f_min,obs_sim=opt.calcular()
        print "Valor optimo de T: " + str(T)
        print "Valor optimo de S: " +str(S)
        print "Valor optimo de f_min: " +str(f_min)
        print "Valor optimo de obs_sim: " +str(obs_sim)
        print "------------------------------------------------"
        print "fin"

        reply = QtGui.QMessageBox.information(self,u"Información",u"El proceso de optimización a concluido")
        self.padre.close()        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = optimizacion([1,2,3],Form)
    ui.setupUi()
    Form.show()
    dic={}
    #dic["clave"]=[]
    #dic["CaliTheis"]=[]
    #dic["clave"].append('valor1')
    #dic["clave"].append('valor2')
    #dic["clave"].append('valor3')

    metodo="ricardo"
    claves=dic.keys()

    #Busco el indice del metodo
    token=False
    for clave in claves:
        if (clave==metodo):
            #Si existe el metodo en el diccionario, le agrego el pozo
            token=True
            dic[clave].append('coso1pa')
    if (token==False): #Si no existe el metodo, lo creo y le agrego el pozo
        dic[metodo]=[]
        dic[metodo].append('coso1')

    print dic
    sys.exit(app.exec_())

