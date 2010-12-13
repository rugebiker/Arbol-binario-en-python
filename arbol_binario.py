#!/usr/bin/python2

'''
Created on Dec 11, 2010

@author: biker
'''

import sys
from PyQt4 import QtCore, QtGui
from ventana import Ui_MainWindow

class nodo:    
    def __init__ (self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class ventanita(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.raiz = None
        QtCore.QObject.connect(self.ui.texto, QtCore.SIGNAL("returnPressed()"), self.crearnodo)
        QtCore.QObject.connect(self.ui.botonagregar, QtCore.SIGNAL("clicked()"), self.crearnodo)
        QtCore.QObject.connect(self.ui.botonretirar, QtCore.SIGNAL("clicked()"), self.inicializareliminar)
        
    def crearnodo(self):
        try:
            auxiliar = nodo(int(self.ui.texto.text()))
            if self.raiz == None:
                self.raiz = auxiliar
            else:
                self.insertar(self.raiz, auxiliar)
            self.repaint()
        except:
            print "No es un numero"
        self.ui.texto.setText("")
        self.ui.texto.setFocus()
                
    def insertar(self, auxiliar, nuevo):
        if nuevo.dato < auxiliar.dato:
            if auxiliar.izquierda == None:
                auxiliar.izquierda = nuevo
            else:
                self.insertar(auxiliar.izquierda, nuevo)
        elif nuevo.dato > auxiliar.dato:
            if auxiliar.derecha == None:
                auxiliar.derecha = nuevo
            else:
                self.insertar(auxiliar.derecha, nuevo)
        elif nuevo.dato == auxiliar.dato:
            QtGui.QMessageBox.information(self, "Aviso", "Numero repetido")
    
    def inicializareliminar(self):
        try:
            if self.raiz != None:
                if self.raiz.dato == int(self.ui.texto.text()):
                    if self.raiz.izquierda == None and self.raiz.derecha == None:
                        self.raiz = None
                    elif self.raiz.izquierda == None:
                        self.raiz = self.raiz.derecha
                    elif self.raiz.derecha == None:
                        self.raiz = self.raiz.izquierda
                    else:
                        auxiliar = self.raiz.izquierda
                        self.raiz = self.raiz.derecha
                        self.insertar(self.raiz, auxiliar)
                else:
                    try:
                        self.eliminar(self.raiz, nodo(int(self.ui.texto.text())))
                    except AttributeError:
                        print "No esta el numero"
                self.repaint()
                self.ui.texto.setText("")
                self.ui.texto.setFocus()
        except ValueError:
            print "No es un numero"
            
    def eliminar(self, auxiliar, numero):
        if numero.dato < auxiliar.dato:
            if numero.dato == auxiliar.izquierda.dato:
                if auxiliar.izquierda.izquierda == None and auxiliar.izquierda.derecha == None:
                    auxiliar.izquierda = None
                elif auxiliar.izquierda.izquierda == None:
                    auxiliar.izquierda = auxiliar.izquierda.derecha
                elif auxiliar.izquierda.derecha == None:
                    auxiliar.izquierda = auxiliar.izquierda.izquierda
                else:
                    auxiliar2 = auxiliar.izquierda.izquierda
                    auxiliar.izquierda = auxiliar.izquierda.derecha
                    self.insertar (auxiliar.izquierda, auxiliar2)
            else:
                self.eliminar(auxiliar.izquierda, numero)
        elif numero.dato > auxiliar.dato:
            if numero.dato == auxiliar.derecha.dato:
                if auxiliar.derecha.derecha == None and auxiliar.derecha.izquierda == None:
                    auxiliar.derecha = None
                elif auxiliar.derecha.izquierda == None:
                    auxiliar.derecha = auxiliar.derecha.derecha
                elif auxiliar.derecha.derecha == None:
                    auxiliar.derecha = auxiliar.derecha.izquierda
                else:
                    auxiliar2 = auxiliar.derecha.izquierda
                    auxiliar.derecha = auxiliar.derecha.derecha
                    self.insertar (auxiliar.derecha, auxiliar2)
            else:
                self.eliminar(auxiliar.derecha, numero)
         
    def paintEvent(self, event):
        paint = QtGui.QPainter()
        paint.begin(self)
        X = self.size().width()
        self.pintar(paint, self.raiz, X/2, 100, X/2)
        paint.end()
        
    def pintar(self, paint, auxiliar, X, Y, ayuda):
        if auxiliar != None :
            paint.setPen(QtGui.QColor("Red"))
            paint.drawText(X, Y, str(auxiliar.dato))
            paint.drawEllipse(X-10, Y-20, 30, 30)
            if auxiliar.izquierda != None:
                paint.setPen(QtGui.QColor("Blue"))
                paint.drawLine(X+4, Y+10, X+4-ayuda/2, Y+60)
            if auxiliar.derecha != None:
                paint.setPen(QtGui.QColor("Blue"))
                paint.drawLine(X+4, Y+10, X+4+ayuda/2, Y+60)
            self.pintar(paint, auxiliar.izquierda, X-ayuda/2, Y+80, ayuda/2)
            self.pintar(paint, auxiliar.derecha, X+ayuda/2, Y+80, ayuda/2);
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = ventanita()
    myapp.show()
    sys.exit(app.exec_())